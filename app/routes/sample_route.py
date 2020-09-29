from sanic import Blueprint, response
from sanic.response import json

from ..managers import UserManager


sample_blueprint = Blueprint('sample_blueprint', version=4)


@sample_blueprint.route('/hello', methods=['GET'])
async def hello(request):
    return json({'message': 'hello world!'})


@sample_blueprint.route("/users")
async def list_all(request):
    _response = await UserManager.get_users()
    return response.json(_response)


@sample_blueprint.route("/user")
async def add_user(request):
    payload = request.json
    _response = await UserManager.create_user(payload)
    return response.json(_response)
