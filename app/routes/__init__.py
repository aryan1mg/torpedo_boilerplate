from .basic import basic
from .basic_with_db_cache import basic_with_db_cache
from .basic_with_service_client import with_service_client
from .basic_with_background_task import basic_with_background_task

blueprints = [basic, basic_with_db_cache, with_service_client, basic_with_background_task]
