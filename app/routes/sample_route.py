import asyncio
from sanic import Blueprint


from torpedo import send_response, Request, Task, TaskExecutor
from torpedo.exceptions import BadRequestException, HTTPInterServiceRequestException
from ..service_clients import AddressClient


sample_blueprint = Blueprint('sample_blueprint', version='v4')


@sample_blueprint.route('/hello/<name:string>', methods=['GET'], name='hello')
async def hello(request: Request, name):
    payload = request.request_params()
    await asyncio.sleep(10)
    return send_response({'message': 'hello world!'})


@sample_blueprint.route('/address_by_id', methods=['GET'])
async def address_by_id(request: Request):
    payload = request.request_params()

    tasks = [Task(AddressClient.by_id(payload), result_key='address_result')]
    task_result = await TaskExecutor(tasks=tasks).submit()
    address_result = task_result[0].result
    if isinstance(address_result, Exception):
        raise BadRequestException('No results found.')
    else:
        result = address_result
        return send_response(result)
