from signal import pause
from sanic.log import logger
from torpedo.exceptions import BadRequestException
from tortoise_wrapper.wrappers import ORMWrapper

from ..caches import UserCache
from ..models import User,Crud

class UserManager1:
    @classmethod
    async def get_all(cls):
        user = await ORMWrapper.raw_sql('Select * from student')
        return user

    @classmethod
    async def get_user(cls, payload):
        user = await ORMWrapper.get_by_filters(Crud,payload)
        if user:
            for i in range(len(user)):
                user[i] = await user[i].to_dict()
            return user 
        else:
            return {"message":"No such User Exists"}

    @classmethod
    async def create_user(cls,payload):

        if await Crud.filter(stu_id=payload.get("stu_id")):
            return {"message":"User Exists, Choose a different ID"}
        else:
            new_user = await ORMWrapper.create(Crud, payload)
            new_user = await new_user.to_dict()
            return new_user

    @classmethod
    async def update(cls,params,payload):
        #name = str(payload)
        user = await ORMWrapper.get_by_filters(Crud,params)
        logger.info("user: {}".format(user))
        if user:
            user = user[0]
            updated_user = await ORMWrapper.update_with_filters(user,Crud,payload,None,["name","school"])
            logger.info("heyo, {}".format(updated_user))
            logger.info("hello")
            return {"message": "User Updated"}
        else:
            return {"message":"No such User Exists"}
    
    @classmethod
    async def delete(cls,payload,row):
        # name = str(payload)
        user = await ORMWrapper.get_by_filters(Crud,payload)
        if user:
            await ORMWrapper.delete_with_filters(row,Crud,payload)
            return {"message":"user deleted"}
        else:
            return {"message":"No such User Exists"}