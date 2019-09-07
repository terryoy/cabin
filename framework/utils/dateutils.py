# -*- coding: utf-8 -*-
import time
from datetime import datetime

def to_timestamp(dt):
    return int(time.mktime(dt.timetuple())*1000)

def from_timestamp(ts):
    return datetime.fromtimestamp(ts / 1000.0)

def to_time_number(timeField):
    """从datetime.time到数字表达的时间值(HHMMSS)"""
    return int(timeField.strftime('%H%M%S'))

def from_time_number(timeNumber):
    return datetime.strptime(str(timeNumber), '%H%M%S').time()
