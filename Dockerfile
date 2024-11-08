# start by pulling the python image
FROM python:3.12

WORKDIR /messagingservice

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV PYTHONPATH="${PYTHONPATH}:/messagingservice"
EXPOSE 5000


# Define environment variable
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the Flask app
CMD ["flask", "run"]

