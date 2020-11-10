from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.dialects import postgresql
import uuid

db = SQLAlchemy()
migrate = Migrate()


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, unique=True, nullable=False)

class Input(db.Model):
    __tablename__ = "inputs"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique)
class MqttEvents(db.Model):
    __tablename__ = "mqtt_events"
    id = db.Column(db.Integer, primary_key=True)

    fingerprint = db.Column(postgresql.UUID(as_uuid=True), nullable=False)
