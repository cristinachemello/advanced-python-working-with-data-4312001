# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
from collections import defaultdict

# open the data file and load the JSON
def getevents():
    with open("../../30DayQuakes.json", "r") as datafile:
        data = json.load(datafile)

        events = defaultdict(int)

        for quake in data["features"]:
            events[quake["properties"]["type"]] += 1
    
        return dict(events)  #convert into a regular dictionary