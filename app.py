import json
from flask import Flask, jsonify, request
from helpers.validate import Validate

app = Flask(__name__)
validate = Validate()

@app.route('/sendMessage', methods=['POST'])
def send_message():
    data = request.get_json()
    validation = validate.validate_payload(data)
    if validation != True:
        return jsonify(validation), 400
    return data

if __name__ == '__main__':
    app.run(debug=True,port=5000)
