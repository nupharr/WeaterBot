import requests


def check_geo(location: str) -> bool:
    responce = requests.get(
        f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=1&appid=382d34fa699d7ad930838475e03efc70"
    )
    return responce.ok
