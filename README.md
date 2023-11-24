# Joke-App-Flask

# Dockerized Flask Joke App

This repository contains a simple Flask application that generates jokes using the `pyjokes` library and displays them via a web interface.

## Setup Instructions

### Prerequisites
- [Docker](https://www.docker.com/) installed on your machine

### Running the Application

1. **Clone the Repository:**

```
git clone https://github.com/EdagPSIT/Joke-App-Flask.git
cd Joke-App-Flask
'''
2. **Build the Docker Image:**
`docker build -t joke-web-app .`

3. **Run the Docker Container**
`docker run -d -p 5000:5000 joke-web-app`


4. **Access the Application:**
Open a web browser and go to `http://localhost:5000` to view the application.

### Application Details

- The Flask application is contained in `app.py`.
- HTML templates are stored in the `templates` directory.
- `requirements.txt` contains the necessary Python dependencies.
- The Dockerfile specifies the steps to build the Docker image.

## Application Usage

- **Home Page (`/`):** Displays a random joke fetched from the `pyjokes` library.
- **User Interaction:** Click on links to navigate to different pages.
- `/users`: Lists all users.
- `/user/<user_id>`: Displays details of a specific user.

## Folder Structure
jokeapp/
├── app.py
├── requirements.txt
├── Dockerfile
└── templates/
    |── index.html
