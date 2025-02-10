import requests

def lambda_handler(event, context):
    """
    Fetches the planet data for the given planet_id and returns the first letter
    of the planet's name in uppercase.
    """
    planet_id = event.get('planet_id')
    if planet_id is None:
        return {'first_letter': None}
    url_planet = f"https://swapi.dev/api/planets/{planet_id}/"
    try:
        response = requests.get(url_planet)
        response.raise_for_status()
        planet_data = response.json()
        name = planet_data.get('name', '')
        if name:
            first_letter = name[0].upper()
            return {'first_letter': first_letter}
        else:
            print("Planet name is missing or empty.")
            return {'first_letter': None}
    except requests.exceptions.RequestException as err:
        print(f"Error fetching planet data: {err}")
        return {'first_letter': None}
