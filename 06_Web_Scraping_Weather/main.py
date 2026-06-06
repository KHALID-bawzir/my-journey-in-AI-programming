from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re
from datetime import date
from tabulate import tabulate
import json

def get_forecast_data():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--log-level=3')
    prefs = {
        "profile.default_content_setting_values": {
            "images": 2,
            "plugins": 2,
            "popups": 2,
            "notifications": 2,
            "media_stream": 2,
        }
    }
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options)
    driver.get("https://world-weather.info/")
    html = driver.page_source


    soup = BeautifulSoup(html, "html.parser")
    resorts = soup.find("div", id="resorts")

    re_cities = r'">([\w\s]+)<\/a><span>'
    cities =re.findall(re_cities , str(resorts))

    re_temps= r'<span>(\+\d+|\-\d+)<span'
    temps =re.findall(re_temps , str(resorts))

    conditions_tag= resorts.find_all('span' , class_='tooltip')
    conditions = [condition.get('title') for condition in conditions_tag]

    weather_data = zip(cities, temps, conditions)
    return weather_data


def get_forecast_text():
    data = get_forecast_data()
    if data:
        today = date.today().strftime("%d %m, %Y")
        with open("weather_data.txt", "w" , encoding="utf-8") as f:
            f.write('Popular Cities Forecast' + '\n')
            f.write(today + '\n')
            f.write('_'*25 + '\n')
            table = tabulate(data, headers=['City', 'Temperature', 'Conditions'] , tablefmt='fancy_grid')
            f.write(table)

def get_forecast_json():
    data = get_forecast_data()
    if data:
        today = date.today().strftime("%d %m, %Y")
        cities = [{ 'city' : city  , 'temp' : temp ,'condition' : condition} for  city,temp,condition in data]
        data_json = {'title' : 'Popular Cities Forecast' , 'data' : today , 'cities' : cities}
        with open("weather_data.json", "w", encoding="utf-8") as f:
            json.dump(data_json, f , ensure_ascii=False)


if __name__ == '__main__':
    get_forecast_text()
    get_forecast_json()