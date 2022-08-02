from sanic.log import logger
from sanic import Blueprint
from torpedo import send_response

from ..managers import UserManager1
#
basic_with_db_cache = Blueprint("basic_with_db_cache", version=4)


@basic_with_db_cache.route("/users/<name:str>", methods=["GET"])
async def get_user(request, name: str):
    payload = request.request_params()
    logger.info(payload,"lets print")
    _response = await UserManager1.get_user(payload)
    return send_response(_response)

@basic_with_db_cache.route("/users/<stu_id:int>", methods=["GET"])
async def get_user(request, stu_id: int):
    payload = request.request_params()
    logger.info(payload,"lets print")
    _response = await UserManager1.get_user(payload)
    return send_response(_response)

@basic_with_db_cache.route("/users", methods=["GET"])
async def get_all(request):
    _response = await UserManager1.get_all()
    return send_response(_response)

@basic_with_db_cache.route("/users", methods=["POST"])
async def create_user(request):
    payload = request.custom_json()
    _response = await UserManager1.create_user(payload)
    return send_response(_response)

@basic_with_db_cache.route("/users/<stu_id:int>", methods=["PUT"])
async def update(request,stu_id:int):
    params = request.request_params()
    payload = request.custom_json()
    logger.info("payload, {}, {}".format(payload,"hi,there!"))
    logger.info("params, {}".format(params))
    _response = await UserManager1.update(params,payload)
    return send_response(_response) 

@basic_with_db_cache.route("/users/<name:str>", methods=["DELETE"])
async def delete(request,name:str):
    payload =request.request_params()
    r_w = request.custom_json()
    _response = await UserManager1.delete(payload,r_w)
    return send_response(_response)