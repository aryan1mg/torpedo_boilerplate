from torpedo import Host, CONFIG, register_cache

from .cache_host import cache_host
from .routes import blueprints

config = CONFIG.config


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
    # config object will be dict representation of config.json read by the utility function in torpedo
    config = CONFIG.config

    # set up cache for service. there is also a support for multiple caches. To add support for multiple cache, pass
    # an argument multiple=True in below method. If argument is passed then config.json has to be updated as well.
    # for single cache support config file will have following key values:
    # "REDIS_HOST": "localhost"
    # "REDIS_PORT": 6379
    # for a multi cache support system, config have the following key values:
    # "REDIS_CACHE_HOSTS": {
    #     "GLOBAL": {
    #         "HOST": "localhost",
    #         "PORT": 6379
    #     },
    #     "Service1": {
    #         "HOST": "localhost",
    #         "PORT": 6379
    #     },
    #     "Service2": {
    #         "HOST": "localhost",
    #         "PORT": 6379
    #     }
    # }
    init_cache()

    Host._name = config['NAME']
    Host._host = config['HOST']
    Host._port = config['PORT']
    Host._workers = config.get('WORKERS', 2)  # number of workers to run, keep <= num of cores
    # debug would be true for local, make sure it is false on staging and production. This flag also defines logging
    # in torpedo. If this flag is false then logs are written in files by overriding the default logging settings.
    Host._debug = config.get('DEBUG', True)

    # register combined blueprint group here. these blueprints are defined in the routes directory and has to be
    # collected in init file otherwise route will end up with 404 error.
    Host._handlers = blueprints

    # setup db config using tortoise orm configuration. If service doesn't need database setup then remove the
    # below line
    Host._db_config = get_db_config()

    Host.run()
