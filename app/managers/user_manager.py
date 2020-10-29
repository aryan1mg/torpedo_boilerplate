from ..models import User

from torpedo.wrappers import ORMWrapper
from torpedo.exceptions import BadRequestException


class UserManager:

    @classmethod
    async def get_users(cls, payload):
        username = payload.get('username')
        user = await ORMWrapper.get_by_filters(User, {'username': username})
        if not user:
            raise BadRequestException('No users found.')
        user = await user[0].to_dict()
        return user
