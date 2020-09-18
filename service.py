from app.utils import json_file_to_dict

from app import create_app


config = json_file_to_dict('./config.json')


if __name__ == '__main__':
    host = config['HOST']
    port = config['PORT']
    debug = config.get('DEBUG', False)
    num_workers = config.get('WORKERS', 2)
    create_app(config=config).run(
        host=host,
        port=port,
        debug=debug,
        workers=num_workers
    )
