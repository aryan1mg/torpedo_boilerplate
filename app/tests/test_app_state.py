from sanic import Sanic
import pytest
from torpedo.common_utils import CONFIG, json_file_to_dict
from torpedo.exceptions import JsonDecodeException
from sanic.request import Request
from torpedo import Host
from app.routes import group

config = CONFIG.config
config_template = json_file_to_dict('./config_template.json')


def request_params(self):
    """
    function to get all query params and match_info params as query params
    :return: a dictionary of query params
    """
    params = {}
    for key, value in self.args.items():
        modified_key = key.replace('[]', '')
        if '[]' in key:
            params[modified_key] = value
        else:
            params[key] = value[0]

    for key, value in self.match_info.items():
        params[key] = value
    return params


def custom_json(self, *args, **kwargs):
    """Return BODY as JSON."""
    data = self.json
    if data is None:
        raise JsonDecodeException('Invalid Request')
    return data


@pytest.yield_fixture
def app():
    setattr(Request, 'request_params', request_params)
    setattr(Request, 'custom_json', custom_json)
    _app = Sanic(config.get('NAME'))
    _app.update_config(config)
    _app.blueprint(group)
    yield _app


@pytest.fixture
def sanic_client(loop, app, sanic_client):
    return loop.run_until_complete(sanic_client(app))


async def test_fixture_test_client_get(sanic_client):
    """
    GET request
    """
    resp = await sanic_client.get('/v4/hello/ajay')
    assert resp.status == 200
    resp_json = await resp.json()
    assert resp_json == {'data': {'message': 'hello world!'}, 'is_success': True, 'status_code': 200}

