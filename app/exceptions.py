from sanic.exceptions import SanicException


class BadRequestException(SanicException):
    """
        error will be dict like object
        error = {'message': 'an error occured', 'errors': [{'message': 'user not found'}]}
    """

    def __init__(self, error):
        self._error = error

    @property
    def error(self):
        return self._error
