'''importing'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

'''routing'''
@app.route("/emotionDetector")
def emo_detector():
    '''function1'''
    text_to_analyze = request.args.get('textToAnalyze')
    dominant_emotion = emotion_detector(text_to_analyze)
    if dominant_emotion is None:
        return "Invalid text! Please try again."
    return f"For the given statement, the system response is {dominant_emotion}."

@app.route("/")
def render_index_page():
    '''function2'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
