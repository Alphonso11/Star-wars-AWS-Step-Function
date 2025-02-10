import requests

def lambda_handler(event, context):
    """
    Fetches the planet data for the given planet_id, counts the number of residents,
    and returns the count modulo 10.
    """
    planet_id = event.get('planet_id')
    if planet_id is None:
        return {'residents_mod': None}
    url_planet = f"https://swapi.dev/api/planets/{planet_id}/"
    try:
        response = requests.get(url_planet)
        response.raise_for_status()
        planet_data = response.json()
        residents = planet_data.get('residents', [])
        residents_count = len(residents)
        residents_mod = residents_count % 10
        return {'residents_mod': residents_mod}
    except requests.exceptions.RequestException as err:
        print(f"Error fetching planet data: {err}")
        return {'residents_mod': None}
