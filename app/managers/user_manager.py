from torpedo.exceptions import BadRequestException
from torpedo.wrappers import ORMWrapper

from ..caches import UserCache
from ..models import User


class UserManager:
    @classmethod
    async def get_user(cls, payload):
        username = payload.get("username")

        user = await UserCache.get(username)
        if user:
            return user
        else:
            user = await ORMWrapper.get_by_filters(User, {"username": username})
            if not user:
                raise BadRequestException("No users found.")
            user = await user[0].to_dict()

            # set value to cache
            await UserCache.set_user(username, user)
            return user
