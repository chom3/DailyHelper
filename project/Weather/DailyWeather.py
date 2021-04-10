import requests
import json
from project.config import *

headers = {
    'Content-Type': 'application/json'
}

def getWeather(weather_api_token):
    reqResponse = requests.get(f"https://api.openweathermap.org/data/2.5/weather?zip={ZIPCODE}&units=imperial&appid={weather_api_token}", headers=headers).json()
    return f"In {reqResponse['name']}, the temperature is {reqResponse['main']['temp']}°F, " \
    + f"high is {reqResponse['main']['temp_max']}°F, " \
    + f"low is {reqResponse['main']['temp_min']}°F. " \
    + f"Expect {reqResponse['weather'][0]['description'].lower()}."