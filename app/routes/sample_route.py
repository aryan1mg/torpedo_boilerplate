from sanic import Blueprint

from ..utils import send_response


sample_blueprint = Blueprint('sample_blueprint', version=4)


@sample_blueprint.route('/hello', methods=['GET'])
async def hello(request):
    return send_response({'message': 'hello world!'})
