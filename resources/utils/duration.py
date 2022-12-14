from datetime import timedelta

from db.schema.duration import DurationType

def duration_timedelta(duration:DurationType)->timedelta:
    if duration is DurationType.five_min_after:
        return timedelta(minutes=5)
    elif duration is DurationType.one_hour_after:
        return timedelta(hour=1) 
    return None  