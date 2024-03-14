import re

HEAD = 'HEAD'
TEMP = '--TEMP--'
TEMP_PREFIX = f"{TEMP}-"


NAMESPACE_PATTERN = r'[a-zA-Z0-9\-\.\_\@]+'
NAMESPACE_REGEX = re.compile(r'^' + NAMESPACE_PATTERN + '$')

ACCESS_TYPE_VIEW = 'View'
ACCESS_TYPE_EDIT = 'Edit'
ACCESS_TYPE_NONE = 'None'
DEFAULT_ACCESS_TYPE = ACCESS_TYPE_VIEW
ACCESS_TYPE_CHOICES = ((ACCESS_TYPE_VIEW, 'View'),
                       (ACCESS_TYPE_EDIT, 'Edit'),
                       (ACCESS_TYPE_NONE, 'None'))
SUPER_ADMIN_USER_ID = 1
OCL_ORG_ID = 1
VERBOSE_PARAM = 'verbose'
RAW_PARAM = 'raw'
BRIEF_PARAM = 'brief'
UPDATED_SINCE_PARAM = 'updatedSince'
UPDATED_BY_USERNAME_PARAM = 'updatedBy'
LAST_LOGIN_SINCE_PARAM = 'lastLoginSince'
LAST_LOGIN_BEFORE_PARAM = 'lastLoginBefore'
DATE_JOINED_SINCE_PARAM = 'dateJoinedSince'
DATE_JOINED_BEFORE_PARAM = 'dateJoinedBefore'
RELEASED_PARAM = 'released'
PROCESSING_PARAM = 'processing'
ISO_639_1 = 'ISO 639-1'
NA = 'n/a'
YES = 'yes'
NO = 'no'
DEFAULT_VALIDATION_SCHEMA = 'None'
OPENMRS_VALIDATION_SCHEMA = 'OpenMRS'
VALIDATION_SCHEMAS = ((DEFAULT_VALIDATION_SCHEMA, DEFAULT_VALIDATION_SCHEMA),
                      (OPENMRS_VALIDATION_SCHEMA, OPENMRS_VALIDATION_SCHEMA))
