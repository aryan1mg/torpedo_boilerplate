from torpedo import CONFIG

from ..base_api_client import APIClient


class AddressClient(APIClient):
    _config = CONFIG.config
    address_config = _config["LOCATION_SERVICE"]
    _host = address_config["HOST"]

    @classmethod
    async def by_id(cls, payload):
        path = "/v4/address"
        result = await cls.get(path, query_params=payload)
        return result.data
