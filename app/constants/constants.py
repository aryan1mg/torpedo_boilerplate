import enum


class HTTPStatusCodes(enum.Enum):
    SUCCESS = 200
    BAD_REQUEST = 400
    NOT_FOUND = 404
    FORBIDDEN = 403
    UNAUTHORIZED = 401
    MOVED_TEMPORARILY = 302
    INTERNAL_SERVER_ERROR = 500


class Constant(enum.Enum):
    DEFAULT_LIMIT = 100
    DEFAULT_OFFSET = 0
