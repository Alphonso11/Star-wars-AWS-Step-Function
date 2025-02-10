def lambda_handler(event, context):
    """
    Calculate the planet ID based on average height and number of planets.
    """
    avg_height = event.get('avg_height', 0)
    num_planets = event.get('num_planets', 0)
    if num_planets == 0:
        print("No planets available to select.")
        return {'planet_id': None}
    planet_id = int(avg_height) % num_planets
    return {'planet_id': planet_id}
