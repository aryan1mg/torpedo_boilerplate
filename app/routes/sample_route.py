from sanic import Blueprint, response
from sanic.response import json

from ..models.user import Users


sample_blueprint = Blueprint('sample_blueprint', version=4)


@sample_blueprint.route('/sample_url', methods=['GET'])
async def by_email_id(request):
    return json({'message': 'hello world!'})


@sample_blueprint.route("/")
async def list_all(request):
    users = await Users.all()
    return response.json({"users": [str(user) for user in users]})


@sample_blueprint.route("/user")
async def add_user(request):
    user = await Users.create(name="New User")
    return response.json({"user": str(user)})
