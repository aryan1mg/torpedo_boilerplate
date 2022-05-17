from collections import defaultdict

from tortoise_wrapper.db import CustomTextField, ModelUtilMixin
from tortoise import Model, fields

from .abc import AbstractBaseUser


class User(AbstractBaseUser, ModelUtilMixin):
    force_password_reset = fields.BooleanField(null=True)

    @property
    def external_id(self):
        return ""

    class Meta:
        table = "users"

    async def to_dict(self, filter_keys=None, get_related=True, related_fields=None):
        result = await super().to_dict(filter_keys, get_related, related_fields)
        if result:
            prop_dict = {}
            if result.get("roles") and isinstance(result["roles"], list):
                role_dict = defaultdict(list)
                for role in result["roles"]:
                    role_dict[role.get("app", "")].append(role.get("role"))
                result["roles"] = dict(role_dict)
            if result.get("properties") and isinstance(result["properties"], list):
                prop_dict = {}
                for prop in result["properties"]:
                    prop_dict[prop.get("name", "")] = prop.get("value")
                result["properties"] = dict(prop_dict)
            else:
                result["properties"] = {}
            if result.get("properties_new") and isinstance(
                result["properties_new"], list
            ):
                for prop in result["properties_new"]:
                    prop_dict[prop.get("name", "")] = prop.get("value")
                result["properties"] = dict(prop_dict)
        result.pop("properties_new", None)
        return result


class UserProperty(Model, ModelUtilMixin):
    """
    UserProperty Model Points to the "profile" table in the Database
    """

    # TODO: Note: Here "id" field does not exists in the DB,  we are pointing it to the username column of the db.
    #  There is no use in App for the "id" field,  This is added just for the convention of the Tortoise ORM.
    #  In Future when "id" field is added to the DB, we need to the update the "id" field here.

    json_keys_for_name = ["plan_info"]
    serializable_keys = {"username", "name", "value"}

    # id = fields.TextField(source_field='username', null=True, pk=True)
    username = fields.ForeignKeyField(
        "identity.User",
        related_name="properties",
        on_delete=fields.CASCADE,
        source_field="username",
        pk=True,
    )
    name = CustomTextField(index=True)
    value = CustomTextField(index=True)

    class Meta:
        table = "profile"


class UserPropertyNew(Model, ModelUtilMixin):
    """
    UserProperty Model Points to the "profile" table in the Database
    """

    json_keys_for_name = ["plan_info"]
    serializable_keys = {"username", "name", "value"}

    id = fields.BigIntField(pk=True)
    username = fields.ForeignKeyField(
        "identity.User",
        related_name="properties_new",
        on_delete=fields.CASCADE,
        source_field="username",
    )
    name = CustomTextField(index=True)
    value = CustomTextField(index=True)
    created = fields.BigIntField(null=True)
    updated = fields.BigIntField(null=True)

    class Meta:
        table = "profile_new"
