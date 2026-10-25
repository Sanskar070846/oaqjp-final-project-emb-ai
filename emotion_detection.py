import requests


def emotion_detector(text_to_analyze):
    """Detect emotions in text using the Watson NLP service."""

    empty_result = {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None
    }

    if not isinstance(text_to_analyze, str) or not text_to_analyze.strip():
        return empty_result

    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    headers = {
        "grpc-metadata-mm-model-id":
        "emotion_aggregated-workflow_lang_en_stock"
    }

    payload = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(
            url, json=payload, headers=headers, timeout=30
        )

        if response.status_code == 400:
            return empty_result

        response.raise_for_status()
        data = response.json()
        emotions = data["emotionPredictions"][0]["emotion"]

        scores = {
            "anger": emotions["anger"],
            "disgust": emotions["disgust"],
            "fear": emotions["fear"],
            "joy": emotions["joy"],
            "sadness": emotions["sadness"]
        }

        scores["dominant_emotion"] = max(scores, key=scores.get)
        return scores

    except (requests.RequestException, KeyError, IndexError, ValueError):
        return empty_result


def format_emotion_output(result):
    """Format emotion scores and dominant emotion for display."""

    if not result or result.get("dominant_emotion") is None:
        return "Unable to detect emotions. Please provide valid text."

    return (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']}, "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )