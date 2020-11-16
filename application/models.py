from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.dialects import postgresql
from sqlalchemy.schema import ForeignKeyConstraint
from sqlalchemy.orm import relationship

db = SQLAlchemy()
migrate = Migrate()


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())


class Location(db.Model):
    __tablename__ = "locations"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    zipcode = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=db.func.now())
    groups = relationship("Group", backref="locations")
    __table_args__ = (
        db.UniqueConstraint(
            'name',
            'user_id',
            name='_location_user_uc'
        ),
    )


class Group(db.Model):
    __tablename__ = "groups"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    location_id = db.Column(db.Integer, db.ForeignKey(Location.id))
    created_at = db.Column(db.DateTime, default=db.func.now())
    __table_args__ = (db.UniqueConstraint('name', 'location_id', name='_group_location_uc'),)


class Zone(db.Model):
    __tablename__ = "zones"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    group_id = db.Column(db.Integer, db.ForeignKey(Group.id))
    created_at = db.Column(db.DateTime, default=db.func.now())
    __table_args__ = (
        db.UniqueConstraint(
            'name',
            'group_id',
            name='_zone_group_uc'
        ),
    )


class InputType(db.Model):
    __tablename__ = "input_types"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())


class Input(db.Model):
    __tablename__ = "inputs"
    id = db.Column(db.Integer, primary_key=True)
    input_type_id = db.Column(db.Integer, db.ForeignKey(InputType.id), nullable=False)
    name = db.Column(db.String)
    zone_id = db.Column(db.Integer, db.ForeignKey(Zone.id))
    fingerprint = db.Column(postgresql.UUID(as_uuid=True), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
    __table_args__ = (
        db.UniqueConstraint(
            'name',
            'zone_id',
            name='_input_zone_uc'
        ),
    )


class MqttEvents(db.Model):
    __tablename__ = "mqtt_events"
    id = db.Column(db.Integer, primary_key=True)
    input_id = db.Column(db.Integer, db.ForeignKey(Input.id))
    data_load = db.Column(db.JSON, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())


class TimedEvents(db.Model):
    __tablename__ = "timed_events"
    id = db.Column(db.Integer, primary_key=True)
    input_id = db.Column(db.Integer, db.ForeignKey(Input.id), nullable=False)
    cron_job = db.Column(db.String, nullable=False)
    message = db.Column(db.String)


class TriggeredEvents(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    input_id = db.Column(db.Integer, db.ForeignKey(Input.id), nullable=False)
    output_id = db.Column(db.Integer, db.ForeignKey(Input.id), nullable=False)
