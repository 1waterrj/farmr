from flask_restx import Api

from application.apis.farmr1 import api as ns1

print("this is the init file")
api = Api(
    title="farmr",
    version="1.0",
    description="api for managing all resources related to farmr",
    # All API metadatas
)

api.add_namespace(ns1)
