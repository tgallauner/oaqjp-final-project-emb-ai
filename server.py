from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def render_index_page():
    return render_template('index.html')


@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    input_text = request.args.get('textToAnalyze', '')

    result = emotion_detector(input_text)

    # check for invalid response
    if result['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'

    # build message
    message = 'For the given statement, the system response is '
    first_key = True
    for key, value in result.items():
        if key != 'dominant_emotion':
            if not first_key:
                message = message + ', '
            message = message + f'\'{key}\': ' + str(value)
            first_key = False
        else:
            message = message + '. The dominant emotion is ' + value + '.'

    return message


if __name__ == '__main__':
    app.run(port=5000, debug=True)
