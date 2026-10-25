"""Flask web application for emotion detection."""

from flask import Flask, render_template, request

from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def home():
    """Render the emotion detection interface."""
    return render_template("index.html")


@app.route("/emotionDetector")
def detect_emotion():
    """Analyze submitted text and return the emotion results."""
    text = request.args.get("textToAnalyze", "").strip()
    result = emotion_detector(text)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']}, "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
