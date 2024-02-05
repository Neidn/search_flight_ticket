import os
import requests

from twilio.rest import Client


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.url = os.getenv("SHEETY_URL")
        self.twilio_account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        self.twilio_auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        self.twilio_phone_number = os.getenv("TWILIO_PHONE_NUMBER")
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

    def send_sms(self, message: str, target_phone_number: str) -> bool:
        client = Client(
            self.twilio_account_sid,
            self.twilio_auth_token,
        )
        message = client.messages.create(
            body=message,
            from_=self.twilio_phone_number,
            to=target_phone_number
        )
        print(message.sid)

        return True if message.sid else False
