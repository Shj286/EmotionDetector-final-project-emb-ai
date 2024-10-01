import requests, json

def emotion_detector(text_to_analyze):
    URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input_json= { "raw_document": { "text": text_to_analyze } }

    response = requests.post(URL, headers=headers, json=input_json)

    response_dict = json.loads(response.text)
    
    # Extract emotions and their scores
    emotions = response_dict['emotion_predictions'][0]['emotion']
    
    # Initialize a dictionary to hold the emotions we're interested in
    emotion_scores = {
        'anger': 0.0,
        'disgust': 0.0,
        'fear': 0.0,
        'joy': 0.0,
        'sadness': 0.0
    }
    
    # Populate the emotion_scores with the actual scores
    for emotion in emotions:
        emotion_name = emotion['emotion']
        score = emotion['score']
        if emotion_name in emotion_scores:
            emotion_scores[emotion_name] = score
    
    # Determine the dominant emotion
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    emotion_scores['dominant_emotion'] = dominant_emotion
    
    return emotion_scores
