import json

def lambda_handler(event, context):
    """
    AWS Lambda handler function to generate a secret code.
    """
    try:
        # Extract data from the event (payload from previous states)
        film_title = event.get("film_title")
        average_height = event.get("average_height")
        num_planets = event.get("num_planets")
        planet_id = event.get("planet_id")
        residents_mod = event.get("residents_mod")
        first_letter = event.get("first_letter")

        # Validate required fields
        if None in [film_title, average_height, num_planets, planet_id, residents_mod, first_letter]:
            raise ValueError("Missing required data in the event payload.")

        # First character: Map film_title to a letter (e.g., first letter of the film title)
        first_char = chr(64 + film_title)

        # Second character: Use residents_mod (already calculated in previous steps)
        second_char = residents_mod  # chr(48) is '0'

        # Third character: Use the first letter of the planet name
        third_char = first_letter.upper() if first_letter else 'X'

        # Combine the characters to form the secret code
        secret_code = f"{first_char}{second_char}{third_char}"

        return {
            "statusCode": 200,
            "body": {
                "secret_code": secret_code
            }
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": {
                "error": str(e)
            }
        }