import json
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/sendMessage', methods=['POST'])
def send_message():
  data = request.get_json()
  print(type(data),data)
  if not data['type'] or data['type'] not in ('Email', 'SMS'):
    return jsonify({ 'error': 'Invalid properties.' }), 400
  return data

if __name__ == '__main__':
   app.run(port=5000)