from torpedo import TaskExecutor, Task
from torpedo.exceptions import BadRequestException

from ..service_clients import AddressClient


class AddressManager:

    @classmethod
    async def get_address_by_id(cls, payload):
        tasks = [Task(AddressClient.by_id(payload), result_key='address_result')]
        task_result = await TaskExecutor(tasks=tasks).submit()
        address_result = task_result[0].result
        if isinstance(address_result, Exception):
            raise BadRequestException('No results found.')

        return address_result
