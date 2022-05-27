from datetime import datetime
from unicodedata import category
from test import Category, locations,current_user
from pydantic import BaseModel, Field
from location import *

class Preferences(BaseModel):
    byCar: bool
    lunch: bool
    dinner: bool
    onlyFree: bool
    withPet:bool
    data: datetime.date
    categories: list[Category]

class Itinerary(BaseModel):
    morning: Location
    lunch: Location
    afternoon: list[Location]
    dinner: Location
    night: Location

def make_itinerary(prefs: Preferences):
    day = prefs.data.get_weekday()
    myItinerary = Itinerary()

    filters = [
        lambda loc: True if prefs.onlyFree else prefs.onlyFree and loc.price == 0,
        lambda loc: loc.category in prefs.categories,
        lambda loc: True if prefs.withPet else prefs.withPet and loc.with_pets
    ]
    ok = [ loc for loc in locations if all([ f(loc) for f in filters ]) ]

    def is_open(loc, start, end):
        x.opening_times[day].hour <= start and x.closing_times[day].hour >= end
    morning   = [x for x in ok if is_open(x, 10, 12) and not x.durata > 2]
    afternoon = [x for x in ok if is_open(x, 12, 18) and not x.durata > 6]
    evening   = [x for x in ok if is_open(x, 18, 22) and not x.durata > 4]

    calc_score()

    lambda calc: location = calc_age(current_user,20,40) + calc_likes(location.id) + calc_weather(location)
    morning = [(x, calc(x)) for x in morning]
    sorted(morning, key=lambda x: x[1], reverse=True)
    Itinerary.morning = morning[0]


    # prefs.luoghi
    #restaurant = [x for x in locations if  x.category == Category.RESTORATION]

    return {"response": "like added"}

weights = {
    "age"       : 0.25
    "distance"  : 0.25
    "rain"      : 0.5
    "likes"     : 0.5
}
scores = {}


    

def calc_age(user_age, lowest, highest):
    if user_age >= lowest and user_age <= highest:
        return 1.0
    diff = min(lowest - user_age, user_age - highest)
    return (1.0 - (diff / 100.0)) * weights["age"]

def calc_likes(id):
    API_KEY = "Your API Key"
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY


#def distance

#def tests():
    #print(make_itinerary({
        
    #}))