LOOKUP_CONCEPT_CLASSES = ['Concept Class', 'Datatype', 'NameType', 'DescriptionType', 'MapType', 'Locale']
REFERENCE_VALUE_SOURCE_MNEMONICS = ['Classes', 'Datatypes', 'NameTypes', 'DescriptionTypes', 'Locales']
FIVE_MINS = 5 * 60
INCLUDE_RETIRED_PARAM = 'includeRetired'
INCLUDE_MAPPINGS_PARAM = 'includeMappings'
INCLUDE_SEARCH_META_PARAM = 'includeSearchMeta'
INCLUDE_CONCEPTS_PARAM = 'includeConcepts'
INCLUDE_EXTRAS_PARAM = 'includeExtras'
INCLUDE_PARENT_CONCEPTS = 'includeParentConcepts'
INCLUDE_CHILD_CONCEPTS = 'includeChildConcepts'
INCLUDE_HIERARCHY_PATH = 'includeHierarchyPath'
INCLUDE_PARENT_CONCEPT_URLS = 'includeParentConceptURLs'
INCLUDE_CHILD_CONCEPT_URLS = 'includeChildConceptURLs'
INCLUDE_INVERSE_MAPPINGS_PARAM = 'includeInverseMappings'
INCLUDE_SUBSCRIBED_ORGS = 'includeSubscribedOrgs'
INCLUDE_PINS = 'includePins'
INCLUDE_CLIENT_CONFIGS = 'includeClientConfigs'
INCLUDE_OVERVIEW = 'includeOverview'
INCLUDE_CREATOR_PINS = 'includeCreatorPins'
INCLUDE_HIERARCHY_ROOT = 'includeHierarchyRoot'
INCLUDE_SUMMARY = 'includeSummary'
INCLUDE_VERBOSE_REFERENCES = 'includeReferences'
INCLUDE_VERIFICATION_TOKEN = 'includeVerificationToken'
INCLUDE_AUTH_GROUPS = 'includeAuthGroups'
INCLUDE_INACTIVE = 'includeInactive'
INCLUDE_SOURCE_VERSIONS = 'includeSourceVersions'
INCLUDE_COLLECTION_VERSIONS = 'includeCollectionVersions'
MAPPING_LOOKUP_CONCEPTS = 'lookupConcepts'
MAPPING_LOOKUP_FROM_CONCEPT = 'lookupFromConcept'
MAPPING_LOOKUP_TO_CONCEPT = 'lookupToConcept'
MAPPING_LOOKUP_SOURCES = 'lookupSources'
MAPPING_LOOKUP_FROM_SOURCE = 'lookupFromSource'
MAPPING_LOOKUP_TO_SOURCE = 'lookupToSource'
LIMIT_PARAM = 'limit'
OFFSET_PARAM = 'offset'
FHIR_LIMIT_PARAM = '_count'
LIST_DEFAULT_LIMIT = 25
CSV_DEFAULT_LIMIT = 1000
SEARCH_PARAM = 'q'
INCLUDE_FACETS = 'HTTP_INCLUDEFACETS'
SEARCH_LATEST_REPO_VERSION = 'HTTP_INCLUDESEARCHLATEST'
INCLUDE_SEARCH_STATS = 'HTTP_INCLUDESEARCHSTATS'
FACETS_ONLY = 'facetsOnly'
SEARCH_STATS_ONLY = 'searchStatsOnly'
HTTP_COMPRESS_HEADER = 'HTTP_COMPRESS'
NOT_FOUND = 'Not found.'
OK_MESSAGE = 'ok!'
PERSIST_NEW_ERROR_MESSAGE = "An error occurred while trying to persist new {}."
MUST_SPECIFY_EXTRA_PARAM_IN_BODY = 'Must specify {} param in body.'
SOURCE_PARENT_CANNOT_BE_NONE = 'Source parent cannot be None.'
INVALID_EXPANSION_URL = "Expansion URL doesn't exists"
PARENT_RESOURCE_CANNOT_BE_NONE = 'Parent resource cannot be None.'
CREATOR_CANNOT_BE_NONE = 'Creator cannot be None.'
CANNOT_DELETE_ONLY_VERSION = 'Cannot delete only version.'
BULK_IMPORT_QUEUES_COUNT = 4
MAX_PINS_ALLOWED = 4
CONFIRM_EMAIL_ADDRESS_MAIL_SUBJECT = "Confirm E-mail Address"
PASSWORD_RESET_MAIL_SUBJECT = "Password Reset E-mail"
LATEST = 'latest'
VERSION_HEADER = 'X-OCL-API-VERSION'
REQUEST_USER_HEADER = 'X-OCL-REQUEST-USER'
RESPONSE_TIME_HEADER = 'X-OCL-RESPONSE-TIME'
REQUEST_URL_HEADER = 'X-OCL-REQUEST-URL'
REQUEST_METHOD_HEADER = 'X-OCL-REQUEST-METHOD'
DEPRECATED_API_HEADER = 'X-OCL-API-DEPRECATED'
CHECKSUM_STANDARD_HEADER = 'X-OCL-API-STANDARD-CHECKSUM'
CHECKSUM_SMART_HEADER = 'X-OCL-API-SMART-CHECKSUM'
CREATE_PARENT_VERSION_QUERY_PARAM = 'createParentVersion'
CURRENT_USER = 'CURRENT_USER'
REQUEST_URL = 'REQUEST_URL'
ES_REQUEST_TIMEOUT = 60  # seconds, default is 10
ES_REQUEST_TIMEOUT_ASYNC = 60 * 5  # seconds, default is 10
CASCADE_METHOD_PARAM = 'method'
CASCADE_HIERARCHY_PARAM = 'cascadeHierarchy'
CASCADE_MAPPINGS_PARAM = 'cascadeMappings'
EXCLUDE_MAP_TYPES_PARAM = 'excludeMapTypes'
EXCLUDE_FUZZY_SEARCH_PARAM = 'excludeFuzzy'
EXCLUDE_WILDCARD_SEARCH_PARAM = 'excludeWildcard'
SEARCH_MAP_CODES_PARAM = 'searchMapCodes'
MAP_TYPES_PARAM = 'mapTypes'
CASCADE_LEVELS_PARAM = 'cascadeLevels'
RETURN_MAP_TYPES = 'returnMapTypes'
EQUIVALENCY_MAP_TYPES = 'equivalencyMapType'
CASCADE_DIRECTION_PARAM = 'reverse'
OMIT_IF_EXISTS_IN = 'omitIfExistsIn'
INCLUDE_SELF = 'includeSelf'
FACET_SIZE = 20
ALL = '*'
CANONICAL_URL_REQUEST_PARAM = 'canonicalUrl'
SAME_STANDARD_CHECKSUM_ERROR = 'No changes detected. Standard checksum is same as last version.'
