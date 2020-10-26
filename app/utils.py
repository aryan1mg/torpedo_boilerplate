import time
import uuid
import ujson


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

