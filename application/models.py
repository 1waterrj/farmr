from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.dialects import postgresql

db = SQLAlchemy()
migrate = Migrate()


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())


class Input(db.Model):
    __tablename__ = "inputs"
    __table_args__ = (
        db.ForeignKeyConstraint(
            ['name'],
            ['zone_id'],
        ),
    )
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    zone_id = db.Column(db.Integer, db.ForeignKey('Zone.id'))
    fingerprint = db.Column(postgresql.UUID(as_uuid=True), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())


class Zone(db.Model):
    __tablename__ = "zones"
    __table_args__ = (
        db.ForeignKeyConstraint(
            ['name'],
            ['group_id'],
        ),
    )
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    group_id = db.Column(db.Integer, db.ForeignKey('Group.id'))
    created_at = db.Column(db.DateTime, default=db.func.now())


class Location(db.Model):
    __tablename__ = "locations"
    __table_args__ = (
        db.ForgeignKeyConstraint(
            ['name'],
            ['user_id'],
        ),
    )
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    zipcode = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=db.func.now())


class Group(db.Model):
    __tablename__ = "groups"
    __table_args__ = (
        db.ForeignKeyConstraint(
            ['name'],
            ['location_id'],
        ),
    )
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    location_id = db.Column(db.Integer, db.ForeignKey('Location.id'))
    created_at = db.Column(db.DateTime, default=db.func.now())


class MqttEvents(db.Model):
    __tablename__ = "mqtt_events"
    id = db.Column(db.Integer, primary_key=True)
    input_id = db.Column(db.Integer, db.ForeignKey('Input.id'))
    data_load = db.Column(db.JSON, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
