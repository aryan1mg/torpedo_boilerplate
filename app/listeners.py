from .constants import ListenerEventTypes


async def notify_server_started_after_five_seconds(app, loop):
    pass


listeners = [(notify_server_started_after_five_seconds, ListenerEventTypes.AFTER_SERVER_START.value)]
