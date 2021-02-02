import asyncio

from .constants import ListenerEventTypes


async def notify_server_started_after_five_seconds(app, loop):
    await asyncio.sleep(5)
    print(app.name)


listeners = [(notify_server_started_after_five_seconds, ListenerEventTypes.AFTER_SERVER_START.value)]
