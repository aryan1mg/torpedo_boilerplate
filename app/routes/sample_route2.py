from sanic import Blueprint

from torpedo import send_response
from ..managers import UserManager


test_blueprint = Blueprint('test', version='v4')


@test_blueprint.route("/users", methods=['GET'])
async def get_user(request):
    payload = request.args
    _response = await UserManager.get_user(payload)
    return send_response(_response)
