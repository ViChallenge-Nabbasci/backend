from location import Category
from pydantic import BaseModel, Field

class User(BaseModel):
    username: str
    email: str
    age: int
    preferences: list[Category]

users = [
    User(username="flanny", email="a@b.org",age=21, preferences=[Category.MUSEUM, Category.RESTORATION]),
    User(username="chrg127", email="c@d.org",age=22, preferences=[Category.RESTORATION, Category.TREKKING]),
    User(username="federaffo00", email="e@f.org",age=23, preferences=[Category.MUSEUM]),
]

current_user = User(username="flanny", email="a@b.org",age=24, preferences=[Category.MUSEUM, Category.RESTORATION])
