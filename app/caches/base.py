import json

from ..cache_host import cache_host
from torpedo import CONFIG


class Base:
    config = CONFIG.config
    _service_prefix = config['NAME']
    _key_prefix = 'base'
    _delimiter = ':'

    @classmethod
    def prefixed_key(cls, key: str):
        """
        :param key:
        :return:
        """
        return cls._service_prefix + cls._delimiter + cls._key_prefix + cls._delimiter + key

    @classmethod
    async def set(cls, key, value, expire=0):
        """
        :param key:
        :param value:
        :param expire:
        :return:
        """
        await cache_host['global'].set_key(key=cls.prefixed_key(key), value=json.dumps(value), expire=expire)

    @classmethod
    async def get(cls, key):
        """
        :param key:
        :return:
        """
        result = await cache_host['global'].get_key(key=cls.prefixed_key(key))
        if result:
            result = json.loads(result)
        return result
