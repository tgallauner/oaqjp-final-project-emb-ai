"""Emotion detection app"""
import requests


def error_response():
    return {'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,} 


def emotion_detector(text_to_analyze):
    # define url, headers and payload
    url = r'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock'}
    payload = {'raw_document': {
        'text': text_to_analyze
    }}

    # feedback from the model
    analysis = None

    # perform request
    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            analysis = response.json()
        elif response.status_code == 400:
            return error_response()
        else:
            print(f'An ERROR with status code {response.status_code} occured.')
            return error_response()

    except Exception as e:
        print(f'An ERROR occured: {e}')
        return error_response()

    # extract required set of emotions
    analysis = analysis['emotionPredictions'][0]['emotion']

    # identify dominant emotion
    max_rating = 0
    dominant_emotion = ""

    for key, value in analysis.items():
        if value > max_rating:
            max_rating = value
            dominant_emotion = key
    analysis['dominant_emotion'] = dominant_emotion

    # return the models feedback
    return analysis


if __name__ == '__main__':
    print(emotion_detector('I love this new technology.'))
