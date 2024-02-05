import os
import requests



class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.url = os.getenv("SHEETY_URL")

        response = requests.get(url=self.url)
        response.raise_for_status()

        self.data = response.json()
        self.data = self.data['prices']

    def get_data(self) -> list:
        return self.data

    def update_iata_code(self, row_id: int, iata_code: str) -> dict:
        body = {
            "price": {
                "iataCode": iata_code
            }
        }
        response = requests.put(url=f"{self.url}/{row_id}", json=body)
        response.raise_for_status()

        return response.json()

