import requests


def check_geo(location: str) -> dict | bool:
    responce = requests.get(
        f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=1&appid=382d34fa699d7ad930838475e03efc70"
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
        f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=current&lang=ru&appid=382d34fa699d7ad930838475e03efc70"
    )
    if responce.ok:
        data = responce.json()
        return data
    return None
