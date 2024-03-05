import json
import os
import sys

from dotenv import load_dotenv

from mail import *
from weather import getweatherforecast

# load the .env file
load_dotenv()

# if it doesn't work delete this line but for me, it didn't work, so I had to add this line
print(os.getcwd())
os.chdir("./projects/skiSeason")
print(os.getcwd())


def main():
    # get api key from .env file and put it into a variable
    key = os.getenv("WEATHER_TOKEN")
    # get the location from the json file
    locations = getonelocation()
    # TODO: remove this line for final version
    print(locations)
    print("----------------------------------------")
    for cords in locations:
        print(cords)
        response = getweatherforecast(key, cords[1], cords[2])
        print(response)


def parsejson():
    locations = dict
    # open the json file and dump it into a variable
    with open("ski.json", "r") as file:
        locations = json.load(file)
    # return that shit
    return locations


def getonelocation():
    # call parsejson for putting the response in a dictionary
    data = parsejson()
    # The "locationlist" variable likely stores a list of locations or addresses.
    locationlist = []
    # loop over each location in the json file and get the lat and lon
    for location in data["locations"]:
        name = location['name']
        lat = location['lat']
        lon = location['lon']
        locationtup = (name, lat, lon)
        locationlist.append(locationtup)
        # TODO: remove this line for final version
        print(f"name: {name}, lat: {lat}, lon: {lon}")
    return locationlist


# check if the main function is the main entry point
if __name__ == '__main__':
    try:
        # run that shit
        main()
    # handle keyboard interrupt errors
    except KeyboardInterrupt:
        sys.exit(130)
