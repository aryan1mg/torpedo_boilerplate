from sanic import Blueprint

from torpedo import send_response
from ..managers import UserManager


test_blueprint = Blueprint('test', version='v4')


@test_blueprint.route("/users", methods=['GET'])
async def list_all(request):
    payload = request.args
    _response = await UserManager.get_users(payload)
    return send_response(_response)


@test_blueprint.route("/user", methods=['POST'])
async def add_user(request):
    payload = request.json
    _response = await UserManager.get_users(payload)
    return send_response(_response)

