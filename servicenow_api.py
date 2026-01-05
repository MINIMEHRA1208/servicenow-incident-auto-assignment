import requests
from config import SNOW_INSTANCE, SNOW_USERNAME, SNOW_PASSWORD

HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

def get_incident(sys_id):
    url = f"{SNOW_INSTANCE}/api/now/table/incident/{sys_id}"
    response = requests.get(
        url,
        auth=(SNOW_USERNAME, SNOW_PASSWORD),
        headers=HEADERS,
        timeout=10
    )
    response.raise_for_status()
    return response.json()["result"]

def update_incident(sys_id, data):
    url = f"{SNOW_INSTANCE}/api/now/table/incident/{sys_id}"
    response = requests.patch(
        url,
        auth=(SNOW_USERNAME, SNOW_PASSWORD),
        headers=HEADERS,
        json=data,
        timeout=10
    )
    response.raise_for_status()
