from datetime import datetime,timedelta

from fastapi import Depends
from sqlalchemy.orm import Session

from db.db_setup import get_db,SessionLocal
from db.create_fake_data import create_fake_data
from db.schema.sensor_type import SensorType


if __name__ == '__main__':
        create_fake_data(   number = 50,
                            sensor_type=SensorType.temperature,
                            id_range=[1,4],value_range=[0,10],
                            messurement_types=["Celcuis","Fahrenheit"],
                            datetime_duration=[datetime.now()-timedelta(hours=2),datetime.now()],
                            db = SessionLocal())