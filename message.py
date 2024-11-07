from helpers.storage import *
from datetime import datetime

class Message():

    def send_sms(self,phone, content):
        print("SMS sent")
        return True
    
    def send_email(self, email, content):
        print("Email send")
        return True
    
    def message_service(self, data):
        type = data.get("type")
        recipient = data.get("recipient")
        content =  data.get("content")

        if type == "SMS":
            self.send_sms(recipient, content)
        elif type == "Email":
            self.send_email(recipient, content)
        return True
