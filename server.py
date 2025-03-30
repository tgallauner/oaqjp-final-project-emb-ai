from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

def main():
    pass

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    input_text = request.json.get('text', '')

    if not input_text:
        return 'ERROR: No input provided!', 400

    result = emotion_detector(input_text)

    # build message
    message = 'For the given statement, the system response is '
    for key, value in result.items():
        if key != 'dominant_emotion':
            message = message + f'\'{key}\': ' + str(value) + ', '
        else:
            message = message + '\b\b. The dominant emotion is ' + value + '.'

    return message


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
