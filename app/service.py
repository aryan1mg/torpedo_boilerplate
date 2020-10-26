from torpedo import Host, CONFIG, register_cache

from sanic import Blueprint
from .cache_host import cache_host
from .utils import get_config
from .routes import group

config = get_config()


def init_cache(multiple=False):
    """
    :return:
    """
    if multiple:
        cache_host.update(register_cache(multiple=True))
    else:
        cache_host['global'] = register_cache()


def get_db_config():
    db_config = {
        "connections": {
            "default": {
                "engine": "tortoise.backends.asyncpg",
                "credentials": {
                    "host": config['POSTGRES_HOST'],
                    "port": config['POSTGRES_PORT'],
                    "user": config['POSTGRES_USER'],
                    "password": config['POSTGRES_PASS'],
                    "database": config['POSTGRES_DB']
                },
            },
        },
        "apps": {
            "identity": {
                "models": ['app.models.user'],
                "default_connection": "default"
            },
        },
    }
    return db_config


if __name__ == '__main__':
    config = CONFIG.config

    init_cache(multiple=True)

    Host._name = config['NAME']
    Host._host = config['HOST']
    Host._port = config['PORT']
    Host._workers = config.get('WORKERS', 2)  # number of workers to run, keep <= num of cores
    # debug would be true for local, make sure it is false on staging and production
    Host._debug = config.get('DEBUG', True)

    # register combined blueprint group here
    handlers = []
    for _group in group.blueprints:
        for sub_group in _group.routes:
            handlers.append((_group, sub_group))

    Host._handlers = handlers

    # setup db config
    Host._db_config = get_db_config()

    Host.run()
