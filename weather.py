import requests
import sys

api_key = "xxxxxxxxxxxxxxxxx"
base_url= "http://api.openweathermap.org/data/2.5/weather?"

city_name = sys.argv[1]

full_url = base_url + "q=" + city_name + "&appid=" + api_key
req = requests.get(full_url)
info = req.json()

if info["cod"] != "404":
    x = info["main"]
    current_temperature = x["temp"]
    tnc = round(float(current_temperature - 273.15),2)
    current_pressure = x["pressure"]
    current_humidiy = x["humidity"]
    z = info["weather"]
    weather_description = z[0]["description"]
    s = info["wind"]
    speed = s["speed"]
    print()
    print("Temperature (in celsius unit): ",
        					round(float(current_temperature - 273.15),2) , "°C",
        		"\nAtmospheric pressure : " +
        					str(current_pressure) + "hpa"
        		"\nHumidity : " +
        					str(current_humidiy) + "%"
        		"\nDescription: " +
        					str(weather_description).capitalize()+
                "\nWind Speed :" + str(speed) + "m/s" +"\n")

else:
  print("Not Found ")
