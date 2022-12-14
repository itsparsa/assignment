import os
import random
from datetime import datetime,timedelta
from random import randint,choice,random

from sqlalchemy.orm import Session
from faker import Faker
from tqdm import tqdm

from resources.utils.sensor_table import sensor_type_table
from db.schema.sensor_type import SensorType
from typing import List


def create_fake_data(number:int,sensor_type:SensorType,id_range:List[int] ,value_range:List[float],messurement_types:List[str],datetime_duration:List[datetime],db:Session):
    fake = Faker()
    for _ in tqdm(range(number)):
        id = randint(*id_range)
        type = choice(messurement_types)
        timestamp = datetime_duration[0]
        timestamp += timedelta(seconds=randint(0,2*60*60))
        value = random()*abs(value_range[1]-value_range[0]) + min(*value_range)
        base = sensor_type_table(sensor_type)
        if base:
            if db.query(base).where(base.id == id , base.timestamp == timestamp).first():
                continue
            else: 
                db_sensor=base( id = id ,type = type.lower() ,timestamp = timestamp,value = value)
                db.add(db_sensor)
                db.commit()
                db.refresh(db_sensor)

    






