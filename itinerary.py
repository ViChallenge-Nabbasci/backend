from datetime import datetime

from test import Category, Location


class Preferences(BaseModel):
    byCar:bool
    lunch:bool
    dinner:bool
    onlyFree:bool
    data:datetime.time
    luoghi:list[Category]



@app.post("/getItinerary")
async def get_Itinerary(req: Preferences):
    ok = []
    for x in luoghi:
        if()

    return {"response": "like added"}