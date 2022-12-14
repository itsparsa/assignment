from typing import Optional,List

import fastapi
from fastapi import Depends
from sqlalchemy.orm import Session
from datetime import datetime

from db.schema.sensor import Sensor
from db.db_setup import get_db
from .utils.sensor import get_all_sensors,post_sensor,get_sensor_by_type_time
from db.schema.sensor_type import SensorType
from db.schema.duration import DurationType

router = fastapi.APIRouter()

@router.get("/sensor")
async def get_sensor(db: Session = Depends(get_db)):
    return get_all_sensors(db=db )
   

@router.post("/sensor/{sensor_type}")
async def post_sensor( sensor_type:SensorType ,sensor:Sensor,db: Session = Depends(get_db)):
    return post_sensor (sensor=sensor,db=db,sensor_type=sensor_type)
  

@router.get("/sensor/{sensor_type}/{id}/{type}/{duration}/{startdatetime}")
# /sensor/temperature/2/Celcuis/5min/2022-12-11T18:52:27.969550
async def get_sensor_by_type_timestamps(  sensor_type:SensorType,
                    id:int,
                    type:str,
                    duration:DurationType,
                    startdatetime:datetime,
                    db:Session = Depends(get_db)):
                    # pass
    return get_sensor_by_type_time(sensor_type=sensor_type,id=id, type=type,duration=duration,startdatetime=startdatetime,db=db) 