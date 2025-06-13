import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    payload = { "raw_document": { "text": text_to_analyze } } 
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = payload, headers=header)
    json_response = json.loads(response.text)
    emotion_aggregated = {}

    if response.status_code == 200:
        emotion_aggregated = json_response['emotionPredictions'][0]['emotion']
        max_score = 0
        dominant_emotion = ""
        for emotion, score in emotion_aggregated.items():
            if score > max_score:
                max_score = score
                dominant_emotion = emotion
        emotion_aggregated["dominant_emotion"] = dominant_emotion
    elif response.status_code == 400:
        emotion_aggregated = {
            "anger": None,
            "disgust": None,
            "dominant_emotion": None,
            "fear": None,
            "joy": None,
            "sadness": None
        }
    return emotion_aggregated