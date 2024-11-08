# MessagingService

A simple messaging service API built using Flask that supports sending and validating messages. The service stores data using SQLite and includes automated testing and a CI/CD pipeline with GitHub Actions.

## Stack

- **Python**: Core programming language.
- **Flask**: Web framework for building the API.
- **SQLite**: Database for storing messages.
- **Pytest**: Testing framework.
- **Docker**: Containerization for deployment.
- **GitHub Actions**: CI/CD pipeline.

## Setup and Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/swathihameed/MessagingService.git
   cd messagingservice
   ```

2. Install the required dependencies:
   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```
3. Set up environment variables. You can create a .env file in the root directory:
   ```env
   FLASK_ENV=development
   DATABASE=sqlite
   sqlite_db_file=db.sqlite3
   ```

### Running the Application
   To run the Flask application locally, use the following command:
   ```bash
   flask run
   ```
   The application will be available at http://127.0.0.1:5000.


### API Endpoints
POST ```/sendMessage```
Description: Sends a message (SMS or Email).

Request Body:
```json
{
  "type": "SMS",
  "recipient": "+11234567890",
  "content": "Hello World!"
}
```
Response:
```json
{
  "type": "SMS",
  "recipient": "+11234567890",
  "content": "Hello World!"
}
```
GET ```/viewData```
Description: Retrieves all messages and their status from the database.

Response:
```json

{
  "messages": [
    [1, "SMS", "+11234567890", "Hello World!", "200", "timestamp"]
  ],
  "message_status": [
    [1, "200", "timestamp"]
  ]
}
```

### Testing
To run the tests using pytest, execute the following command:

```bash

pytest tests/
```
The tests will validate the API endpoints and the helper functions.

### Docker Deployment
1. Build the Docker image:

```bash

docker build -t messagingservice .
```

2. Run the Docker container:
```bash
docker run -p 5000:5000 --env sqlite_db_file=<DB_NAME>  messagingservice
```
The application will be accessible at http://localhost:5000.

### CI/CD with GitHub Actions
The project includes a GitHub Actions workflow for automated testing, building, and deploying the Docker image.

#### GitHub Actions Workflow
The workflow consists of the following jobs:
 - build-and-test: Sets up the Python environment, installs dependencies, and runs tests.
 - docker-deploy: Builds and pushes the Docker image to DockerHub.
 - Environment Variables in GitHub Settings

You need to add the following environment variables in GitHub repository settings under Settings > Secrets and variables > Actions:

DOCKER_USERNAME: Your DockerHub username.
DOCKER_PASSWORD: Your DockerHub password.

### To Do:
- Deploy to GCP
- Refactor the message handling logic to support additional channels
- Add twilio and sendgrid integration
