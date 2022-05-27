import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field
import socket

app = FastAPI()

def _find_next_id():
    return max(User.id for us in users) + 1

class User(BaseModel):
    id: int = Field(default_factory=_find_next_id, alias="id")
    username: str

users = [
    User(id=1, username="flanny"),
    User(id=2, username="chrg127"),
    User(id=3, username="federaffo00"),
]

@app.get("/getUsers")
async def get_countries():
    return users

@app.post("/addUser", status_code=201)
async def add_country(newUser: User):
    users.append(newUser)
    return users



hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
if __name__ == "__main__":
    uvicorn.run("test:app", host=local_ip, port=8080, log_level="info")