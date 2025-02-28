import requests
import pandas as pd
from datetime import datetime 

BASE_URL = " http://api.jolpi.ca/ergast/f1/"

# def get_drivers():
#     """Fetches all drivers and maps driver number to name"""
#     url = f"{BASE_URL}/drivers"
#     response = requests.get(url)
#     if response.status_code == 200:
#         drivers = response.json()
#         return {driver["driver_number"]: driver["full_name"] for driver in drivers}
#     return None

# def get_circuit(session_key, circuit_key):
#     """Fetches circuit name from circuit key"""

#     url = F"{BASE_URL}/sessions?session_key={session_key}&circuit_key={circuit_key}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         circuit = response.json()
#         return circuit[0]["circuit_short_name"]
#     return None

# def get_race_sessions(circuit_key):
#     """Fetches the race sessions in given year and circuit"""

#     url = f"{BASE_URL}/sessions?circuit_key={circuit_key}"
#     response = requests.get(url)
#     if(response.status_code == 200):
#         sessions = response.json()
#         return [session for session in sessions if session["session_type"] == "Race" and session["session_name"] == "Race"]
#     return None

# def get_weather(session_key):
#     """Fetches the weather information for the given session"""

#     url = f"{BASE_URL}/weather?session_key={session_key}"
#     response = requests.get(url)
#     return response.json() if response.status_code == 200 else None

def get_final_positions(circuit, driver):
    """Fetches the final position of the driver in the given session"""

    url = f"{BASE_URL}/circuits/{circuit}/drivers/{driver}/results/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def get_historical_data(circuit, driver):
    """Fetch the historical data for the driver in the given circuit"""

    results = get_final_positions(circuit, driver)
    race_results = {}

    for race in results['MRData']['RaceTable']['Races']:
        season = race['season']
        position = race['Results'][0]['position']
        race_results[season] = position

    return race_results

# def get_historical_race_data(driver_number, circuit_key):
#     """Fetches the historical race data for multiple years"""

#     data = []

#     sessions = get_race_sessions(circuit_key)
#     print(sessions)
#     driver = get_drivers()[driver_number]
    
#     for session in sessions:
#         session_key = session["session_key"]
#         final_positions = get_final_positions(session_key)
#         #weather = get_weather(session_key)
        
#         for position in final_positions:
#             if position["driver_number"] == driver_number:
#                 data.append({
#                     "year": session["year"],
#                     "driver": driver,
#                     "position": position["position"],
#                 })
        
#     df = pd.DataFrame(data)
#     pivot_df = df.pivot_table(index="driver", columns="year", values="position", aggfunc="first")
#     pivot_df = pivot_df.fillna('N/A') 
    
#     return pivot_df

# data = get_historical_race_data(4, 7)
# print(data)