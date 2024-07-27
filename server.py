''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emotion_detection():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    if text_to_analyze == '':
        return "Enter text to Analyze"

    response = emotion_detector(text_to_analyze)

    if response['anger'] is None:
        return "Invalid input ! Try again."

    return (
    f"For the given statement, the system response is \n"
    f"'anger': {response['anger']}, \n"
    f"'disgust': {response['disgust']}, \n"
    f"'fear': {response['fear']}, \n"
    f"'joy': {response['joy']} and \n"
    f"'sadness': {response['sadness']}. \n"
    f"The dominant emotion is <b>{response['dominant_emotion']}</b>."
    )



@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(host="0.0.0.0", port=5001)
