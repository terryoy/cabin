import time
from datetime import datetime

def to_timestamp(dt):
    return int(time.mktime(dt.timetuple())*1000)

def from_timestamp(ts):
    return datetime.fromtimestamp(ts / 1000.0)
