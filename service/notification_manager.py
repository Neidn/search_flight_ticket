import os
import smtplib

from twilio.rest import Client


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.twilio_account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        self.twilio_auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        self.twilio_phone_number = os.getenv("TWILIO_PHONE_NUMBER")

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

        return True if message.sid else False

    def send_email(self, message: str, target_email: str) -> bool:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=os.getenv("MY_EMAIL"), password=os.getenv("EMAIL_PASSWORD"))
            result = connection.sendmail(
                from_addr=os.getenv("MY_EMAIL"),
                to_addrs=target_email,
                msg=f"Subject:Flight Deal!\n\n{message}"
            )

            return True if not result else False
