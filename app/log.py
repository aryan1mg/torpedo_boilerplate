
LOGGING_CONFIG_DEFAULTS = dict(
    version=1,
    disable_existing_loggers=False,
    loggers={
        "sanic.root": {
            "level": "INFO",
            "handlers": ["console"]
        },
        "sanic.error": {
            "level": "DEBUG",
            "handlers": ["error_console"],
            "qualname": "sanic.error",
        },
        "sanic.access": {
            "level": "INFO",
            "handlers": ["access_console", "error_console"],
            "qualname": "sanic.access",
        },
    },
    handlers={
        "console": {
            "class": "logging.FileHandler",
            "formatter": "generic",
            "filename": "logs/sanic_service.log",
        },
        "access_console": {
            "class": "logging.FileHandler",
            "formatter": "access",
            "filename": "logs/sanic_service.log"
        },
        "error_console": {
            "class": "logging.FileHandler",
            "formatter": "generic",
            "filename": "logs/sanic_exceptions.log"
        },
    },
    formatters={
        "generic": {
            "format": "%(asctime)s [%(process)d] [%(levelname)s] %(message)s",
            "datefmt": "[%Y-%m-%d %H:%M:%S %z]",
            "class": "logging.Formatter",
        },
        "access": {
            "format": "%(asctime)s - (%(name)s)[%(levelname)s] - [%(host)s]: "
            + "%(request)s %(message)s %(status)d %(byte)d",
            "datefmt": "[%Y-%m-%d %H:%M:%S %z]",
            "class": "logging.Formatter",
        },
    },
)
