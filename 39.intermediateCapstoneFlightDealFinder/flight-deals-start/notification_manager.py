from twilio.rest import Client
import os

TWILIO_SID = os.environ["account_sid"]
TWILIO_AUTH_TOKEN = os.environ["auth_token"]
TWILIO_VIRTUAL_NUMBER = os.environ["Tel_from"]
TWILIO_VERIFIED_NUMBER = os.environ["Tel_to"]


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        pass

    # def send_sms(self, message):
    #     message = self.client.messages.create(
    #         body=message,
    #         from_=TWILIO_VIRTUAL_NUMBER,
    #         to=TWILIO_VERIFIED_NUMBER,
    #     )
    #     # Prints if successfully sent.
    #     print(message.sid)