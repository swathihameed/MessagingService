from flask import jsonify
import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()

class SMSChannel:
    """Handles SMS message sending using Twilio API."""

    def __init__(self):
        """Initializes the Twilio client with credentials from environment variables."""
        self.account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        self.auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        self.from_phone = os.getenv("TWILIO_FROM_PHONE_NUMBER")
        self.client = Client(self.account_sid, self.auth_token)

    def send_message(self, message_body: str, recipient: str):
        """
        Sends an SMS message using the Twilio API.
        """
        try:
            message = self.client.messages.create(
                body=message_body,
                from_=self.from_phone,
                to=recipient
            )
            return jsonify({"status": message.status, "id": message.sid})

        except Exception as e:
            print("Error sending SMS:", e)
            return jsonify({"error": str(e)}), 500
