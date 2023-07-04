from django.db.models import Case, When, IntegerField
from elasticsearch_dsl import FacetedSearch, Q
from pydash import compact, get


class CustomESFacetedSearch(FacetedSearch):
    def __init__(self, query=None, filters={}, sort=(), exact_match=False):  # pylint: disable=dangerous-default-value
        self.exact_match = exact_match
        super().__init__(query=query, filters=filters, sort=sort)

    def format_search_str(self, search_str):
        if self.exact_match:
            return search_str.replace('*', '')
        return f"{search_str}*".replace('**', '*')

    def query(self, search, query):
        if query:
            search_str = self.format_search_str(query)
            if self.fields:
                return search.filter('query_string', fields=self.fields, query=search_str)

            return search.query('multi_match', query=search_str)

        return search

    def params(self, **kwargs):
        self._s = self._s.params(**kwargs)


class CustomESSearch:
    def __init__(self, dsl_search):
        self._dsl_search = dsl_search
        self.queryset = None
        self.max_score = None
        self.scores = {}
        self.highlights = {}
        self.score_stats = None
        self.score_distribution = None
        self.total = 0

    @staticmethod
    def get_match_phrase_criteria(field, search_str, boost):
        return CustomESSearch.get_term_match_criteria(
            field, search_str, boost
        ) | CustomESSearch.get_prefix_criteria(
            field, search_str, boost
        ) | Q('match_phrase', **{field: {'query': search_str, 'boost': boost}})

    @staticmethod
    def get_term_match_criteria(field, search_str, boost):
        return Q(
            'term', **{field: {'value': search_str, 'boost': boost + 100}}
        )

    @staticmethod
    def get_prefix_match_criteria(field, search_str, boost):
        return Q(
            'prefix', **{
                field: {
                    'value': search_str,
                    'boost': boost + 95
                }
            }
        )

    @staticmethod
    def get_prefix_criteria(field, search_str, boost):
        return Q(
            'prefix', **{
                field: {
                    'value': search_str,
                    'boost': boost + 95
                }
            }
        )

    @staticmethod
    def get_match_criteria(field, search_str, boost):
        return Q('match', **{field: {'query': search_str, 'boost': boost}})

    @staticmethod
    def get_wildcard_criteria(field, search_str, boost):
        return Q("wildcard", **{field: {'value': search_str, 'boost': boost, 'case_insensitive': True}})

    @staticmethod
    def fuzzy_criteria(search_str, field, boost=0, max_expansions=10):
        criterion = CustomESSearch.__fuzzy_criteria(boost, field, max_expansions, search_str)
        words = compact(search_str.split())
        if len(words) > 1:
            for word in words:
                criterion |= CustomESSearch.__fuzzy_criteria(boost, field, max_expansions, word)
        return criterion

    @staticmethod
    def __fuzzy_criteria(boost, field, max_expansions, word):
        return Q(
            {
                'fuzzy': {
                    field: {
                        'value': word,
                        'boost': boost,
                        'fuzziness': 'AUTO',
                        'max_expansions': max_expansions
                    }
                }
            }
        )

    def apply_aggregation_score_histogram(self):
        self._dsl_search.aggs.bucket(
            "distribution", "histogram", script="_score", interval=1, min_doc_count=1)

    def apply_aggregation_score_stats(self):
        self._dsl_search.aggs.bucket("score", "stats", script="_score")

    def to_queryset(self, keep_order=True):
        """
        This method return a django queryset from the an elasticsearch result.
        It cost a query to the sql db.
        """
        s, hits = self.__get_response()

        for result in hits.hits:
            _id = get(result, '_id')
            self.scores[int(_id)] = get(result, '_score')
            highlight = get(result, 'highlight')
            if highlight:
                self.highlights[int(_id)] = highlight.to_dict()

        pks = [result.meta.id for result in s]

        qs = self._dsl_search._model.objects.filter(pk__in=pks)  # pylint: disable=protected-access

        if keep_order:
            preserved_order = Case(
                *[When(pk=pk, then=pos) for pos, pk in enumerate(pks)],
                output_field=IntegerField()
            )
            qs = qs.order_by(preserved_order)
        self.queryset = qs
        self.total = hits.total.value

    def get_aggregations(self, verbose=False, raw=False):
        s, _ = self.__get_response()

        result = s.aggs.to_dict()
        if raw:
            return result
        self.max_score = result['score']['max']
        return self._get_score_buckets(
            self.max_score, result['distribution']['buckets'], verbose)

    @staticmethod
    def _get_score_buckets(max_score, buckets, verbose=False):
        high_threshold = max_score * 0.8
        low_threshold = max_score * 0.5

        def get_confidence(threshold):
            return round((threshold/max_score) * 100, 2)

        def build_confidence(_bucket):
            scores = _bucket['scores']
            if scores:
                _bucket['confidence'] = f"~{get_confidence(sum(scores) / len(scores))}%"
            if not verbose:
                _bucket = {k: v for k, v in _bucket.items() if k in ['name', 'threshold', 'total', 'confidence']}
            return _bucket

        def build_bucket(name, confidence_threshold, threshold=None, confidence_prefix='>='):
            threshold = threshold or confidence_threshold
            return {
                'name': name,
                'threshold': round(threshold, 2),
                'scores': [],
                'doc_counts': [],
                'confidence': f"{confidence_prefix}{get_confidence(confidence_threshold)}%",
                'total': 0
            }

        def append_to_bucket(_bucket, _score, count):
            _bucket['scores'].append(_score)
            _bucket['doc_counts'].append(count)
            _bucket['total'] += count

        high = build_bucket('high', high_threshold)
        medium = build_bucket('medium', low_threshold)
        low = build_bucket('low', low_threshold, 0.01, '<')

        for bucket in buckets:
            score = bucket['key']
            doc_count = bucket['doc_count']

            if score >= high_threshold:
                append_to_bucket(high, score, doc_count)
            elif score < low_threshold:
                append_to_bucket(low, score, doc_count)
            else:
                append_to_bucket(medium, score, doc_count)

        return [build_confidence(high), build_confidence(medium), build_confidence(low)]

    def __get_response(self):
        # Do not query again if the es result is already cached
        if not hasattr(self._dsl_search, '_response'):
            # We only need the meta fields with the models ids
            s = self._dsl_search.source(excludes=['*'])
            s = s.execute()
            hits = s.hits
            self.max_score = hits.max_score
            return s, hits
        return self._dsl_search, None
