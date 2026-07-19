"""
Emotion Detection Module

This module provides functions to detect emotions from text using IBM Watson NLP API.
"""

import json
import requests

def emotion_detector(text_to_analyze):
    """
    Send text to Watson NLP API and return raw JSON response.

    Args:
        text_to_analyze (str): The text to analyze.

    Returns:
        dict: Raw JSON response from API, or a dict with None values if status 400.
    """
    url = (
        'https://sn-watson-emotion.labs.skills.network/'
        'v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, json=input_json, headers=header, timeout=10)

    if response.status_code == 200:
        return json.loads(response.text)

    # Status code 400 or other errors return None dict
    return {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }

def emotion_predictor(detected_text):
    """
    Parse raw emotion response and extract emotion scores.

    Args:
        detected_text (dict): Raw JSON response from emotion_detector.

    Returns:
        dict: Formatted emotions with dominant emotion.
    """
    if not detected_text or 'emotionPredictions' not in detected_text:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    emotions = detected_text['emotionPredictions'][0]['emotion']
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }
