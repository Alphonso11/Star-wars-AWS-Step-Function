import requests
import datetime

def lambda_handler(event, context):
    """Fetches the earliest released Star Wars film."""
    url = "https://swapi.dev/api/films"

    try:
        response = requests.get(url)
        response.raise_for_status()
        response_json = response.json()  # Parse JSON response

        # Extract and convert release dates
        date_format = '%Y-%m-%d'
        dates = [datetime.datetime.strptime(item['release_date'], date_format) for item in response_json['results']]

        # Find the earliest movie
        earliest_movie_index = dates.index(min(dates))
        earliest_movie = response_json['results'][earliest_movie_index]

        # Extract character URLs
        character_urls = earliest_movie.get('characters', [])

        # Return relevant data
        return {
            "film_title": earliest_movie.get('episode_id'),
            "character_urls": character_urls
        }

    except requests.exceptions.RequestException as err:
        # Return error in the same structure
        return {
            "film_title": "Error",
            "character_urls": [],
            "error": f"Error: {err}"
        }