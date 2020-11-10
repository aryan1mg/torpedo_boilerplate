from sanic import Blueprint
from torpedo import send_response, Request

from ..managers import AddressManager


with_service_client = Blueprint('sample_blueprint', version='v4')


@with_service_client.route('/address_by_id', methods=['GET'])
async def address_by_id(request: Request):
    payload = request.request_params()
    result = await AddressManager.get_address_by_id(payload)
    return send_response(result)
