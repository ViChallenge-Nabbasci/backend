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
import sys
import location
import itinerary
import users

app = FastAPI()






# add like

class LikeRequest(BaseModel):
    email: str
    id: int

@app.post("/sendLike")
async def get_user(req: LikeRequest):
    email = req.email
    id = req.id
    e = [ u for u in users.users if u.email == email ]
    n = [ s for s in location.locations if s.id == id ]

    if len(e) == 0 or len(n) == 0:
        return {"response": "bad request"}

    if email not in location.likes:
        location.likes[email] = [id]
    elif id not in location.likes[email]:
        location.likes[email].append(id)

    location.save_likes()
    return {"response": "like processed"}


@app.get("/ping")
async def test_sku():
    return {"message:": "pong"}

@app.post("/getItinerary")
async def get_itinerary(req: itinerary.Preferences):
    return itinerary.make_itinerary(req)



if __name__ == "__main__":
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    location.load_likes()
    location.load_locations()
    uvicorn.run("test:app", host=local_ip, port=8080, log_level="debug")
