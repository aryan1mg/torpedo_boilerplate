from ..models import User
from ..db import ORM


class UserManager:

    @classmethod
    async def get_users(cls, payload):
        username = payload.get('username')
        user = await ORM.get_by_filters(User, {'username': username})
        if not user:
            raise TypeError('No users found.')
        user = await user[0].to_dict()
        return user

