from sanic import Blueprint

from .sample_route import sample_blueprint
from .sample_route2 import test_blueprint

group = Blueprint.group(sample_blueprint, test_blueprint)

group.middleware()


