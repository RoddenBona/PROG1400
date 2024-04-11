"""
Author: Rodden Bona
Student ID: W0461260
Course: PROG1400
Repository: https://github.com/RoddenBona/PROG1400
Project: JSON Weather App Part 2
Version 1.0
Last edited: April 11 2024
"""

import OOPWeatherap_1
#importing the first program to fucntion inside of this one


#Input our api key
api_key = "82005d27a116c2880c8f0fcb866998a0"
open_map = OOPWeatherap_1.OpenMapAPI(api_key)
kelvin = 273.15
city_name = input("Enter city name: ")

try:
    city_weather = open_map.get_weather_by_city(city_name)
except NameError:
    print("""Check city name, api key, internet connection, or api service
          One of them may be missing or down at the moment""")


if city_weather["cod"] == 200:
    print(f"weather in", city_name)
    print("Description: ", city_weather["weather"][0]["description"])
    print("temperature", round(city_weather["main"]["temp"] - kelvin), "°C")
else:
    print("""Check city name, api key, internet connection, or api service
          One of them may be missing or down at the moment""")