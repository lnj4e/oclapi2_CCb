from django.urls import re_path, path

from core.collections.feeds import CollectionFeed
from core.common.constants import NAMESPACE_PATTERN
from . import views

urlpatterns = [
    re_path(r'^$', views.CollectionListView.as_view(), name='collection-list'),
    re_path(
        fr"^(?P<collection>{NAMESPACE_PATTERN})/$",
        views.CollectionRetrieveUpdateDestroyView.as_view(),
        name='collection-detail'
    ),
    re_path(
        r'^(?P<collection>' + NAMESPACE_PATTERN + ')/client-configs/$',
        views.CollectionClientConfigsView.as_view(),
        name='collection-client-configs'
    ),
    re_path(
        fr"^(?P<collection>{NAMESPACE_PATTERN})/summary/$",
        views.CollectionSummaryView.as_view(),
        name='collection-summary'
    ),
    re_path(
        fr"^(?P<collection>{NAMESPACE_PATTERN})/logo/$",
        views.CollectionLogoView.as_view(),
        name='collection-logo'
    ),
    re_path(
        fr'^(?P<collection>{NAMESPACE_PATTERN})/versions/$',
        views.CollectionVersionListView.as_view(),
        name='collection-version-list'
    ),
    re_path(fr'^(?P<collection>{NAMESPACE_PATTERN})/concepts/atom/$', CollectionFeed()),
    re_path(
        fr'^(?P<collection>{NAMESPACE_PATTERN})/latest/$',
        views.CollectionLatestVersionRetrieveUpdateView.as_view(),
        name='collectionversion-latest-detail'
    ),
    re_path(
        fr'^(?P<collection>{NAMESPACE_PATTERN})/latest/summary/$',
        views.CollectionLatestVersionSummaryView.as_view(),
        name='collectionversion-latest-summary'
    ),
    re_path(
        fr'^(?P<collection>{NAMESPACE_PATTERN})/latest/export/$',
        views.CollectionVersionExportView.as_view(),
        name='collectionversion-latest-export-detail'
    ),
    path(
        "<str:collection>/concepts/<str:concept>/mappings/",
        views.CollectionVersionConceptMappingsView.as_view(),
        name='concept-mappings'
    ),
    path(
        "<str:collection>/concepts/<str:concept>/<str:concept_version>/mappings/",
        views.CollectionVersionConceptMappingsView.as_view(),
        name='concept-version-mappings'
    ),
    path(
        "<str:collection>/concepts/<str:concept>/<str:concept_version>/",
        views.CollectionVersionConceptRetrieveView.as_view(),
        name='concept-version-detail'
    ),
    path(
        "<str:collection>/concepts/<str:concept>/",
        views.CollectionVersionConceptRetrieveView.as_view(),
        name='concept-detail'
    ),
    re_path(
        fr"^(?P<collection>{NAMESPACE_PATTERN})/concepts/",
        views.CollectionVersionConceptsView.as_view(),
        name='concept-list'
    ),
    path(
        "<str:collection>/mappings/<str:mapping>/<str:mapping_version>/",
        views.CollectionVersionMappingRetrieveView.as_view(),
        name='mapping-version-detail'
    ),
    path(
        "<str:collection>/mappings/<str:mapping>/",
        views.CollectionVersionMappingRetrieveView.as_view(),
        name='mapping-detail'
    ),
    re_path(
        fr"^(?P<collection>{NAMESPACE_PATTERN})/mappings/",
        views.CollectionVersionMappingsView.as_view(),
        name='mapping-list'
    ),
    re_path(
        fr'^(?P<collection>{NAMESPACE_PATTERN})/references/$',
        views.CollectionReferencesView.as_view(),
        name='collection-references'
    ),
    re_path(
        r'^(?P<collection>{pattern})/references/(?P<reference>{pattern})/$'.format(pattern=NAMESPACE_PATTERN),
        views.CollectionReferenceView.as_view(),
        name='collection-reference'
    ),
    re_path(
        r'^(?P<collection>{pattern})/references/(?P<reference>{pattern})/concepts/$'.format(pattern=NAMESPACE_PATTERN),
        views.CollectionReferenceConceptsView.as_view(),
        name='collection-reference-concepts-list'
    ),
    re_path(
        r'^(?P<collection>{pattern})/references/(?P<reference>{pattern})/mappings/$'.format(pattern=NAMESPACE_PATTERN),
        views.CollectionReferenceMappingsView.as_view(),
        name='collection-reference-mappings-list'
    ),
    re_path(
        fr"^(?P<collection>{NAMESPACE_PATTERN})/extras/$",
        views.CollectionExtrasView.as_view(),
        name='collection-extras'
    ),
    re_path(
        r'^(?P<collection>{pattern})/(?P<version>{pattern})/$'.format(pattern=NAMESPACE_PATTERN),
        views.CollectionVersionRetrieveUpdateDestroyView.as_view(),
        name='collection-version-detail'
    ),
    re_path(
        r'^(?P<collection>{pattern})/(?P<version>{pattern})/summary/$'.format(pattern=NAMESPACE_PATTERN),
        views.CollectionVersionSummaryView.as_view(),
        name='collection-version-summary'
    ),
    re_path(
        r'^(?P<collection>{pattern})/(?P<version>{pattern})/expansions/$'.format(pattern=NAMESPACE_PATTERN),
        views.CollectionVersionExpansionsView.as_view(),
        name='expansion-list'
    ),
    re_path(
        r'^(?P<collection>{pattern})/(?P<version>{pattern})/expansions/(?P<expansion>{pattern})/$'.format(
            pattern=NAMESPACE_PATTERN),
        views.CollectionVersionExpansionView.as_view(),
        name='collection-version-expansion-detail'
    ),
    path(
        "<str:collection>/<str:version>/expansions/<str:expansion>/concepts/<str:concept>/mappings/",
        views.CollectionVersionExpansionConceptMappingsView.as_view(),
        name='concept-mappings'
    ),
    path(
        "<str:collection>/<str:version>/expansions/<str:expansion>/concepts/<str:concept>/<str:concept_version>/mappings/",  # pylint: disable=line-too-long
        views.CollectionVersionExpansionConceptMappingsView.as_view(),
        name='concept-version-mappings'
    ),
    path(
        "<str:collection>/<str:version>/expansions/<str:expansion>/concepts/<str:concept>/<str:concept_version>/",
        views.CollectionVersionExpansionConceptRetrieveView.as_view(),
        name='concept-version-detail'
    ),
    path(
        "<str:collection>/<str:version>/expansions/<str:expansion>/concepts/index/",
        views.ExpansionConceptsIndexView.as_view(),
        name='expansion-concepts-index'
    ),
    path(
        "<str:collection>/<str:version>/expansions/<str:expansion>/concepts/<str:concept>/",
        views.CollectionVersionExpansionConceptRetrieveView.as_view(),
        name='concept-detail'
    ),
    path(
        "<str:collection>/<str:version>/expansions/<str:expansion>/mappings/<str:mapping>/<str:mapping_version>/",
        views.CollectionVersionExpansionMappingRetrieveView.as_view(),
        name='mapping-version-detail'
    ),
    path(
        "<str:collection>/<str:version>/expansions/<str:expansion>/mappings/index/",
        views.ExpansionMappingsIndexView.as_view(),
        name='expansion-mappings-index'
    ),
    path(
        "<str:collection>/<str:version>/expansions/<str:expansion>/mappings/<str:mapping>/",
        views.CollectionVersionExpansionMappingRetrieveView.as_view(),
        name='mapping-detail'
    ),
    re_path(
        r'^(?P<collection>{pattern})/(?P<version>{pattern})/expansions/(?P<expansion>{pattern})/concepts/$'.format(
            pattern=NAMESPACE_PATTERN),
        views.CollectionVersionExpansionConceptsView.as_view(),
        name='collection-version-expansion-concepts'
    ),
    re_path(
        r'^(?P<collection>{pattern})/(?P<version>{pattern})/expansions/(?P<expansion>{pattern})/mappings/$'.format(
            pattern=NAMESPACE_PATTERN),
        views.CollectionVersionExpansionMappingsView.as_view(),
        name='collection-version-expansion-mappings'
    ),
    re_path(
        r"^(?P<collection>{pattern})/extras/(?P<extra>{pattern})/$".format(pattern=NAMESPACE_PATTERN),
        views.CollectionExtraRetrieveUpdateDestroyView.as_view(),
        name='collection-extra'
    ),
    re_path(
        r'^(?P<collection>{pattern})/(?P<version>{pattern})/export/$'.format(pattern=NAMESPACE_PATTERN),
        views.CollectionVersionExportView.as_view(), name='collectionversion-export'
    ),
    re_path(
        r"^(?P<collection>{pattern})/(?P<version>{pattern})/extras/$".format(pattern=NAMESPACE_PATTERN),
        views.CollectionExtrasView.as_view(),
        name='collectionversion-extras'
    ),
    re_path(
        r"^(?P<collection>{pattern})/(?P<version>{pattern})/extras/(?P<extra>{pattern})/$".format(
            pattern=NAMESPACE_PATTERN
        ),
        views.CollectionExtraRetrieveUpdateDestroyView.as_view(),
        name='collectionversion-extra'
    ),
    path(
        "<str:collection>/<str:version>/concepts/<str:concept>/<str:concept_version>/mappings/",
        views.CollectionVersionConceptMappingsView.as_view(),
        name='concept-version-mappings'
    ),
    path(
        "<str:collection>/<str:version>/concepts/<str:concept>/mappings/",
        views.CollectionVersionConceptMappingsView.as_view(),
        name='concept-mappings'
    ),
    path(
        "<str:collection>/<str:version>/concepts/<str:concept>/<str:concept_version>/",
        views.CollectionVersionConceptRetrieveView.as_view(),
        name='concept-version-detail'
    ),
    path(
        "<str:collection>/<str:version>/concepts/<str:concept>/",
        views.CollectionVersionConceptRetrieveView.as_view(),
        name='concept-detail'
    ),
    re_path(
        r"^(?P<collection>{pattern})/(?P<version>{pattern})/concepts/".format(
            pattern=NAMESPACE_PATTERN
        ),
        views.CollectionVersionConceptsView.as_view(),
        name='concept-list'
    ),
    path(
        "<str:collection>/<str:version>/mappings/<str:mapping>/<str:mapping_version>/",
        views.CollectionVersionMappingRetrieveView.as_view(),
        name='mapping-version-detail'
    ),
    path(
        "<str:collection>/<str:version>/mappings/<str:mapping>/",
        views.CollectionVersionMappingRetrieveView.as_view(),
        name='mapping-detail'
    ),
    re_path(
        r"^(?P<collection>{pattern})/(?P<version>{pattern})/mappings/".format(
            pattern=NAMESPACE_PATTERN
        ),
        views.CollectionVersionMappingsView.as_view(),
        name='mapping-list'
    ),
    re_path(
        r'^(?P<collection>{pattern})/(?P<version>{pattern})/references/(?P<reference>{pattern})/$'.format(
            pattern=NAMESPACE_PATTERN),
        views.CollectionReferenceView.as_view(),
        name='collectionversion-reference'
    ),
    re_path(
        r'^(?P<collection>{pattern})/(?P<version>{pattern})/references/(?P<reference>{pattern})/concepts/$'.format(
            pattern=NAMESPACE_PATTERN),
        views.CollectionReferenceConceptsView.as_view(),
        name='collectionversion-reference-concepts-list'
    ),
    re_path(
        r'^(?P<collection>{pattern})/(?P<version>{pattern})/references/(?P<reference>{pattern})/mappings/$'.format(
            pattern=NAMESPACE_PATTERN),
        views.CollectionReferenceMappingsView.as_view(),
        name='collectionversion-reference-mappings-list'
    ),
    re_path(
        r'^(?P<collection>{pattern})/(?P<version>{pattern})/references/$'.format(pattern=NAMESPACE_PATTERN),
        views.CollectionVersionReferencesView.as_view(),
        name='collectionversion-references'
    ),
    re_path(
        r'^(?P<collection>{pattern})/(?P<version>{pattern})/processing/$'.format(pattern=NAMESPACE_PATTERN),
        views.CollectionVersionProcessingView.as_view(),
        name='collectionversion-processing'
    ),
]
