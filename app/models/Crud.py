from collections import defaultdict
from tortoise_wrapper.db import CITextField, CustomTextField, ModelUtilMixin
from tortoise import Model, fields


class Crud(Model, ModelUtilMixin):
    """
    Abstract Class for User and Guest User Models
    Provides all the fields for User Tables

    """

    serializable_keys = {
        "name",
        "stu_id",
        "school"
    }

    name = fields.CharField(max_length=50, null=False)
    stu_id = fields.BigIntField(pk=True)
    school = fields.CharField(max_length=50, null=False) 

    class Meta:
        table = "student"

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