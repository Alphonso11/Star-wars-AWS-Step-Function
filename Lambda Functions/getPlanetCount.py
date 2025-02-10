import requests
import json

def lambda_handler(event, context):
    """
    Fetch the total number of planets from the SWAPI.
    """
    url = "https://swapi.dev/api/planets"
    try:
        response = requests.get(url)
        response.raise_for_status()
        response_json = response.json()
        num_planets = response_json.get('count', 0)
        return {'num_planets': num_planets}
    except requests.exceptions.RequestException as err:
        print(f"Error fetching planet data: {err}")
        return {'num_planets': 0}
