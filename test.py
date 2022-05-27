import uvicorn
from fastapi import FastAPI, Request
from pydantic import BaseModel, Field
import socket

app = FastAPI()

def _find_next_id():
    return max(User.id for us in users) + 1

class User(BaseModel):
    # id: int = Field(default_factory=_find_next_id, alias="id")
    username: str
    email: str

users = [
    User(username="flanny", email="a@b.org"),
    User(username="chrg127", email="c@d.org"),
    User(username="federaffo00", email="e@f.org"),
]

@app.get("/getUsers")
async def get_users():
    return users

@app.post("/addUser", status_code=201)
async def add_user(newUser: User):
    users.append(newUser)
    return users

class GetUserRequest(BaseModel):
    email: str

@app.post("/getUser")
async def get_user(req: GetUserRequest):
    r = [ u for u in users if u.email == req.email ]
    return {"response":"bad id"} if len(r) == 0 else r[0]

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
if __name__ == "__main__":
    uvicorn.run("test:app", host=local_ip, port=8080, log_level="info")
