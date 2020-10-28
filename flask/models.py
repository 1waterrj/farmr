from sqlalchemy import Column, Integer, String, ForeignKey, Date, JSON, UniqueConstraint
from sqlalchemy.orm import relationship
from flask_appbuilder import Model

class mqtt_events(Model):
    id = Column(Integer, primary_key=True)
    fingerprint = Column(String(50), ForeignKey(inputs.fingerprint), nullable=False)
    data = Column(JSON, nullable=False)
    created_at = Column(Date, nullable=False)

class inputs(Model):
    id = Column(Integer, primary_key=True)
    fingerprint = Column(String(50), nullable=False, unique=True)
    input_type = Column(Integer, ForeignKey(input_types.id))
    created_at = Column(Date, nullable=False)
    node = Column(Integer, ForeignKey(nodes.id), nullable=False)

class input_types(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    created_at = Column(Date, nullable=False)

class node(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    account = Column(Integer, ForeignKey(accounts.id))
    created_at = Column(Date)

class accounts(Model):
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    created_at = Column(Date)

class chron_triggers(Model):
    id = Column(Integer, primary_key=True)

class event_triggers(Model):
    id = Column(Integer, primary_key=True)

class locations(Model):
    __table_args__= (
        UniqueConstraint('name','account', name='unique_account_location')
    )
    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    zip_code = Column(Integer)
    account = Column(Integer, ForeignKey(accounts.id), nullable=False)
    created_at = Column(Date)



class groups(Model):
     __table_args__= (
        UniqueConstraint('name','location', name='unique_location_group')
    )
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    location = Column(Integer, ForeignKey(locations.id), nullable=False)
    created_at = Column(Date)

