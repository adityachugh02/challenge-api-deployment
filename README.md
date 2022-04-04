# ImmoEliza API
https://immoeliza-api.herokuapp.com/predict/
## Description
The ImmoEliza API returns a house price prediction and a mean squared error based on 4 mandatory parameters: area, property type, room number and zip code. Additional parameters can be specified for more accurate predictions.
### Structure:
```json
{
  "data": {
    "area": int,
    "property-type": "APARTMENT" | "HOUSE" | "OTHERS",
    "rooms-number": int,
    "zip-code": int,
    "land-area": Optional[int],
    "garden": Optional[bool],
    "garden-area": Optional[int],
    "equipped-kitchen": Optional[bool],
    "full-address": Optional[str],
    "swimming-pool": Optional[bool],
    "furnished": Optional[bool],
    "open-fire": Optional[bool],
    "terrace": Optional[bool],
    "terrace-area": Optional[int],
    "facades-number": Optional[int],
    "building-state": Optional[
      "NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD"
    ]
  }
```
### Response
```json
{
  "prediction": float,
  "error": float
}
```
## Installation
### Prerequisites
> Docker

> Heroku CLI
### Build
> docker build -t immoeliza-api:latest .

> heroku container:push web --app immoeliza-api

> heroku container:release web --app immoeliza-api
## Usage
Once released, the API will be available the following address: https://immoeliza-api.herokuapp.com/
### Status
Check server status at: https://immoeliza-api.herokuapp.com/
### Documentation
The documentation is available at: https://immoeliza-api.herokuapp.com/predict
### Prediction
POST data at https://immoeliza-api.herokuapp.com/predict
