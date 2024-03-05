import requests
import json


def getweatherforecast(api_key, lat, lon):
    data = requests.get(
        f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units={"metric"}").json()
    print(data)
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


# getweatherforecast("a64eb441861ee904de3adf8ea947a821", "Laax")
