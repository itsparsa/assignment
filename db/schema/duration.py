from enum import Enum

class DurationType(str, Enum):
    one_hour_after = "1h"
    five_min_after = "5min"