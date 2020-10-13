from tortoise import Tortoise

from ..constants import Constant


class ORMWrapper:
    @classmethod
    async def get_by_filters(cls, model, filters, order_by=None, limit=Constant.DEFAULT_LIMIT.value,
                             offset=Constant.DEFAULT_OFFSET.value):
        """
        :param model: database model class
        :param filters: where conditions for filter
        :param order_by: for ordering on queryset
        :param limit: limit queryset result
        :param offset: offset queryset results
        :return: list of model objects returned by the where clause
        """
        queryset = model.filter(**filters)
        if order_by:
            queryset = queryset.order_by(order_by)
        if limit:
            queryset = queryset.limit(limit)

        if offset:
            queryset = queryset.offset(offset)

        return await queryset

    @classmethod
    async def update_with_filters(cls, row, model, payload, where_clause=None, update_fields=None):
        """
        :param row: database model instance which needs to be updated
        :param model: database model class on which filters and update will be applied. Please see diff between the two.
        :param payload: values which will be updated in the database.
        :param where_clause: conditions on which update will work.
        :param update_fields: fields to update in case of model object update
        :return: None. update doesn;t return any values
        """
        if where_clause:
            await model.filter(**where_clause).update(**payload)
        else:
            for key, value in payload.items():
                setattr(row, key, value)
            await row.save(update_fields=update_fields)
        return None

    @classmethod
    async def create(cls, model, payload):
        """
        :param model: db model
        :param payload: create payload
        :return: model instance
        """
        row = await model.create(**payload)
        return row

    @classmethod
    async def get_or_create_object(cls, model, payload, defaults=None):
        """
        :param model: database model class which needs to be get or created
        :param payload: values on which get or create will happen
        :param defaults: values on which will used to create the data which we do not want to include in filtering
        :return: model object and created - true/false
        """
        defaults = defaults or {}
        row, created = await model.get_or_create(defaults=defaults, **payload)
        return row, created

    @classmethod
    async def delete_with_filters(cls, row, model, where_clause):
        """
        :param row: model object
        :param model: db model
        :param where_clause: where conditional
        :return: None
        """
        if where_clause:
            await model.filter(**where_clause).delete()
        else:
            await row.delete()

    @classmethod
    async def raw_sql(cls, query):
        """
        :param query: contains raw sql query which have to be executed
        :return:
        """
        conn = Tortoise.get_connection('device')
        result = await conn.execute_query(query)
        return result
