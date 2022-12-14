from db import db
from sqlalchemy import PrimaryKeyConstraint

class SensorModel(db.Model):
    __tablename__ = 'sensor'
    
    id = db.Column(db.Integer)
    measurement_type = db.Column(db.String(19),nullable=False)
    timestamp = db.Column(db.DateTime())
    value = db.Column(db.Float(precision=3),nullable=False)
    
    __table_args__ = (
        PrimaryKeyConstraint(id, timestamp),
        {},
    )
    
    