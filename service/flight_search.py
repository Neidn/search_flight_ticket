# Get city name from user input
# Convert city name to IATA code
# Use IATA code to get flight data from Sheety
import os
import datetime
import requests

from pprint import pprint


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.url = "https://tequila-api.kiwi.com/locations/query"
        self.headers = {
            'apikey': os.getenv("KIWI_API_KEY")
        }
        self.date_from = datetime.datetime.now()
        # Set the date to 6 months from today
        self.date_to = (datetime.datetime.now() + datetime.timedelta(days=180))

    def get_iata_code(self, city: str) -> str:
        params = {
            'term': city,
            'location_types': 'city'
        }

        response = requests.get(
            url=self.url,
            headers=self.headers,
            params=params,
        )
        response.raise_for_status()

        data = response.json()

        return data['locations'][0]['code']

    # Get flight data from Sheety
    # Round trip
    def get_flight_data(self, origin_city: str, destination_city: str) -> dict | None:
        url = "https://tequila-api.kiwi.com/v2/search"
        headers = {
            'apikey': os.getenv("KIWI_API_KEY")
        }

        params = {
            'fly_from': origin_city,
            'fly_to': destination_city,
            'dateFrom': self.date_from.strftime("%d/%m/%Y"),
            'dateTo': self.date_to.strftime("%d/%m/%Y"),
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'flight_type': 'round',
            'one_for_city': 1,
            'curr': 'USD',
        }

        response = requests.get(
            url=url,
            headers=headers,
            params=params,
        )
        response.raise_for_status()

        data = response.json()

        if len(data['data']) == 0:
            return None

        return data['data'][0]
