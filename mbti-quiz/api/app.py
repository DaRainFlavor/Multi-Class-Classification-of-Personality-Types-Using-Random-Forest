"""
Flask API for MBTI Personality Type Prediction
Uses trained XGBoost model to predict personality types from quiz answers
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import numpy as np
import os
import joblib

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

# Load the model and label encoder
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'xgb_model.joblib')
LABELS_PATH = os.path.join(os.path.dirname(__file__), 'labels.json')

model = None
class_labels = None

def load_model():
    global model, class_labels
    try:
        model = joblib.load(MODEL_PATH)
        with open(LABELS_PATH, 'r') as f:
            class_labels = json.load(f)
        print("Model and labels loaded successfully!")
        print(f"Classes: {class_labels}")
    except FileNotFoundError:
        print("Model or labels not found!")
        print(f"Expected model at: {MODEL_PATH}")
        print(f"Expected labels at: {LABELS_PATH}")

# Load model immediately when module is imported
load_model()


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': model is not None
    })


@app.route('/predict', methods=['POST'])
def predict():
    """Predict MBTI personality type from quiz answers"""
    if model is None or class_labels is None:
        return jsonify({
            'error': 'Model not loaded.'
        }), 500

    try:
        data = request.get_json()
        answers = data.get('answers', [])

        if len(answers) != 60:
            return jsonify({
                'error': f'Expected 60 answers, got {len(answers)}'
            }), 400

        # Convert answers to numpy array
        X = np.array(answers).reshape(1, -1)

        # Get prediction and probabilities
        prediction = model.predict(X)[0]
        probabilities = model.predict_proba(X)[0]

        # Decode predicted class
        # simple index lookup since we have a list of strings
        predicted_type = class_labels[int(prediction)]

        # Create probabilities dictionary
        prob_dict = {
            class_labels[i]: float(probabilities[i])
            for i in range(len(class_labels))
        }

        # Get confidence (max probability)
        confidence = float(np.max(probabilities))

        return jsonify({
            'predicted_type': predicted_type,
            'confidence': confidence,
            'probabilities': prob_dict
        })

    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500


@app.route('/types', methods=['GET'])
def get_types():
    """Get all possible personality types"""
    if class_labels is None:
        # Fallback if not loaded, though load_model() is called at module level
        return jsonify({
            'types': ['INTJ', 'INTP', 'ENTJ', 'ENTP', 'INFJ', 'INFP', 'ENFJ', 'ENFP',
                     'ISTJ', 'ISFJ', 'ESTJ', 'ESFJ', 'ISTP', 'ISFP', 'ESTP', 'ESFP']
        })
    
    return jsonify({
        'types': class_labels
    })


if __name__ == '__main__':
    # load_model() is already called at module level
    print("\n" + "="*50)
    print("MBTI Prediction API")
    print("="*50)
    print("Endpoints:")
    print("  GET  /health  - Health check")
    print("  POST /predict - Predict personality type")
    print("  GET  /types   - Get all personality types")
    print("="*50 + "\n")
    app.run(host='0.0.0.0', port=5000, debug=True)
