from pprint import pprint
import requests

URL = 'https://api.sheety.co/12629eb4ff41812f7e18fbf1372a8e11/flightDeals/prices'


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        response = requests.get(url=URL)
        response.raise_for_status()

        self.data = response.json()
        self.data = self.data['prices']

    def get_data(self):
        return self.data

    def update_iata_code(self, row_id, iata_code):
        body = {
            "price": {
                "iataCode": iata_code
            }
        }
        response = requests.put(url=f"{URL}/{row_id}", json=body)
        response.raise_for_status()
        pprint(response.json())
        return response.json()
