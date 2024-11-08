import os
from flask import Flask, jsonify, request
from helpers.storage import configure_db, get_all_data
from helpers.validate import Validate
from messagehandlers.message import Message

app = Flask(__name__)
validate = Validate()
message = Message()


def configure():
    """Configure the database and environment variables."""
    configure_db("sqlite")


@app.route('/sendMessage', methods=['POST'])
def send_message():
    """
    Endpoint to handle message sending.

    Expects a JSON payload with 'type', 'recipient', and 'content'.
    Validates the payload and sends the message if validation passes.
    """
    data = request.get_json()
    validation = validate.validate_payload(data)

    if validation is not True:
        return jsonify(validation), 400

    # Validation passed, send the message
    message.message_service(data)
    return jsonify({"success": "true"})


@app.route('/viewData', methods=['GET'])
def view_data():
    """
    Endpoint to view stored data from 'messages' and 'message_status' tables.

    Fetches data from SQLite database and returns it in JSON format.
    """
    db_path = os.getenv("sqlite_db_file")
    messages = get_all_data(db_path, 'messages')
    message_status = get_all_data(db_path, 'message_status')

    return jsonify({
        "messages": messages,
        "message_status": message_status
    })


if __name__ == '__main__':
    configure()
    app.run(debug=True, port=5000)
