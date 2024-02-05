# Get city name from user input
# Convert city name to IATA code
# Use IATA code to get flight data from Sheety
import os

import requests

KIWI_API_KEY = os.getenv("KIWI_API_KEY")
KIWI_URL = "https://tequila-api.kiwi.com/locations/query"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.url = 'https://tequila-api.kiwi.com/locations/query'
        self.headers = {
            'apikey': KIWI_API_KEY
        }

    def get_iata_code(self, city):
        params = {
            'term': city,
            'location_types': 'city'
        }

        response = requests.get(url=self.url, headers=self.headers, params=params)
        response.raise_for_status()

        data = response.json()

        return data['locations'][0]['code']
