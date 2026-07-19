"""
Emotion Detection Module
This module provides functions to detect emotions from text using IBM Watson NLP API.
"""

import json
import requests

def emotion_detector(text_to_analyze):
    """
    Send text to Watson NLP API and return formatted emotion scores.

    Args:
        text_to_analyze (str): The text to analyze.

    Returns:
        dict: Formatted emotions with dominant emotion, or None values on error.
    """
    url = (
        'https://sn-watson-emotion.labs.skills.network/'
        'v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, json=input_json, headers=header, timeout=10)

    if response.status_code == 200:
        # Parse raw JSON
        raw_data = json.loads(response.text)
        # Extract emotions
        emotions = raw_data['emotionPredictions'][0]['emotion']
        anger = emotions['anger']
        disgust = emotions['disgust']
        fear = emotions['fear']
        joy = emotions['joy']
        sadness = emotions['sadness']
        dominant_emotion = max(emotions, key=emotions.get)
        # Return formatted dict
        return {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': dominant_emotion
        }
    else:
        # Return None values for error
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }