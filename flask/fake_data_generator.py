import random
from datetime import datetime,timedelta
from random import randint,choice,random

from faker import Faker
from tqdm import tqdm
from flask import g
from sqlalchemy import func

from models.sensors import SensorModel
from db import db
from app import create_app
from flask_sqlalchemy import SQLAlchemy


def create_fake_data(number,id_range,value_range,measurement_types,datetime_duration,base,db):
    fake = Faker()
    for _ in tqdm(range(number)):
        id = randint(*id_range)
        type = choice(measurement_types)
        timestamp = datetime_duration[0]
        timestamp += timedelta(seconds=randint(0,2*60*60))
        value = random()*abs(value_range[1]-value_range[0]) + min(*value_range)
        if db:
            if db.session.query(base).where(base.id == id , base.timestamp == timestamp).first():
                continue
            else: 
                db_sensor=base( id = id ,measurement_type = type.lower() ,timestamp = timestamp,value = value)
                db.session.add(db_sensor)
                db.session.commit()
                db.session.refresh(db_sensor)

if __name__ == '__main__':
        app = create_app()
        with app.app_context():
            create_fake_data(   number = 50,
                                id_range=[1,4],value_range=[0,10],
                                measurement_types=["Celcuis","Fahrenheit"],
                                datetime_duration=[datetime.now()-timedelta(hours=2),datetime.now()],
                                base = SensorModel,
                                db = db)