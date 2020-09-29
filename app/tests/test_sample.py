from app import create_app
import json
import unittest
from sanic.response import json, text
from sanic import Blueprint
from app import create_app
from app.utils import json_file_to_dict


def test_bp():
    bp = Blueprint("test_text")

    @bp.route("/")
    def handler(request):
        return text("Hello")

    app = create_app(config=json_file_to_dict('./config.json'))
    app.blueprint(bp)
    request, response = app.test_client.get("/")
    assert app.is_request_stream is False

    assert response.text == "Hello"


async def test_fixture_test_client_post():
    """
    POST request
    """
    app = create_app(config=json_file_to_dict('./config.json'))
    resp = await app.test_client.post('/test_post')
    assert resp.status == 200
    resp_json = await resp.json()
    assert resp_json == {"POST": True}


if __name__ == '__main__':
    unittest.main()
