from torpedo import Host, CONFIG

from .routes import blueprints


if __name__ == '__main__':
    # config object will be dict representation of config.json read by the utility function in torpedo
    config = CONFIG.config

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

    Host.run()
