import os
import smtplib
from flask import jsonify
from email.mime.text import MIMEText
from dotenv import load_dotenv
load_dotenv()


class EmailChannel:
    """Handles email sending."""

    def __init__(self):
        """Initialize email configuration from environment variables."""
        self.smtp_host = os.getenv("SMTP_HOST", "smtp.gmail.com")
        self.smtp_port = int(os.getenv("SMTP_PORT", 465))
        self.user = os.getenv("EMAIL_USER")
        self.password = os.getenv("EMAIL_APP_PASSKEY")
        self.default_subject = "Test Email"

    def send_smtp_email(self, subject: str, msg_body: str, sender: str, recipients: list):
        """
        Sends an email using SMTP.
        """
        try:
            # Create MIMEText email message
            msg = MIMEText(msg_body)
            msg["Subject"] = subject
            msg["From"] = sender
            msg["To"] = ", ".join(recipients)

            # Establish secure SMTP connection and send email
            with smtplib.SMTP_SSL(self.smtp_host, self.smtp_port) as smtp_server:
                smtp_server.login(sender, self.password)
                smtp_server.sendmail(sender, recipients, msg.as_string())

            return jsonify({"status": "success"})

        except Exception as e:
            print("Error sending email:", e)
            return jsonify({"error": str(e)}), 500

    def send_message(self, recipient: str, message_body: str):
        """
        Sends a mail using the SMTP email service.
        """
        sender = self.user
        recipients = [recipient]
        try:
            subject = message_body.get("subject")
        except:
            subject = self.default_subject
        
        response = self.send_smtp_email(subject, message_body, sender, recipients)
        return response
