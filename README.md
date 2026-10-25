cat > README.md <<'EOF'
# Final project

## Emotion Detection Application

This project detects the five main emotions in text using the Skills Network
Watson NLP EmotionPredict service.

### Features
- Detects anger, disgust, fear, joy, and sadness.
- Identifies the dominant emotion.
- Provides a Flask web interface.
- Handles empty or invalid input.
- Includes automated unit tests.

### Technology
- Python
- Flask
- Requests
- Watson NLP EmotionPredict API
- unittest

### Run the application
python3 server.py

Launch port 5000 using the Skills Network Cloud IDE.

### Run unit tests
python3 -m unittest -v test_emotion_detection.py

### Package
EmotionDetection
EOF