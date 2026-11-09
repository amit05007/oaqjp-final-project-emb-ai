	
import requests
import json

def emotion_detector(text_to_analyze ):  
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header) 
    all_emotions = ""
    if response.status_code == 200:
        formatted_response =  json.loads(response.text)
        all_emotions = formatted_response["emotionPredictions"][0]["emotion"]
        dom_emotion = max(all_emotions, key =all_emotions.get)   
        all_emotions["dominant_emotion"] = dom_emotion
    elif response.status_code == 500:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    # For any other unexpected status codes, set label and score to None
    else:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }


    return all_emotions  

        
