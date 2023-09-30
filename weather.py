from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_weather_from(city = "Dallas"):
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'
    weather_data = requests.get(request_url).json()
    return weather_data

if __name__ == "__main__":
    print("\n***Welcome to the Weather App**\n")
    city = input("\nPlease Enter a City: ")

    #Validate against empty strings
    if not bool(city.strip()):
        city = 'Kansas City'
    print("\n")
    print(get_weather_from(city))
