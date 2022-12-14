from typing import Optional,List

from fastapi import FastAPI

from db.schema.sensor import Sensor
from resources.sensor import router
from db.db_setup import engine,Base

Base.metadata.create_all(bind = engine)

app = FastAPI()
app.include_router(router)
