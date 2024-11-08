import json  
import logging as logger

test_data = {
      "type": "SMS",
      "recipient": "+11234567890",
      "content": "Test message"
    }


def test_send_message(client):  
    response = client.post(  
        "/sendMessage", data=json.dumps(test_data), content_type="application/json"  
    )  
    assert response.status_code == 200
    create_response_json = json.loads(response.data)  
    assert create_response_json == {
      "type": "SMS",
      "recipient": "+11234567890",
      "content": "Test message"
    }

def test_send_message_missing_type(client):
    # Test with missing "type" field
    response = client.post('/sendMessage', json={
        "recipient": "test@example.com",
        "content": "Hello!"
    })
    assert response.status_code == 400
    assert response.json == {"error": "Invalid 'type'"}

def test_send_message_invalid_email(client):
    # Test with invalid email format
    response = client.post('/sendMessage', json={
        "type": "Email",
        "recipient": "invalid-email",
        "content": "Hello!"
    })
    print(response.text)
    assert response.status_code == 400
    assert response.json == {"error": "Email ID is not valid"}

def test_send_message_invalid_phone(client):
    # Test with invalid phone format
    response = client.post('/sendMessage', json={
        "type": "SMS",
        "recipient": "12345",
        "content": "Hello!"
    })
    assert response.status_code == 400
    assert response.json == {"error": "Phone Number is not valid"}

def test_send_message_valid_email(client):
    # Test with valid email message payload
    response = client.post('/sendMessage', json={
        "type": "Email",
        "recipient": "test@example.com",
        "content": "Hello!"
    })
    assert response.status_code == 200
    assert response.json == {
        "type": "Email",
        "recipient": "test@example.com",
        "content": "Hello!"
    }

def test_send_message_valid_sms(client):
    # Test with valid SMS message payload
    response = client.post('/sendMessage', json={
        "type": "SMS",
        "recipient": "123-456-7890",
        "content": "Hello!"
    })
    assert response.status_code == 200
    assert response.json == {
        "type": "SMS",
        "recipient": "123-456-7890",
        "content": "Hello!"
    }
    