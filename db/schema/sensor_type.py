from enum import Enum

class SensorType(str, Enum):
    temperature = "temperature"
    humidity = "humidity"