from db.models.sensor import TemperatureSensor,HumiditySensor
from db.db_setup import Base
from db.schema.sensor_type import SensorType

def sensor_type_table(sensor_type:SensorType)->Base:
    if sensor_type is SensorType.temperature:
        return TemperatureSensor
    elif sensor_type is SensorType.humidity:
        return HumiditySensor 
    return None  