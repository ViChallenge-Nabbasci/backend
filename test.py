from audioop import add
from unicodedata import category
import uvicorn
from fastapi import FastAPI, Request
from pydantic import BaseModel, Field
import socket
import datetime
import enum
import pandas as pd

app = FastAPI()




class Category(enum.Enum):
    RESTORATION = enum.auto
    TREKKING = enum.auto
    BIKE = enum.auto
    MUSEUM = enum.auto









class User(BaseModel):    
    username: str
    email: str
    preferences: list[Category]

users = [
    User(username="flanny", email="a@b.org", preferences=[Category.BIKE, Category.RESTORATION]),
    User(username="chrg127", email="c@d.org", preferences=[Category.RESTORATION, Category.TREKKING]),
    User(username="federaffo00", email="e@f.org", preferences=[Category.MUSEUM]),
]

class Location(BaseModel):
    id: int
    name: str
    address: str
    # lat: float
    # long: float
    opening_times: list[datetime.time]
    closing_times: list[datetime.time]
    categories: list[Category]

locations = [
    Location(id=0, name="struttura", address="da qualche parte", opening_times=[], closing_times=[], categories=[Category.MUSEUM])
]

likes = {
    
}


def _find_next_id():
    return max(Location.id for us in locations) + 1

def loadCsv(path):
    df = pd.read_csv(path)
    print(df.to_json())
loadCsv('data.csv')







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
    else:
        likes[email].append(id)

    return {"response": "like added"}









hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
if __name__ == "__main__":
    uvicorn.run("test:app", host=local_ip, port=8080, log_level="info")
