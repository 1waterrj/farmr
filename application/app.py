from flask import Flask
from application.apis import api
from flask_restx import Api, Namespace, Resource, fields


def create_app(config_name):

    app = Flask(__name__)

    config_module = f"application.config.{config_name.capitalize()}Config"

    app.config.from_object(config_module)

    from application.models import db, migrate

    db.init_app(app)
    migrate.init_app(app, db)

    api.init_app(app)
    print(api, "this is the app")
    cat = api.model(
        "Cat",
        {
            "id": fields.String(required=True, description="The cat identifier"),
            "name": fields.String(required=True, description="The cat name"),
        },
    )

    CATS = [
        {"id": "felix", "name": "Felix"},
        {"id": "tom", "name": "Tom"},
    ]

    print(api, "this is the farmr file")

    @api.route("/")
    class CatList(Resource):
        @api.doc("list_cats")
        @api.marshal_list_with(cat)
        def get(self):
            print(CATS)
            """List all cats"""
            return CATS

    @api.route("/<id>")
    @api.param("id", "The cat identifier")
    @api.response(404, "Cat not found")
    class Cat(Resource):
        @api.doc("get_cat")
        @api.marshal_with(cat)
        def get(self, id):
            """Fetch a cat given its identifier"""
            for cat in CATS:
                if cat["id"] == id:
                    return cat
            api.abort(404)

    @api.route("/hello")
    class HelloWorld(Resource):
        def get(self):
            return {"hello": "world"}

    return app
