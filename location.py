from pydantic import BaseModel, Field
import sys
import datetime
import enum
import json

class Category(enum.Enum):
    RESTORATION = "restoration"
    THEATER     = "theater"
    TREKKING    = "trekking"
    BIKE        = "bike"
    MUSEUM      = "museum"
    SQUARE      = "square"
    PARK        = "park"
    CHURCH      = "church"

def all_categories():
    return [
        Category.RESTORATION,
        Category.THEATER,
        Category.TREKKING,
        Category.BIKE,
        Category.MUSEUM,
        Category.SQUARE,
        Category.PARK,
        Category.CHURCH
    ]

def find_next_id():
    return 0 if len(locations) == 0 else max(us.id for us in locations) + 1

class Location(BaseModel):
    id: int = Field(default_factory=find_next_id)
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
    with_pets: bool
    ages: list[int]
    img: str
    location:str

locations = {}
likes = {}

def save_likes():
    global likes
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
        except Exception as e:
            print(e)
            sys.exit(0)


def all_likes():
    return sum([ len(likes[key]) for key in likes ])

def all_likes_for(id):
    return sum([ 1 if id in likes[key] else 0 for key in likes ])

