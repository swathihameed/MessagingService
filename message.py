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
        
            timestamp = datetime.now()
            status_code = 200 #message send status
            msg_id = 123

            query = f'''INSERT INTO message_status(status , timestamp) VALUES (?,?)'''
            DATA = [status_code, timestamp]
            sqlite_connection(query, DATA)
            query = ''' INSERT INTO messages(type, recipient, message_content, status_code) VALUES (?, ?, ?, ?)'''
            DATA = [data.get("type"), data.get("recipient"), data.get("content"),status_code] 
            sqlite_connection(query,DATA)
            print("stored to db")
        return True
