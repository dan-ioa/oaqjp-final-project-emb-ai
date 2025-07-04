"""Flask server application for emotion detection."""

from typing import Dict, Any

from flask import Flask, request, jsonify

from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector", methods=["POST"])
def emotion_detector_endpoint() -> Any:
    """
    Endpoint to detect emotion from given text.

    Returns:
        JSON response with emotion scores and dominant emotion,
        or error message for invalid input.
    """
    input_data: Dict[str, Any] = request.get_json()

    if not input_data or "text" not in input_data:
        return jsonify({"error": "Missing 'text' field in request"}), 400

    text = input_data["text"]
    result = emotion_detector(text)

    if result.get("dominant_emotion") is None:
        return jsonify({"message": "Invalid text! Please try again!"}), 400

    description = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return description, 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
    