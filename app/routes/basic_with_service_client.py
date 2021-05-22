from sanic import Blueprint
from torpedo import Request, send_response

from ..managers import AddressManager

with_service_client = Blueprint("basic_with_service_client", version=4)


@with_service_client.route("/address_by_id", methods=["GET"])
async def address_by_id(request: Request):
    """
    this is an example of route which interacts with another microservice returning
    result in v4 format. This api will call location service to get address by id.
    See implementation in service_clients -> location_service -> address.py
    """
    payload = request.request_params()
    result = await AddressManager.get_address_by_id(payload)
    return send_response(result)
