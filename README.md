# Star Wars AWS Step Function

This project demonstrates an AWS Step Function workflow that processes data inspired by the Star Wars universe. The workflow interacts with several AWS Lambda functions to retrieve data, perform calculations, and generate a custom output.

## Workflow Overview

The Step Function workflow consists of the following states:

1. **GetFilm**: Fetches film data using the `getFilmData` Lambda function.
2. **AverageHeight**: Calculates the average height of characters from the film using the `calculateAverageHeight` Lambda function.
3. **PlanetCount**: Counts the number of planets using the `getPlanetCount` Lambda function.
4. **SelectPlanet**: Selects a planet based on average character height and planet count using the `selectPlanet` Lambda function.
5. **Parallel Processing**:
   - **CountResident**: Counts the number of residents on the selected planet.
   - **GetPlanetName**: Retrieves the name of the selected planet.
6. **MergeParallelOutputs**: Merges the results of the parallel branches into a unified output.
7. **GenerateCode**: Combines all results to produce the final output using the `generateCode` Lambda function.

## Diagram

Below is the visual representation of the workflow:

![Step Functions Graph](stepfunctions_graph.png)

## State Machine JSON Definition

The JSON definition of the Step Function is provided in [`StarWars.asl.json`](StarWars.asl.json). This file defines all states, transitions, and Lambda integrations used in the workflow.

## AWS Lambda Functions

The workflow uses the following AWS Lambda functions:

1. **`getFilmData`**: Fetches details about a Star Wars film, including character URLs.
2. **`calculateAverageHeight`**: Calculates the average height of characters in the film.
3. **`getPlanetCount`**: Returns the total number of planets in the dataset.
4. **`selectPlanet`**: Selects a planet based on provided metrics (average height and planet count).
5. **`countResident`**: Counts the number of residents on the selected planet.
6. **`getPlanetName`**: Retrieves the name of the selected planet.
7. **`generateCode`**: Generates the final output combining all the data.

## Example Output

An example output from the `GenerateCode` state:

```json
{
  "film_title": "A New Hope",
  "average_height": 175,
  "num_planets": 12,
  "planet_id": 5,
  "residents_mod": 7,
  "first_letter": "T"
}
