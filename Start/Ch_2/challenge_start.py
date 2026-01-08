# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
from collections import defaultdict


# open the data file and load the JSON
def get_event_classification():
    with open("../../30DayQuakes.json", "r") as datafile:
        data = json.load(datafile)

    # use a defaultdict to categorize
    totals = defaultdict(int)
    for event in data["features"]:
        totals[event["properties"]["type"]] += 1

    return dict(totals)

result = get_event_classification()
print(result)
