import json
import requests

def get_weather_desc_and_temp():
    api_key = "7438e09ecf5b39d2c6527b7693e8c41c"
    city = "Shelley"
    url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"

    requests = requests.get(url)
    json = requests.json()


    description = json.get('weather')[0].get("description")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")
   

    return {'description': description, 
              'temp_min': temp_min,
              'temp_max' : temp_max}

def main():
weather_dict = get_weather_desc_and_temp() 
# Print the Results
print("Today's forecast is", weather_dict.get('descriptions'))   
print("The maximum temperature is", weather_dict.get('temp_max'))
print("The minimum temperature is", weather_dict.get('temp_min'))
main()