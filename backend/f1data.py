import requests
import pandas as pd
from datetime import datetime 

BASE_URL = "https://api.openf1.org/v1"

def get_drivers():
    """Fetches all drivers and maps driver number to name"""
    url = f"{BASE_URL}/drivers"
    response = requests.get(url)
    if response.status_code == 200:
        drivers = response.json()
        return {driver["driver_number"]: driver["full_name"] for driver in drivers}
    return None

def get_circuit(session_key, circuit_key):
    """Fetches circuit name from circuit key"""

    url = F"{BASE_URL}/sessions?session_key={session_key}&circuit_key={circuit_key}"
    response = requests.get(url)
    if response.status_code == 200:
        circuit = response.json()
        return circuit[0]["circuit_short_name"]
    return None

def get_race_sessions(year, circuit_key):
    """Fetches the race sessions in given year and circuit"""

    url = f"{BASE_URL}/sessions?year={year}&circuit_key={circuit_key}"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

def get_weather(session_key):
    """Fetches the weather information for the given session"""

    url = f"{BASE_URL}/weather?session_key={session_key}"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

def get_final_positions(session_key):
    """Fetches the final position of the driver in the given session"""

    url = f"{BASE_URL}/position?session_key={session_key}"
    response = requests.get(url)
    positions = response.json()
    last_positions = {}
    for position in positions:
        driver_number = position["driver_number"]
        position_time = position["date"]

        if driver_number not in last_positions or position_time > last_positions[driver_number]["date"]:
            last_positions[driver_number] = position

    return list(last_positions.values())

def get_historical_race_data(years, circuit_key):
    """Fetches the historical race data for multiple years"""

    data = []

    for year in years:
        sessions = get_race_sessions(year, circuit_key)
        race_session = next((s for s in sessions if s["session_type"] == "Race" and s["session_name"] == "Race"), None)

        if not race_session:
            continue

        session_key = race_session["session_key"]
        positions = get_final_positions(session_key)
        #weather = get_weather(session_key)

        for driver in positions:
            data.append({
                "year": year,
                "circuit": get_circuit(session_key, circuit_key),
                "driver": get_drivers()[driver["driver_number"]],
                "driver_number": driver["driver_number"],
                "position": driver["position"],
            })

    return pd.DataFrame(data)
    
df = get_historical_race_data([2023,2024], 7)
print(df)