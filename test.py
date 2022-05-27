from audioop import add
from unicodedata import category
import uvicorn
from fastapi import FastAPI, Request
from pydantic import BaseModel, Field
import socket
import datetime
import enum
import json
import pickle
import pandas as pd
import sys

app = FastAPI()




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









class User(BaseModel):    
    username: str
    email: str
    preferences: list[Category]

users = [
    User(username="flanny", email="a@b.org", preferences=[Category.MUSEUM, Category.RESTORATION]),
    User(username="chrg127", email="c@d.org", preferences=[Category.RESTORATION, Category.TREKKING]),
    User(username="federaffo00", email="e@f.org", preferences=[Category.MUSEUM]),
]




def _find_next_id():
    return max(Location.id for us in locations) + 1




# add like

class LikeRequest(BaseModel):
    email: str
    id: int

@app.post("/sendLike")
async def get_user(req: LikeRequest):
    email = req.email
    id = req.id
    e = [ u for u in users if u.email == email ]
    n = [ s for s in locations if s.id == id ]

    if len(e) == 0 or len(n) == 0:
        return {"response": "bad request"}

    if email not in likes:
        likes[email] = [id]
    elif id not in likes[email]:
        likes[email].append(id)

    save_likes()
    return {"response": "like processed"}



locations = {}
likes = {}

def save_likes():
    with open('likes.json', 'w') as fp:
        json.dump(likes, fp)

def load_likes():
    global likes
    with open('likes.json') as d:
        try:
            likes = json.load(d)
        except:
            likes = {}

def load_locations():
    global locations
    with open('locations.json') as d:
        try:
            locations = [ Location(**x) for x in json.load(d) ]
        except:
            print('json load fail')
            sys.exit(0)







if __name__ == "__main__":
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    load_likes()
    load_locations()
    uvicorn.run("test:app", host=local_ip, port=8080, log_level="info")
    
