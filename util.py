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

class Category(enum.Enum):
    RESTORATION = "restoration"
    THEATER = "theater"
    TREKKING = "trekking"
    BIKE = "bike"
    MUSEUM = "museum"

class Location(BaseModel):
    id: int
    name: str
    opening_times: list[datetime.time]
    closing_times: list[datetime.time]
    phone: str
    price: int
    durata: int
    address: str
    notes: str
    category: Category
    outside: bool

json_stuff = """
[
  {
    "id": 0,
    "name": "Villaggio Preistorico del Monte Corgnon",
    "opening_times": [
        "00:10:00", "00:10:00", "00:10:00", "00:10:00", "00:10:00", "00:10:00", "00:10:00"
    ],
    "closing_times": [
        "00:19:00", "00:19:00", "00:19:00", "00:19:00", "00:19:00", "00:19:00", "00:19:00"
    ],
    "phone": "0424407264",
    "price": 4,
    "durata": 1,
    "address": "",
    "notes": "",
    "category": "museum",
    "outside": true
  },
  {
    "id": 1,
    "name": "museum Civico Giuseppe Zannato",
    "opening_times": [
        "00:00:00", "00:00:00", "00:00:00", "00:00:00", "00:00:00", "00:15:00", "00:15:00"
    ],
    "closing_times": [
        "00:00:00", "00:00:00", "00:00:00", "00:00:00", "00:00:00", "00:18:00", "00:18:00"
    ],
    "phone": "0444492565",
    "price": 3,
    "durata": 1,
    "address": "",
    "notes": "",
    "category": "museum",
    "outside": true
  },
  {
    "id": 2,
    "name": "museum Archeologico dell’Alto Vicentino",
    "opening_times": [
        "00:00:00", "00:00:00", "00:00:00", "00:00:00", "00:00:00", "00:00:00", "00:15:00"
    ],
    "closing_times": [
        "00:00:00", "00:00:00", "00:00:00", "00:00:00", "00:00:00", "00:00:00", "00:18:00"
    ],
    "phone": "0445649570",
    "price": 0,
    "durata": 1,
    "address": "",
    "notes": "",
    "category": "museum",
    "outside": false
  },
  {
    "id": 3,
    "name": "museum Archeologico dei Sette Comuni",
    "opening_times": [
        "00:10:00", "00:10:00", "00:10:00", "00:10:00", "00:10:00", "00:10:00", "00:10:00"
    ],
    "closing_times": [
        "00:16:00", "00:16:00", "00:16:00", "00:16:00", "00:16:00", "00:16:00", "00:16:00"
    ],
    "phone": 3516889103,
    "price": 8,
    "durata": 2,
    "address": "",
    "notes": "",
    "category": "museum",
    "outside": false
  },
  {
    "id": 4,
    "name": "Castello Inferiore e museum dei Costumi della partita a scacchi",
    "opening_times": [
        "00:09:00", "00:09:00", "00:09:00", "00:09:00", "00:09:00", "00:09:00", "00:09:00"
    ],
    "closing_times": [
        "00:18:00", "00:18:00", "00:18:00", "00:18:00", "00:18:00", "00:18:00", "00:18:00"
    ],
    "phone": "042472127",
    "price": 8,
    "durata": 2,
    "address": "",
    "notes": "",
    "category": "museum",
    "outside": false
  },
  {
    "id": 5,
    "name": "Covolo del Butistone e museum",
    "opening_times": [
        "00:09:00", "00:09:00", "00:09:00", "00:09:00", "00:09:00", "00:09:00", "00:09:00"
    ],
    "closing_times": [
        "00:18:00", "00:18:00", "00:18:00", "00:18:00", "00:18:00", "00:18:00", "00:18:00"
    ],
    "phone": 3388308984,
    "price": 5,
    "durata": 2,
    "address": "",
    "notes": "",
    "category": "museum",
    "outside": false
  },
  {
    "id": 6,
    "name": "Teatro Olimpico",
    "opening_times": [
        "00:00:00", "00:09:00", "00:09:00", "00:09:00", "00:09:00", "00:09:00", "00:09:00"
    ],
    "closing_times": [
        "00:00:00", "00:17:00", "00:17:00", "00:17:00", "00:17:00", "00:17:00", "00:17:00"
    ],
    "phone": "0444320854",
    "price": 11,
    "durata": 2,
    "address": "",
    "notes": "",
    "category": "theater",
    "outside": false
  },
  {
    "id": 7,
    "name": "Ristorante al pastello",
    "opening_times": [
        "00:00:00", "00:00:00", "00:00:00", "00:00:00", "00:00:00", "00:00:00", "00:00:00"
    ],
    "closing_times": [
        "00:00:00", "00:00:00", "00:00:00", "00:00:00", "00:00:00", "00:24:00", "00:24:00"
    ],
    "phone": "0444323721",
    "price": 10,
    "durata": 2,
    "address": "",
    "notes": "",
    "category": "restoration",
    "outside": false
  }
]"""

def tests():
    assert is_open([ time( 8, 0), time(15, 0) ],
                   [ time(12, 0), time(18, 0) ],
                   time(17, 0)) != None
    locs = [ Location(**x) for x in json.loads(json_stuff) ]
    print([ loc.json() for loc in locs ])

tests()
