from flask import Flask
from flask_restx import Api


def create_app(config_name):

    app = Flask(__name__)
    api = Api()
    api.init_app(app)

    config_module = f"application.config.{config_name.capitalize()}Config"

    app.config.from_object(config_module)

    from application.models import db, migrate

    db.init_app(app)
    migrate.init_app(app, db)

    @app.route("/")
    def hello_world():
        return "Hello, World!"

    return app
