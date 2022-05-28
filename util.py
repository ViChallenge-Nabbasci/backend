import datetime
import enum
import uvicorn
from datetime import time
from pydantic import BaseModel, Field
import json
from fastapi import FastAPI, Request
from typing import List

def to_mins(time):
    return time.hour * 60 + time.minute

def is_open(open_times, close_times, now = datetime.datetime.now().time()):
    return any([ [ot, ct] if now > ot and now < ct else None
                 for ot, ct in zip(open_times, close_times) ])

def get_user(email):
    r = [ u for u in users if u.email == email ]
    return r[0] if len(r) == 0 else None

def tests():
    assert is_open([ time( 8, 0), time(15, 0) ],
                   [ time(12, 0), time(18, 0) ],
                   time(17, 0)) != None

tests()
