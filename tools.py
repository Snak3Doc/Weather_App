# tools.py
### Imports ###
from pathlib import Path
import json
import re
from datetime import datetime, timedelta
from os import getenv
from dotenv import load_dotenv
load_dotenv()
from PIL import Image
import os

import requests
from requests.exceptions import RequestException, ConnectionError, HTTPError, Timeout
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from rich import print
from rich.traceback import install
install(show_locals=True)


### Constants ###
WORK_DIR = Path.cwd()
API_KEY = getenv("API_KEY")
CELSIUS_SYMBOL = u'\N{DEGREE SIGN}C'


### Functions ###
def get_weather(city_name, country_code):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&appid={API_KEY}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
            return weather_data
        
        elif response.status_code == 404:
            return "City not found"
        
        else:
            return f"Error, status code: {response.status_code}"
        
    except (ConnectionError, Timeout):
        print("Connection Error")
    except HTTPError as e:
        print(f"Error, status code: {e.response.status_code}")
    except RequestException:
        print("An error occurred during the request")
    
def get_forecast(city_name, country_code):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name},{country_code}&appid={API_KEY}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            forecast_data = response.json()
            return forecast_data
        
        elif response.status_code == 404:
            return "City not found"
        
        else:
            return f"Error, status code: {response.status_code}"

    except (ConnectionError, Timeout):
        print("Connection Error")
    except HTTPError as e:
        print(f"Error, status code: {e.response.status_code}")
    except RequestException:
        print("An error occurred during the request")


def get_icon(icon_code):
    icon_path = WORK_DIR/"weather_icons"/f"{icon_code}.png"
    if not icon_path.exists():
        url = f"http://openweathermap.org/img/w/{icon_code}.png"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                with open(WORK_DIR/"weather_icons"/f"{icon_code}.png", "wb") as icon_file:
                    icon_file.write(response.content)
                    print("Downloaded Icon")
            else:
                print(f"Error, status code: {response.status_code}")

        except (ConnectionError, Timeout):
            print("Connection Error")
        except HTTPError as e:
            print(f"Error, status code: {e.response.status_code}")
        except RequestException:
            print("An error occurred during the request")

    try:
        img = Image.open(icon_path)
        cropped_img = img.crop((0, 10, 50, 40))
        cropped_img.save(WORK_DIR/"weather_icons"/"temp.png")
        icon = QIcon(str(WORK_DIR/"weather_icons"/"temp.png")).pixmap(50, 25)
        os.remove(WORK_DIR/"weather_icons"/"temp.png")
        return icon
    except:
        print("Error creating icon")


def get_local_time(tz_offset):
    utc_time = datetime.utcnow() # Get the current UTC time
    timezone_offset = timedelta(seconds=tz_offset) # Calculate the timezone offset as a timedelta object
    date_time = utc_time + timezone_offset # Convert the UTC time to local time using the timezone offset
    local_time = date_time.strftime(f"%H:%M:%S") # Format the date_time into 24-hour (HH:MM:SS) format
    local_date = date_time.strftime(f"%d-%m-%y") # Format the date_time into (DD:MM:YYYT) format
    return local_time, local_date


def get_celsius(kelvin_temp):
    celsius_temp = f"{int(round(kelvin_temp - 273.15, 0))}{CELSIUS_SYMBOL}"
    return celsius_temp


def validate_str(input_str):
    regex_pattern = r'^[\w\s]+,\s[\w\s]+$'
    return bool(re.match(regex_pattern, input_str))

    #- Examples of how the pattern works:
        #- "Hanoi, VN" > True
        #- "New York, US" > True
        #- "US" > False
        #- "Hanoi" > False
        #- "Hanoi VN" > False

    #- This pattern ^[\w\s]+,\s[\w\s]+$ works as follows:

        #- ^ asserts the start of the line.
        #- [\w\s]+ matches one or more word characters or whitespace characters. This allows for multiple words before the comma.
        #- , matches the comma literally.
        #- \s matches any whitespace character.
        #- [\w\s]+ again matches one or more word characters or whitespace characters, allowing for multiple words after the comma.
        #- $ asserts the end of the line.


def write_json(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


### Experiment With Function Calls Here ###
if __name__ == "__main__":
    forecast_data = get_forecast("Hanoi", "VN")
    write_json(forecast_data, "data_forecast.json")
    #print(validate_string_format("a"))
    # city_name = "Melbourne"
    # country_code = "AU"

    # weather_data = get_weather(city_name, country_code)
    # #forcast_data = get_forcast(city_name, country_code)

    # write_json(weather_data, "data_weather.json")
    # #write_json(forcast_data, "data_forcast.json")

    # local_time, local_date = get_local_time(weather_data["timezone"])
    # print(local_time)
    # print(local_date)
    
    # temp = get_celsius(weather_data["main"]["temp"])
    # print(temp)

    # get_icon(weather_data["weather"][0]["icon"])