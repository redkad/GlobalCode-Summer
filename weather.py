"""import pyowm

apikey = "203a61c5705cf6e0a3a0608148ff3200"
owm = pyowm.OWM(apikey)
observation = owm.weather_at_place('Tokyo, japan')
observation1= owm.weather_at_place('Hong Kong')
w = observation.get_weather()
q = observation1.get_weather()
 
print("The wind in Tokyo is: " , w.get_wind())
print("The humidity in Tokyo is: ", w.get_humidity())
print("The temperature in Tokyo is: ", w.get_temperature(unit = "celsius"))
print("The snow in Tokyo is: ", w.get_snow())
print("The pressure in Tokyo is: " ,w.get_pressure())

print("The wind in Hong Kong is: " , q.get_wind())
print("The humidity in Hong Kong is: ", q.get_humidity())
print("The temperature in Hong Kong is: ", q.get_temperature(unit = "celsius"))
print("The snow in Hong Kong is: ", q.get_snow())
print("The pressure in Hong Kong is: " ,q.get_pressure())

    
if (w.get_humidity() > q.get_humidity()):
    print("The humidity in Tokyo is higher ")
    
else:
    print("The humidity in Hong Kong is higher ")"""

import wbdata

print(wbdata.api.get_country(country_id="GHA", incomelevel=None, lendingtype=None, display=None))