from typing import Optional, Union, Any

import warnings
import ujson

from tortoise.exceptions import BaseORMException
from tortoise.fields import TextField, Field


class ArrayField(Field, list, tuple, set):

    def to_db_value(self, value: Optional[Union[list, tuple, set]], instance) -> Optional[str]:
        if instance and not instance._saved_in_db:
            return value
        if value is None:
            return None
        if isinstance(value, self.field_type):
            return ujson.dumps(value).translate({ord("["): "{", ord("]"): "}"})
        else:
            raise BaseORMException("Non Iterable value provided for ArrayField ")

    def to_python_value(self, value: Optional[Union[str, list]]) -> Optional[list]:
        if value is None or isinstance(value, list):
            return value
        else:
            return ujson.loads(value)


class TextArrayField(ArrayField):
    pass


class IntArrayField(ArrayField):
    pass


class CustomTextField(TextField):

    __slots__ = ()
    indexable = True

    def __init__(
        self, pk: bool = False, **kwargs: Any
    ) -> None:
        if pk:
            warnings.warn(
                "TextField as a PrimaryKey is Deprecated, use CharField instead",
                DeprecationWarning,
                stacklevel=2,
            )
        super(TextField, self).__init__(pk=pk, **kwargs)


class CITextField(CustomTextField):
    pass
