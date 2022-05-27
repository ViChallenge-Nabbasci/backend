from location import Category

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
