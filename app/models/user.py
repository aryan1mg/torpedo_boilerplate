from collections import defaultdict

from tortoise import fields

from .mixins import ModelUtilMixin
from .abc import AbstractBaseUser


class User(AbstractBaseUser, ModelUtilMixin):
    force_password_reset = fields.BooleanField(null=True)

    @property
    def external_id(self):
        return ''

    class Meta:
        table = 'users'

    async def to_dict(self, filter_keys=None, get_related=True, related_fields=None):
        result = await super().to_dict(filter_keys, get_related, related_fields)
        if result:
            prop_dict = {}
            if result.get('roles') and isinstance(result['roles'], list):
                role_dict = defaultdict(list)
                for role in result['roles']:
                    role_dict[role.get('app', "")].append(role.get('role'))
                result['roles'] = dict(role_dict)
            if result.get('properties') and isinstance(result['properties'], list):
                prop_dict = {}
                for prop in result['properties']:
                    prop_dict[prop.get('name', "")] = prop.get('value')
                result['properties'] = dict(prop_dict)
            else:
                result['properties'] = {}
            if result.get('properties_new') and isinstance(result['properties_new'], list):
                for prop in result['properties_new']:
                    prop_dict[prop.get('name', "")] = prop.get('value')
                result['properties'] = dict(prop_dict)
        result.pop('properties_new', None)
        return result
