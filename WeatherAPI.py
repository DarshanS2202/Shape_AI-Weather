import requests
from datetime import datetime

api_key="ccab47aa5ed804b28046042a26a44ba2"
location=input("Enter the Location : ")
complete_api_link="https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key

api_link=requests.get(complete_api_link)
api_data=api_link.json()

temp=(api_data['main']['temp']-273.15)
weather_desc=api_data['weather'][0]['description']
hmdt=api_data['main']['humidity']
wind_spd=api_data['wind']['speed']
datetime=datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print("----------------------------------------------------------")
print("Weather Stats for - {}  || {}".format(location,datetime))
print("----------------------------------------------------------")
print("Current Temperature :",temp)
print("Current Weather Description :",weather_desc)
print("Current Humidity :",hmdt)
print("Current Wind Speed :",wind_spd)