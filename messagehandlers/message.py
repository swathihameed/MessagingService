from helpers.storage import *
from datetime import datetime
from flask import jsonify

class Message():

    def send_sms(self,phone, content):
        print("SMS sent")
        return jsonify({"success": "true"})
    
    def send_email(self, email, content):
        print("Email send")
        return jsonify({"success": "true"})
    
    def message_service(self, data):
        type = data.get("type")
        recipient = data.get("recipient")
        content =  data.get("content")

        if type == "SMS":
            response = self.send_sms(recipient, content)
        elif type == "Email":
            response = self.send_email(recipient, content)
        
        timestamp = datetime.now()
        status_code = response.status_code #message send status

        #store to db
        insert_data('message_status', ['status' , 'timestamp'],[status_code , timestamp])
        insert_data('messages', ['type', ' recipient', ' message_content', 'status_code'], 
                    [data.get("type"), data.get("recipient"), data.get("content"),status_code] )
        print("stored to db")
        return True
