from datetime import datetime
from unicodedata import category
# from test import Category, locations,current_user
from pydantic import BaseModel, Field
import location
import datetime
import users

class Preferences(BaseModel):
    byCar: bool
    lunch: bool
    dinner: bool
    onlyFree: bool
    withPet:bool
    data: datetime.date
    categories: list[location.Category]

class Itinerary(BaseModel):
    morning: list[location.Location]
    lunch: list[location.Location]
    afternoon: list[location.Location]
    dinner: list[location.Location]
    night: list[location.Location]

def make_itinerary(prefs: Preferences):
    day = prefs.data.weekday()


    filters = [
        #lambda loc: True if prefs.onlyFree else prefs.onlyFree and loc.price == 0,
        #lambda loc: loc.category in prefs.categories,
        #lambda loc: True if prefs.withPet else prefs.withPet and loc.with_pets
    ]
    ok = [ loc for loc in location.locations if all([ f(loc) for f in filters ]) ]


    def is_open(loc, start, end):
        return loc.opening_times[day].hour <= start and loc.closing_times[day].hour >= end
        #return True
    morning   = [x for x in ok if is_open(x, 10, 12) and not x.durata > 2]
    afternoon = [x for x in ok if is_open(x, 12, 18) and not x.durata > 6]
    evening   = [x for x in ok if is_open(x, 18, 22) and not x.durata > 4]

    print(len(morning))
    print(len(afternoon))
    print(len(evening))

    calc = lambda location: calc_age(users.current_user.age,20,40) + calc_likes(location.id) + calc_weather(location)
    morning = [(x, calc(x)) for x in morning]
    sorted(morning, key=lambda x: x[1], reverse=True)
    morningAct =[elem[0] for elem in morning[0:3] ]

    afternoon = [(x, calc(x)) for x in afternoon]
    sorted(afternoon, key=lambda x: x[1], reverse=True)
    afternoonAct=[elem[0] for elem in afternoon[0:3] ]

    evening = [(x, calc(x)) for x in evening]
    sorted(evening, key=lambda x: x[1], reverse=True)
    eveningAct =[elem[0] for elem in evening[0:3] ]
    


    return Itinerary (
        morning= morningAct,
        lunch= afternoonAct,
        afternoon= afternoonAct,
        dinner= afternoonAct,
        night= eveningAct
    )

    # prefs.luoghi
    #restaurant = [x for x in locations if  x.category == Category.RESTORATION]


weights = {
    "age"       : 0.25,
    "distance"  : 0.25,
    "rain"      : 0.5,
    "likes"     : 0.5
}
scores = {}


    

def calc_age(user_age, lowest, highest):
    if user_age >= lowest and user_age <= highest:
        return 1.0
    diff = min(lowest - user_age, user_age - highest)
    return (1.0 - (diff / 100.0)) * weights["age"]

def calc_likes(id):
    return 0

def calc_weather(id):
    return 0

#def distance

#def tests():
    #print(make_itinerary({
        
    #}))