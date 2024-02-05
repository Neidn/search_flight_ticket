# Get city name from user input
# Convert city name to IATA code
# Use IATA code to get flight data from Sheety
import os

import requests

KIWI_API_KEY = os.getenv("KIWI_API_KEY")


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        """
        self.url = 'https://tequila-api.kiwi.com/locations/query'
        self.api_key = 'YOUR_API_KEY'
        self.headers = {
            'apikey': self.api_key
        }
        """

    def get_iata_code(self, city):
        return "Testing IATA code"
