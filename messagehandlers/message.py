from helpers.storage import *
from datetime import datetime
import os
from dotenv import load_dotenv
from .message_channels import ChannelType
load_dotenv()

class Message:

    def __init__(self):
        self.channel_type = ChannelType()

    def message_service(self, data):
        message_type = data.get("type")
        recipient = data.get("recipient")
        content = data.get("content")

        # Get the appropriate channel handler from the factory
        channel = self.channel_type.get_channel(message_type)

        # Send the message using the appropriate channel
        response = channel.send_message(recipient, content)

        timestamp = datetime.now()
        status_code = response.status_code  # Message send status

        # Store to the database
        db_path = os.getenv("sqlite_db_file")
        insert_data(db_path, 'message_status', ['status', 'timestamp'], [status_code, timestamp])
        insert_data(db_path, 'messages', ['type', 'recipient', 'message_content', 'status_code'], 
                    [message_type, recipient, content, status_code])
        
        print("Stored to DB")
        return response
