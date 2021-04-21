from sanic import Blueprint
from torpedo import send_response

from ..managers import UserManager

basic_with_db_cache = Blueprint('basic_with_db_cache', version=4)


@basic_with_db_cache.route("/users", methods=['GET'])
async def get_user(request):
    """
    this is an example of route which interacts with the database connection created in same service.
    We are connecting with identity db on staging for this service. See model implementation at models -> user.py.
    It also uses caching support defined in caches -> user.py.
    """
    payload = request.args
    _response = await UserManager.get_user(payload)
    return send_response(_response)
