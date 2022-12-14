from typing import Optional
from datetime import datetime
from fastapi import Query

from pydantic import BaseModel

class Sensor(BaseModel):
    id : int
    type : str 
    timestamp :Optional[datetime] 
    value : float