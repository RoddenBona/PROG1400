import OoopWeather

#first we gotta deal with our api key
api_key = "82005d27a116c2880c8f0fcb866998a0"
open_map = OoopWeather.OpenMapAPI(api_key)
kelvin = 273.15
city_name = input("Enter city name: ")

try:
    city_weather = open_map.get_weather_by_city(city_name)
except NameError:
    print("""Check city name, api key, internet connection, or api service
          One of them may be missing or down at the moment""")



if city_weather:
    print(f"weather in", city_name)
    print("Description: ", city_weather["weather"][0]["description"])
    print("temperature", round(kelvin - city_weather["main"]["temp"]), "°C")
else:
    print("""Check city name, api key, internet connection, or api service
          One of them may be missing or down at the moment""")