import requests

headers = {
    "x-rapidapi-key": "RAPIDAPI_KEY",
    "x-rapidapi-host": "ufc-api5.p.rapidapi.com",
}


def get_fighter_stats(fighter_name):
    url = f"https://ufc-api5.p.rapidapi.com/api/v1/fighters/{fighter_name}/stats"

    response = requests.get(url, headers=headers)
    parsed = response.json()

    if "data" not in parsed:
        return None

    return parsed["data"]