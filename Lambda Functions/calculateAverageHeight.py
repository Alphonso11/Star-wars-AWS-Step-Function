import requests

def lambda_handler(event, context):
    """
    Calculates the average height of characters from given URLs.

    Parameters:
    event (list): A list of URLs pointing to character data.

    Returns:
    dict: A dictionary containing the average height of the characters.
    """
    total_height = 0
    valid_heights_count = 0

    for url in event:  # event is a list of URLS
        try:
            response = requests.get(url)
            response.raise_for_status()
            character_data = response.json()
            height = character_data.get('height', '0')
            if height.isdigit():
                total_height += int(height)
                valid_heights_count += 1
        except requests.exceptions.RequestException as err:
            print(f"Error fetching data from {url}: {err}")

    if valid_heights_count == 0:
        average_height = 0
    else:
        average_height = total_height / valid_heights_count

    return {
        'average_height': average_height
    }
