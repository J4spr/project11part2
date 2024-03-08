import requests
import calculations as calc
import json


def getweatherforecast(api_key, lat, lon):
    data = requests.get(
        f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units={"metric"}").json()
    return data["list"][:5]  # only first 5 days


def formatweatherforecast(weather_forecast):
    # Function to format weather forecast data
    forecasts = []
    for forecast in weather_forecast:
        date = forecast["dt_txt"].split()[0]
        temperature = forecast["main"]["temp"]
        description = forecast["weather"][0]["description"]
        wind_speed = forecast["wind"]["speed"]
        precipitation = forecast["rain"]["3h"] if "rain" in forecast else 0

        # Append formatted forecast to forecasts list
        forecasts.append({
            "date": date,
            "temperature": temperature,
            "description": description,
            "wind_speed": wind_speed,
            "precipitation": precipitation
        })
    return forecasts


def combineResults(results, location, idealTemp, idealRain):
    # berekend de gemiddelde temperatuur
    temp = calc.getAverage(results, lambda x: x.get('temperature'))
    # berekend de totale sneeuw
    rain = calc.getSum(results, lambda x: x.get('precipitation'))
    # berekend de score
    score = 0
    idealTemp = int(idealTemp)
    if idealTemp - 2 <= temp <= idealTemp + 2:
        score = 5
    elif idealTemp - 3 <= temp <= idealTemp + 3:
        score = 4
    elif idealTemp - 5 <= temp <= idealTemp + 5:
        score = 3
    elif idealTemp - 7 <= temp <= idealTemp + 7:
        score = 2
    elif idealTemp - 10 <= temp <= idealTemp + 10:
        score = 1
    if idealRain != 3 and rain < idealRain:
        score += 4
    response = {
        # maakt een lijst met de begin en einddatum
        "location": location,
        "date": [results[0].get('date'), results[len(results) - 1].get('date')],
        "min_temp": calc.getMin(results, lambda x: x.get('temperature')),
        "max_temp": calc.getMax(results, lambda x: x.get('temperature')),
        "temp": round(temp, 1),
        "wind_speed": round(calc.getAverage(results, lambda x: x.get('wind_speed')), 2),
        "precipitation": round(sum([x.get('precipitation') for x in results]), 2),
        "score": score,
        "description": calc.getMostFrequent(results, lambda x: x.get('description'))
    }
    return response
