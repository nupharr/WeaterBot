import requests
import os
from dotenv import load_dotenv
from datetime import date, datetime

load_dotenv()
WEATHER_TOKEN = os.getenv("WEATER_TOKEN")


def check_geo(location: str) -> dict | bool:
    responce = requests.get(
        f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=1&appid={WEATHER_TOKEN}"
    )
    if responce.ok:
        data = responce.json()
        ru_name = data[0].get("local_names", {}).get("ru")
        lat = data[0].get("lat")
        lon = data[0].get("lon")
        result = {"ru_name": ru_name, "lat": lat, "lon": lon}
        return result
    return False


def get_weater(lat: str, lon: str):
    responce = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&lang=ru&units=metric&appid={WEATHER_TOKEN}"
    )
    if responce.ok:
        data = responce.json()

        city = data["name"]
        cur_weater = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.fromtimestamp(
            data["sys"]["sunset"]
        ) - datetime.fromtimestamp(data["sys"]["sunrise"])

        return f"""***{datetime.now().strftime("%Y-%m-%d %H:%M")}***
Погода в городе: {city}
Температура: {cur_weater}°C
Влажность: {humidity}%
Давление: {pressure} мм.рт.ст
Ветер: {wind} м/с
Восход солнца: {sunrise_timestamp}
Закат солнца: {sunset_timestamp}
Продолжительность дня: {length_of_the_day}"""
