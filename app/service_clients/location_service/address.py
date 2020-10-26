from torpedo import CONFIG, BaseApiRequest

from ..base_api_client import APIClient


class AddressClient(APIClient):
    _config = CONFIG.config
    _identity_config = _config['LOCATION_SERVICE']
    _host = _identity_config['HOST']

    @classmethod
    async def by_id(cls, payload):
        path = '/v4/address'
        result = await cls.get(path, query_params=payload)
        return result.data
