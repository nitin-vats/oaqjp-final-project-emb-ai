"""Flask application for emotion detection service."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotion():
    """Handle emotion detection requests and return analysis results.
    
    Returns:
        str or tuple: Error message or response with status code
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    return response, 200

@app.route("/")
def default():
    """Render the main index page.
    
    Returns:
        str: Rendered HTML template
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
