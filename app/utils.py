import ujson
import time
import uuid


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


def get_current_time():
    return int(time.time())


def get_uuid_token():
    return str(uuid.uuid4())
