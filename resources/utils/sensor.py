from datetime import datetime

from sqlalchemy.orm import Session
from sqlalchemy import func

from db.schema.sensor import Sensor
from db.schema.sensor_type import SensorType
from db.models.sensor import TemperatureSensor,HumiditySensor
from db.db_setup import Base
from db.schema.duration import DurationType
from db.schema.sensor_type import SensorType
from .sensor_table import sensor_type_table
from .duration import duration_timedelta

def get_all_sensors(db: Session):
    sensors = []
    tmperature_sensors = db.query(TemperatureSensor).all() or []
    humidity_sensors = db.query(HumiditySensor).all() or []
    sensors = tmperature_sensors+humidity_sensors
    return sensors

def post_sensor(sensor:Sensor,db: Session, sensor_type:SensorType):

    db_sensor = sensor_type_table(sensor_type)( id = sensor.id ,type = sensor.type.lower() ,timestamp = sensor.timestamp,value = sensor.value)
    db.add(db_sensor)
    db.commit()
    db.refresh(db_sensor)
    return db_sensor

def get_sensor_by_type_time(  sensor_type:SensorType,id:int,type:str,duration:DurationType,startdatetime:datetime,
                            db:Session): 

    duration = duration_timedelta(duration)
    base = sensor_type_table(sensor_type)
    sensors = db\
                .query( func.min(base.value).label("min"),
                        func.max(base.value).label("max"),
                        func.avg(base.value).label("mean"),
                        func.array_agg(base.timestamp).label("timestamps") )\
                .where( base.id == id ,
                        base.type == type.lower(),
                        base.timestamp >= startdatetime,
                        base.timestamp <= startdatetime+duration)\
                .all()[0]           

    return {"MIN_VALUE" : sensors[0],
            "MAX_VALUE" : sensors[1],
            "MEAN_VALUE" : sensors[2],
            "timestamps" : sensors[3]}                        
    
