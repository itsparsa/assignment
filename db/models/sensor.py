from sqlalchemy import Column,String,Integer,Float,DateTime,PrimaryKeyConstraint

from..db_setup import Base



class TemperatureSensor(Base):
    __tablename__ = "temperatureSensor"

    id = Column(Integer,nullable=False)
    type = Column(String(19),nullable=False)
    timestamp = Column(DateTime())
    value = Column(Float(precision=3),nullable=False)
    
    __table_args__ = (
        PrimaryKeyConstraint(id, timestamp),
        {},
    )

class HumiditySensor(Base):
    __tablename__ = "humiditySensor"
    
    id = Column(Integer,nullable=False)
    type = Column(String(19),nullable=False)
    timestamp = Column(DateTime())
    value = Column(Float(precision=3),nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint(id, timestamp),
        {},
    )   







# class Sensor(Base):
#     __tablename__ = "sensor"

#     id = Column(Integer)
#     type = Column(String(19),nullable=False)
#     timestamp = Column(DateTime())
#     m_type = Column(String(19),nullable=False)
#     # value = Column(Float(precision=3),nullable=False)

#     __table_args__ = (
#         PrimaryKeyConstraint(id, timestamp),
#         {},
#     )

#     __mapper_args__ = {
#         "polymorphic_on": "type",
#         "polymorphic_identity": "sensor",
#     }
    
# class TemperatureSensor(Sensor):
#     temp_value = Column(Float(precision=3),nullable=False)
#     __mapper_args__ = {
#         "polymorphic_identity": "temperatureSensor",
#     }
    
# class HumiditySensor(Sensor):
#     humidity_value = Column(Float(precision=4),nullable=False)
#     __mapper_args__ = {
#         "polymorphic_identity": "humiditysensor",
#     }
    




