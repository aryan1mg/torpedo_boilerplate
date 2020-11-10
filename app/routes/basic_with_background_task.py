import asyncio

from sanic import Blueprint

from torpedo import send_response


basic_with_background_task = Blueprint('test', version='v4')


@basic_with_background_task.route("/long_task", methods=['GET'])
async def get_user(request):
    request.app.add_task(long_runnning_task(10))
    return send_response({'message': 'long running task created.'})


async def long_runnning_task(sec):
    await asyncio.sleep(sec)
    print("task completed after sleeping for {} seconds".format(sec))
