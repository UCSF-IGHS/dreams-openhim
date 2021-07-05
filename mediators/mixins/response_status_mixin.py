

class ResponseStatusMixin:
    SUCCESS_CREATED = 'SUCCESS_CREATED'
    SUCCESS_DUPLICATE_IGNORED = 'SUCCESS_DUPLICATE_IGNORED'
    SUCCESS_UPDATED = 'SUCCESS_UPDATED'
    SUCCESS_DELETED = 'SUCCESS_DELETED'
    ERROR_SERIALIZATION_ERROR = 'ERROR_SERIALIZATION_ERROR'
    ERROR_VALIDATION_ERROR = 'ERROR_VALIDATION_ERROR'
    ERROR_VALIDATION_DATE_IN_FUTURE = 'ERROR_VALIDATION_DATE_IN_FUTURE'
    ERROR_VALIDATION_CLIENT_NOT_FOUND = 'ERROR_VALIDATION_CLIENT_NOT_FOUND'
    ERROR_VALIDATION_IP_NOT_FOUND = 'ERROR_VALIDATION_IP_NOT_FOUND'
    ERROR_VALIDATION_INTERVENTION_TYPE_NOT_FOUND = 'ERROR_VALIDATION_INTERVENTION_TYPE_NOT_FOUND'
    ERROR_VALIDATION_HTS_RESULT_NOT_FOUND = 'ERROR_VALIDATION_HTS_RESULT_NOT_FOUND'
    ERROR_VALIDATION_EXTERNAL_ORGANISATION_NOT_FOUND = 'ERROR_VALIDATION_EXTERNAL_ORGANISATION_NOT_FOUND'
    ERROR_VALIDATION_PREGNANCY_TEST_RESULT_NOT_FOUND = 'ERROR_VALIDATION_PREGNANCY_TEST_RESULT_NOT_FOUND'
    ERROR_VALIDATION_USER_NOT_FOUND = 'ERROR_VALIDATION_USER_NOT_FOUND'
    ERROR_ACCESS_DENIED = 'ERROR_ACCESS_DENIED'

    MEDIATOR_RESPONSE_PROCESSING = 'Processing'
    MEDIATOR_RESPONSE_FAILED = 'Failed'
    MEDIATOR_RESPONSE_COMPLETED = 'Completed'
    MEDIATOR_RESPONSE_SUCCESSFUL = 'Successful'
    MEDIATOR_RESPONSE_COMPLETED_WITH_ERRORS = 'Completed with error(s)'