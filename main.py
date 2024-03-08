import json
import os
import sys

import json

import createMail
import mail
import weather
from mail import *
import weather

# load the .env file


def main():
    while True:
        idealTemp = input("Enter temp in °C: ")
        if idealTemp.isnumeric():
            break
        print("enter a correct number")
    print("1) > 1mm")
    print("2) > 2mm")
    print("3) no preference")
    while True:
        idealRain = input("Enter ideal rain: ")
        if idealRain.isnumeric() and 1 <= int(idealRain) <= 3:
            break
        print("enter a correct number")
    with open('apikey.json', 'r') as file:
        key = json.load(file)
    # get the location from the json file
    locations = getonelocation()
    list = []
    # todo: remove this
    # response = weather.getweatherforecast(key, locations[0][2], locations[0][3])
    # response = weather.combineResults(weather.formatweatherforecast(response), {"city": locations[0][0], "country": locations[0][1]}, int(idealTemp), int(idealRain))
    # list.append(response)
    for cords in locations:
        response = weather.getweatherforecast(key, cords[2], cords[3])
        response = weather.combineResults(weather.formatweatherforecast(response), {"city": cords[0], "country": cords[1]}, int(idealTemp), int(idealRain))
        list.append(response)
    list = sorted(list, key=lambda x: x.get("score"), reverse=True)
    email = createMail.createMail(list)
    mail.send("minejeis.developer@gmail.com", email)
    print("mail sent")


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
        city = location['city']
        lat = location['lat']
        lon = location['lon']
        country = location['country']
        locationtup = (city, country, lat, lon)
        locationlist.append(locationtup)
    return locationlist


# check if the main function is the main entry point
if __name__ == '__main__':
    try:
        # run that shit
        main()
    # handle keyboard interrupt errors
    except KeyboardInterrupt:
        sys.exit(130)
