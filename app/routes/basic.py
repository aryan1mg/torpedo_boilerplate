from sanic import Blueprint
from torpedo import send_response, Request


basic = Blueprint('sample_blueprint', version='v4')


@basic.route('/hello/<name:string>', methods=['GET'], name='hello')
async def hello(request: Request, name):
    """ A very basic route created using sanic blueprint. """
    payload = request.request_params()
    return send_response({'message': 'hello {}!'.format(name)})

