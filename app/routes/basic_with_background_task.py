import asyncio

from sanic import Blueprint

from torpedo import send_response


basic_with_background_task = Blueprint('basic_with_background', version=4)


@basic_with_background_task.route("/long_task", methods=['GET'])
async def get_user(request):
    """
    this is an example of route which uses creates a long running background task.
    Tasks can be grouped in a single file at root folder in tasks.py but for this example its defined below.
    """
    request.app.add_task(long_runnning_task(5))
    return send_response({'message': 'long running task created.'})


async def long_runnning_task(sec):
    """
    to mock the long running task, we are using asyncio sleep of 10 seconds to delay the execution
    """
    await asyncio.sleep(sec)
    print("task completed after sleeping for {} seconds".format(sec))
