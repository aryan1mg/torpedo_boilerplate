from ..models import User
from ..utils import get_current_time, get_uuid_token


class UserManager:

    @classmethod
    async def create_user(cls, payload):
        name = payload.get('name')

        _payload = {
            'name': name,
            'username': get_uuid_token(),
            'created': get_current_time(),
            'updated': get_current_time()
        }
        user = await User.create(**_payload)
        return {'data': await user.to_dict()}

    @classmethod
    async def get_users(cls):
        users = await User.all()
        users = [await x.to_dict() for x in users]
        return {'data': users}

