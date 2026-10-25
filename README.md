# Final Project: AI-Based Emotion Detection

## Project Overview
This project develops an AI-based emotion detection application that analyzes customer feedback and identifies emotions expressed in text using the Watson NLP library.

## Objectives
- Detect emotions in text.
- Identify anger, disgust, fear, joy, and sadness.
- Format the detected emotions into a structured response.
- Package the application as a reusable Python module.
- Perform unit testing.
- Deploy the application using Flask.
- Implement error handling and static code analysis.

## Technologies Used
- Python 3
- Watson NLP
- Flask
- Requests
- Unittest
- PyLint

## Project Structure
- `emotion_detection.py` — Emotion detection logic.
- `__init__.py` — Python package initialization.
- `test_emotion_detection.py` — Unit tests.
- `server.py` — Flask web application.
- `static/` — Static web resources.
- `templates/` — HTML templates.

## Execution
Install the required dependencies:

```bash
python3 -m pip install requests flask
```

Run the unit tests:

```bash
python3 test_emotion_detection.py
```

Start the Flask application:

```bash
python3 server.py
```

## Learning Outcomes
This project demonstrates Python application development, API integration, modular packaging, unit testing, web deployment, error handling, and static code analysis.
