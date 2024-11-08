import pytest
from helpers.validate import Validate

validate = Validate()

def test_validate_email():
    assert validate.validate_email("test@example.com") == True
    assert validate.validate_email("invalid-email") == False
    assert validate.validate_email("12345@example.com") == True

def test_validate_phone():
    assert validate.validate_phone("123-456-7890") == True
    assert validate.validate_phone("+1 (123) 456-7890") == True
    assert validate.validate_phone("12345") == False

def test_validate_payload_missing_param():
    data = {
        "recipient": "test@example.com",
        "content": "Hello!"
    }
    result = validate.validate_payload(data)
    assert result == {"error": "Invalid 'type'"}

def test_validate_payload_invalid_type():
    data = {
        "type": "InvalidType",
        "recipient": "test@example.com",
        "content": "Hello!"
    }
    result = validate.validate_payload(data)
    assert result == {"error": "Invalid 'type' property"}

def test_validate_payload_valid():
    data = {
        "type": "Email",
        "recipient": "test@example.com",
        "content": "Hello!"
    }
    assert validate.validate_payload(data) == True
