# Python code​​​​​​‌‌‌​‌‌‌​​‌‌‌​​‌‌‌‌​​​‌​‌​ below
# Use print("messages...") to debug your solution.
import json


TotalEvents = 0
TotalFelt = 0
MostFeltEvent = ""
MostFeltCount = 0

def calc_summary():
    global TotalEvents, TotalFelt, MostFeltEvent, MostFeltCount
    # open the data file and load the JSON
    #with open("/tmp/deps/30DayQuakes.json", "r") as datafile:
    #    data = json.load(datafile)
    with open("../../30DayQuakes.json", "r") as datafile:
        data = json.load(datafile)
    # YOUR CODE GOES HERE
    # Calculate the values

    # Total reports in data set
    TotalEvents = int(data['metadata']['count'])

    # Reports where >= 100 people felt the quake
    felt_reports = list(filter(feltreport, data['features']))
    TotalFelt = len(felt_reports)

    # Name of event which was felt by most amount of people
    mostfeltquake = max(data["features"], key=getfelt)
    MostFeltEvent = mostfeltquake['properties']['title']

    # Number of reported felt people for the previous identified event name
    MostFeltCount = int(mostfeltquake['properties']['felt'])


def feltreport(q):
    f = q["properties"]["felt"]
    return (f is not None and f >= 100)

def getfelt(q):
    f = q["properties"]["felt"]
    if f is not None:
        return f
    return 0


# This is how your code will be called.
try:
    calc_summary()
    result = (TotalEvents, TotalFelt, MostFeltEvent, MostFeltCount)
    print(result)
except:
    result = (0,0,"",0)