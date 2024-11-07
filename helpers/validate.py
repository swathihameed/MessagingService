import re

required_payload_params = ["type", "recipient", "content"]
message_format = ["SMS", "Email"]

class Validate():
    #function to validate email address
    def validate_email(self,email):
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        print("Email regex",re.match(pattern, email),re.match(pattern, email) is not None)
        return re.match(pattern, email) is not None

    def validate_phone(self, phone):
        #pattern for US phone numbers
        pattern = re.compile(r'^(\+1|1)?\s*\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$')
        print("Phone regex",re.match(pattern, phone),re.match(pattern, phone) is not None)
        return re.match(pattern, phone) is not None
    
    def validate_payload(self, data):
        validation = True
        required_params = required_payload_params
        for param in required_params:
            if not data.get(param):
                return { "error": f"Invalid \'{param}\'" }

        validation = self.validate_type(data)
        if validation != True:
            return validation
        validation = self.validate_recipient(data)
        if validation != True:
            return validation
        # print(3)
        return validation

    def validate_type(self,data):
        if data.get("type") not in message_format:
            return { "error": f"Invalid \'type\' property" }
        return True

    def validate_recipient(self,data):
        type = data.get("type")
        recipient = data.get("recipient")
        if type == "Email":
            if not self.validate_email(recipient):
                return { "error": f"Email ID is not valid" }
        if type == "SMS":
            if not self.validate_phone(recipient):
                return { "error": f"Phone Number is not valid" }
        return True



# Sample US phone numbers to test
phone_numbers = [
    "123-456-7890",
    "(123) 456-7890",
    "123 456 7890",
    "123.456.7890",
    "+1 123-456-7890",
    "1 123-456-7890"
    "1234567890"
]