from EmotionDetection.emotion_detection import emotion_detector, emotion_predictor
import unittest
from unittest.mock import patch
import json

class TestEmotionDetection(unittest.TestCase):

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_emotion_predictor(self, mock_post):
        # Tạo response giả cho các cảm xúc khác nhau
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200

        # Test 1: joy
        mock_response.text = json.dumps({
            "emotionPredictions": [{
                "emotion": {"anger": 0.1, "disgust": 0.1, "fear": 0.1, "joy": 0.9, "sadness": 0.1}
            }]
        })
        mock_post.return_value = mock_response
        result = emotion_predictor(emotion_detector("I am glad this happened"))
        self.assertEqual(result['dominant_emotion'], 'joy')

        # Test 2: anger
        mock_response.text = json.dumps({
            "emotionPredictions": [{
                "emotion": {"anger": 0.9, "disgust": 0.1, "fear": 0.1, "joy": 0.1, "sadness": 0.1}
            }]
        })
        mock_post.return_value = mock_response
        result = emotion_predictor(emotion_detector("I am really mad about this"))
        self.assertEqual(result['dominant_emotion'], 'anger')

        # Test 3: disgust
        mock_response.text = json.dumps({
            "emotionPredictions": [{
                "emotion": {"anger": 0.1, "disgust": 0.9, "fear": 0.1, "joy": 0.1, "sadness": 0.1}
            }]
        })
        mock_post.return_value = mock_response
        result = emotion_predictor(emotion_detector("I feel disgusted just hearing about this"))
        self.assertEqual(result['dominant_emotion'], 'disgust')

        # Test 4: sadness
        mock_response.text = json.dumps({
            "emotionPredictions": [{
                "emotion": {"anger": 0.1, "disgust": 0.1, "fear": 0.1, "joy": 0.1, "sadness": 0.9}
            }]
        })
        mock_post.return_value = mock_response
        result = emotion_predictor(emotion_detector("I am so sad about this"))
        self.assertEqual(result['dominant_emotion'], 'sadness')

        # Test 5: fear
        mock_response.text = json.dumps({
            "emotionPredictions": [{
                "emotion": {"anger": 0.1, "disgust": 0.1, "fear": 0.9, "joy": 0.1, "sadness": 0.1}
            }]
        })
        mock_post.return_value = mock_response
        result = emotion_predictor(emotion_detector("I am really afraid that this will happen"))
        self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()