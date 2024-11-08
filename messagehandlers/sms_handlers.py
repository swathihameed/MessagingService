# sms_channel.py
from flask import jsonify

class SMSChannel:

    def send_message(self, recipient, content):
        print(f"Sending SMS to {recipient}: {content}")
        # Actual logic to send SMS, e.g., using Twilio or any SMS service
        return jsonify({"success": "true"})
