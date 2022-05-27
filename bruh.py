"""
@app.get("/items/{item_id}")
def read_root(item_id: str, request: Request):
    client_host = request.client.host
    return {"client_host": client_host, "item_id": item_id}
"""

"""
@app.get("/getUsers")
async def get_users():
    return users

@app.post("/addUser", status_code=201)
async def add_user(newUser: User):
    users.append(newUser)
    return users
    """