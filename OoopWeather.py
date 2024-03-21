import requests
import json

class OpenMapAPI:
    def __init__(self,api_key) -> None:
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

#we don't define base_url in the init because it's not supposed to eer be changeable
        
    def get_weather_by_city(self, city_name):
        #https://api.openweathermap.org/data/2.5/weather?q={city%20name}&appid={API%20key}
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