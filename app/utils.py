import time
import ujson
import uuid

from .constants import HTTPStatusCodes

from newrelic.agent import record_exception
from sanic.response import json
from sanic.log import error_logger
from sanic.exceptions import SanicException, Unauthorized


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
    except Exception as e:
        print(e)

    return config


def get_config():
    config = json_file_to_dict('./config.json')
    return config


def get_current_time():
    return int(time.time())


def get_uuid_token():
    return str(uuid.uuid4())


def send_response(data):
    result = dict({
        'data': data,
        'is_success': True
    })
    result['status_code'] = 200
    result['is_success'] = True

    return json(result)


def get_error_body_response(error, status_code, meta=None):

    error_result = dict({'is_success': False, 'status_code': status_code, 'error': error})

    if meta:
        error_result['meta'] = meta

    return json(error_result, status=status_code)


async def exception_handler(request, exception):
    record_exception()
    if isinstance(exception, SanicException):
        response = get_error_body_response({'message': exception.args[0]}, HTTPStatusCodes.BAD_REQUEST.value)
    elif isinstance(exception, Unauthorized):
        response = get_error_body_response({'message': exception.args[0]}, HTTPStatusCodes.UNAUTHORIZED.value)
    else:
        response = get_error_body_response({'message': "Something went wrong"},
                                           HTTPStatusCodes.INTERNAL_SERVER_ERROR.value)
        error_logger.exception(exception)
    return response


def register_exception_handler(app):
    for _error_handler in SanicException.__subclasses__():
        app.error_handler.add(_error_handler, exception_handler)
    app.error_handler.add(Exception, exception_handler)
