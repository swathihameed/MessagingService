from flask import Flask, jsonify, request
from helpers.validate import Validate
from helpers.storage import * 
from messagehandlers.message import Message

app = Flask(__name__)
validate = Validate()
message = Message()

def configure():
    configure_db("sqlite")
    #configure env vars

@app.route('/sendMessage', methods=['POST'])
def send_message():
    data = request.get_json()
    validation = validate.validate_payload(data)
    if validation != True:
        return jsonify(validation), 400
    
    #validation passed. Now send message
    # function to send_message()
    if data.get("type") == "SMS":
        message.message_service(data)
        pass
    
    return jsonify(data)

@app.route('/viewData', methods=['GET'])
def view_data():
    db_path = os.getenv("sqlite_db_file")
    messages = get_all_data(db_path,'messages')
    message_status = get_all_data(db_path,'message_status')
    # Return both tables' data in JSON format
    return jsonify({
        "messages": messages,
        "message_status": message_status
    })

if __name__ == '__main__':
    configure()
    app.run(debug=True,port=5000)
