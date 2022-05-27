from audioop import add
from unicodedata import category

from matplotlib.style import use
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
from location import *
from itinerary import *

app = FastAPI()

class User(BaseModel):    
    username: str
    email: str
    preferences: list[Category]

users = [
    User(username="flanny", email="a@b.org", preferences=[Category.MUSEUM, Category.RESTORATION]),
    User(username="chrg127", email="c@d.org", preferences=[Category.RESTORATION, Category.TREKKING]),
    User(username="federaffo00", email="e@f.org", preferences=[Category.MUSEUM]),
]

current_user = User(username="flanny", email="a@b.org", preferences=[Category.MUSEUM, Category.RESTORATION])




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



@app.post("/getItinerary")
async def get_itinerary(req: Preferences):
    return make_itinerary(req)



if __name__ == "__main__":
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    load_likes()
    load_locations()
    uvicorn.run("test:app", host=local_ip, port=8080, log_level="info")
