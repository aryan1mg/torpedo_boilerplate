from .cache_host import cache_host
from .log import LOGGING_CONFIG_DEFAULTS
from .utils import get_config, register_exception_handler
from .routes import group

from sanic import Sanic
from tortoise.contrib.sanic import register_tortoise
from vessel import RedisCache

config = get_config()


def register_app_blueprints(_app):
    _app.blueprint(group)


def init_cache(_config):
    cache_host['global'] = RedisCache(_config['REDIS_HOST'], _config['REDIS_PORT'])


def register_db(_app):
    register_tortoise(
        _app,
        config={
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
        },
        generate_schemas=False
    )


if __name__ == '__main__':

    # read config from file
    host = config['HOST']
    port = config['PORT']
    # debug would be true for local and staging development, make sure it is false on production
    debug = config.get('DEBUG', False)
    num_workers = config.get('WORKERS', 2)  # num worker to run, should be <= num cores
    log_config = False if debug else LOGGING_CONFIG_DEFAULTS  # custom logging setting

    app = Sanic(config['NAME'], log_config=log_config)

    # register application dependencies

    # register blueprints
    register_app_blueprints(app)

    # setup db connection
    register_db(app)

    # setup exception handlers
    register_exception_handler(app)

    app.run(
        host=host,
        port=port,
        debug=debug,
        workers=num_workers
    )
