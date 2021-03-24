from sanic import Blueprint
from torpedo import send_response, Request


basic = Blueprint('basic_blueprint', version=4)


@basic.route('/hello/<name:string>', methods=['GET'], name='hello')
async def hello(request: Request, name):
    """
    A very basic route created using sanic blueprint.
    """
    return send_response({'message': 'hello {}!'.format(name)})

