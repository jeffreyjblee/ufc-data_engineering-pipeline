import requests
from config.settings import RAPIDAPI_KEY, RAPIDAPI_HOST

headers = {
    "x-rapidapi-key": RAPIDAPI_KEY,
    "x-rapidapi-host": RAPIDAPI_HOST,
}


def get_fighter_stats(fighter_name):
    url = f"https://{RAPIDAPI_HOST}/api/v1/fighters/{fighter_name}/stats"

    response = requests.get(url, headers=headers)
    parsed = response.json()

    if "data" not in parsed:
        return None

    return parsed["data"]