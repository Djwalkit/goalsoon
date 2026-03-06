import requests
from .config import API_KEY, BASE_URL

def headers():
    return {"x-apisports-key": API_KEY}

def live_fixtures():
    r = requests.get(BASE_URL + "/fixtures", headers=headers(), params={"live":"all"}, timeout=20)
    r.raise_for_status()
    return r.json().get("response", [])

def fixture_stats(fixture_id):
    r = requests.get(BASE_URL + "/fixtures/statistics", headers=headers(), params={"fixture":fixture_id}, timeout=20)
    r.raise_for_status()
    return r.json().get("response", [])