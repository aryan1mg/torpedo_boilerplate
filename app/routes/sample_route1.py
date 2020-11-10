from sanic import Blueprint
from torpedo import send_response, Request

from ..managers import AddressManager


sample_blueprint = Blueprint('sample_blueprint', version='v4')


@sample_blueprint.route('/hello/<name:string>', methods=['GET'], name='hello')
async def hello(request: Request, name):
    payload = request.request_params()
    return send_response({'message': 'hello {}!'.format(name)})


@sample_blueprint.route('/address_by_id', methods=['GET'])
async def address_by_id(request: Request):
    payload = request.request_params()
    result = await AddressManager.get_address_by_id(payload)
    return send_response(result)
