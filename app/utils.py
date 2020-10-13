import time
import uuid
import ujson

from newrelic.agent import record_exception
from sanic.response import json
from sanic.log import error_logger
from sanic.exceptions import SanicException, Unauthorized, NotFound, Forbidden, ServerError, \
    ServiceUnavailable, PayloadTooLarge, MethodNotSupported

from .constants import HTTPStatusCodes


def json_file_to_dict(_file: str) -> dict:
    """
    convert json file data to dict

    :param str _file: file location including name

    :rtype: dict
    :return: converted json to dict
    """
    config = None
    try:
        with open(_file) as config_file:
            config = ujson.load(config_file)
    except (ValueError, Exception, FileNotFoundError) as exception:
        print(exception)

    return config


def get_config():
    config = json_file_to_dict('./config.json')
    return config


def get_current_time():
    return int(time.time())


def get_uuid_token():
    return str(uuid.uuid4())


def send_response(data):
    """
    Success response data
    :param data: success response
    :return: success json response
    """
    result = dict({
        'data': data,
        'is_success': True
    })
    result['status_code'] = 200
    result['is_success'] = True

    return json(result)


def get_error_body_response(error, status_code, meta=None):
    """
    :param error: error message
    :param status_code: error status code
    :param meta: meta info for error
    :return: error json response
    """

    error_result = dict({'is_success': False, 'status_code': status_code, 'error': error})

    if meta:
        error_result['meta'] = meta

    return json(error_result, status=status_code)


class ExceptionHandler:
    """
    Exception handler class for sanic routes
    """
    bad_request_exceptions = [SanicException, NotFound, MethodNotSupported, PayloadTooLarge]
    unauthorized_exceptions = [Unauthorized, Forbidden]
    internal_server_exceptions = [Exception, ServerError, ServiceUnavailable]

    @classmethod
    async def internal_server_error_handler(cls, request, exception):
        record_exception()
        error_logger.exception(exception)
        response = get_error_body_response({'message': "Something went wrong"},
                                           HTTPStatusCodes.INTERNAL_SERVER_ERROR.value)
        return response

    @classmethod
    async def bad_request_error_handler(cls, request, exception):
        error_logger.info(exception)
        response = get_error_body_response({'message': exception.args[0]},
                                           HTTPStatusCodes.BAD_REQUEST.value)
        return response

    @classmethod
    async def unauthorized_request_error_handler(cls, request, exception):
        error_logger.info(exception)
        response = get_error_body_response({'message': exception.args[0]},
                                           HTTPStatusCodes.UNAUTHORIZED.value)
        return response


def register_exception_handler(app):
    """
    :param app: Sanic app instance
    :return:
    """

    for _error_handler in ExceptionHandler.bad_request_exceptions:
        app.error_handler.add(_error_handler, ExceptionHandler.bad_request_error_handler)

    for _error_handler in ExceptionHandler.unauthorized_exceptions:
        app.error_handler.add(_error_handler, ExceptionHandler.unauthorized_request_error_handler)

    for _error_handler in ExceptionHandler.internal_server_exceptions:
        app.error_handler.add(_error_handler, ExceptionHandler.internal_server_error_handler)
