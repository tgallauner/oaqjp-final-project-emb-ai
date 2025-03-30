"""Emotion detection app"""
import requests


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
            analysis = response.text
        else:
            print(f'An ERROR with status code {response.status_code} occured.')

    except Exception as e:
        print(f'An ERROR occured: {e}')

    # return the models feedback
    return analysis


if __name__ == '__main__':
    print(emotion_detector('I love this new technology.'))
