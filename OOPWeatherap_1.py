"""
Author: Rodden Bona
Student ID: W0461260
Course: PROG1400
Repository: https://github.com/RoddenBona/PROG1400
Project: Json Weather App Part 1
Version 1.0
Last edited: March 28 2024
"""
import requests
import json
#We neeed to import the modules needed to make requests and access json files from the internet

class OpenMapAPI:
    def __init__(self,api_key,message) -> None:
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
        self.message = ""

#we don't define base_url in the init because it's not supposed to eer be changeable
        
    def get_weather_by_city(self, city_name):
        """
        The OpenWeatherMap API can call by city name, state code, and country
        https://api.openweathermap.org/data/2.5/weather?q={city%20name}&appid={API%20key}
        """
        url = f"{self.base_url}?q={city_name}&appid={self.api_key}"
        response = requests.get(url)
        #error checking
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None
        
if __name__ == "__main__":
    pass