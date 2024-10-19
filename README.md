# Repository for final project
AI Emotion Detector 🧠🎭

Project Overview

This repository contains the code and documentation for the AI Emotion Detector project. The project was developed as part of my IBM certification for Developing AI Applications with Python and Flask. The AI Emotion Detector uses Natural Language Processing (NLP) to analyze a given text and determine the emotions conveyed, such as joy, anger, sadness, and more.

Features

Emotion Detection API: Users can submit text to the API, and it will return a detailed analysis of the emotions present in the text.
Error Handling & Validation: The application incorporates robust error handling for invalid or blank inputs.
Unit Testing: Core functionalities are rigorously tested to ensure reliability and accuracy.
Lightweight Flask Server: The web server is built using Flask, which processes the text and provides the emotion analysis.
Watson NLP API Integration: IBM’s Watson Natural Language Processing API is used to detect emotions from the input text via RESTful API calls.

Tools & Technologies

Python: Used to develop the logic and structure of the application.
Flask: A micro web framework used to handle the web server and API endpoints.
REST API: Integrated the Watson NLP API using RESTful architecture to analyze text and extract emotions.
Requests Library: Employed to send HTTP requests to the Watson API for emotion analysis.
Git & GitHub: Version control was managed using Git, with the repository hosted on GitHub.
PyLint: Used for static code analysis to ensure code quality and adherence to Python standards.
Unit Testing: Implemented unit tests to validate the functionality and reliability of the core components.
Installation

To run this project locally, follow these steps:

Clone the repository:
git clone https://github.com/your-username/emotion-detector.git
cd emotion-detector

Create a virtual environment (optional but recommended):

python3 -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows

Install the dependencies:
pip install -r requirements.txt

Set up your API keys:
Ensure that you have the correct credentials for accessing the Watson NLP API. You can follow this guide to get API keys.

Run the Flask server:
python server.py
Access the application:
Open your browser and navigate to http://127.0.0.1:5000/ or http://localhost:5000/.

Usage

API Endpoint:
POST /emotionDetector: Submit text for emotion analysis.
Example Request:

json
{
    "text": "I am very happy today!"
}
Example Response:

json
{
    "anger": 0.01,
    "disgust": 0.02,
    "fear": 0.03,
    "joy": 0.92,
    "sadness": 0.02,
    "dominant_emotion": "joy"
}

Unit Testing

Unit tests are included to verify the correctness of the core functionalities. To run the tests, simply use:
pytest

Project Structure

emotion-detector/
│
├── static/                    # Static files (CSS, JS, images)
├── templates/                 # HTML files for Flask
├── EmotionDetection/           # Main application logic
│   ├── emotion_detection.py    # Emotion detector and predictor functions
├── server.py                  # Flask server
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation

Future Improvements

Add more advanced emotion categories by expanding the scope of the NLP model.
Implement a real-time streaming feature for continuous emotion detection in live conversations.
Deploy the application on cloud platforms such as Heroku or AWS.

License

This project is licensed under the MIT License - see the LICENSE file for details.
