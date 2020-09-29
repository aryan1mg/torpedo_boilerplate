from sanic import Sanic
from tortoise.contrib.sanic import register_tortoise

from .routes import sample_blueprint
from .models.user import User


def create_app(config):
    app = Sanic('push_service')
    app.config.fromkeys(config)

    register_blueprints(app)

    register_db(app)

    return app


def register_db(app):
    register_tortoise(
        app,
        db_url="sqlite://:memory:",
        modules={"models": ["app.models.user"]},
        generate_schemas=True
    )


def register_blueprints(app):
    app.blueprint(sample_blueprint)
