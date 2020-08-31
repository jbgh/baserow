from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND


ERROR_FIELD_DOES_NOT_EXIST = (
    'ERROR_FIELD_DOES_NOT_EXIST',
    HTTP_404_NOT_FOUND,
    'The requested field does not exist.'
)
ERROR_CANNOT_DELETE_PRIMARY_FIELD = 'ERROR_CANNOT_DELETE_PRIMARY_FIELD'
ERROR_CANNOT_CHANGE_FIELD_TYPE = 'ERROR_CANNOT_CHANGE_FIELD_TYPE'
ERROR_LINK_ROW_TABLE_NOT_PROVIDED = (
    'ERROR_LINK_ROW_TABLE_NOT_PROVIDED',
    HTTP_400_BAD_REQUEST,
    'The `link_row_table` must be provided.'
)
ERROR_LINK_ROW_TABLE_NOT_IN_SAME_DATABASE = 'ERROR_LINK_ROW_TABLE_NOT_IN_SAME_DATABASE'
