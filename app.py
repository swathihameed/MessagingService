import json
from flask import Flask, jsonify, request
from helpers.validate import Validate
from helpers.storage import * 
from datetime import datetime
import psycopg2
from dotenv import load_dotenv
import os 


app = Flask(__name__)
validate = Validate()

load_dotenv()

@app.route('/sendMessage', methods=['POST'])
def send_message():
    data = request.get_json()
    validation = validate.validate_payload(data)
    if validation != True:
        return jsonify(validation), 400
    
    #validation passed. Now send message
    # function to send_message()
    if data.get("type") == "SMS":
        #send sms message
        pass
        # response
    
    #code to store to db
    timestamp = datetime.now()
    status_code = 200 #message send status
    msg_id = 123

    query = f'''INSERT INTO message_status(status , timestamp) VALUES (%s ,%s)'''
    DATA = [status_code, timestamp] 
    db_connection(query,DATA)
    print("stored to db")

    return data


if __name__ == '__main__':
    app.run(debug=True,port=5000)
