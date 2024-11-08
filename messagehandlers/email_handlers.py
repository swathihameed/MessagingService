# email_channel.py
from flask import jsonify

class EmailChannel:

    def send_message(self, recipient, content):
        print(f"Sending Email to {recipient}: {content}")
        # Actual logic to send email, e.g., using SendGrid
        return jsonify({"success": "true"})
