from tortoise import Model, fields
from .mixins import ModelUtilMixin


class User(Model, ModelUtilMixin):
    id = fields.BigIntField(pk=True)
    username = fields.TextField()
    name = fields.TextField()
    created = fields.BigIntField()
    updated = fields.BigIntField()

    class Meta:
        table = 'user'

