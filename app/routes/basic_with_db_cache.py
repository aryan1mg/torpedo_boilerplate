from sanic import Blueprint

from torpedo import send_response
from ..managers import UserManager


basic_with_db_cache = Blueprint('test', version='v4')


@basic_with_db_cache.route("/users", methods=['GET'])
async def get_user(request):
    payload = request.args
    _response = await UserManager.get_user(payload)
    return send_response(_response)
