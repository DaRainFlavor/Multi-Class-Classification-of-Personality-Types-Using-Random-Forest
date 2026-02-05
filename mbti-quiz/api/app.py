"""
Flask API for MBTI Personality Type Prediction
Uses trained XGBoost model to predict personality types from quiz answers
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

# Load the model and label encoder
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'xgb_model.joblib')
ENCODER_PATH = os.path.join(os.path.dirname(__file__), 'label_encoder.joblib')

model = None
label_encoder = None

def load_model():
    global model, label_encoder
    try:
        model = joblib.load(MODEL_PATH)
        label_encoder = joblib.load(ENCODER_PATH)
        print("Model and encoder loaded successfully!")
        print(f"Classes: {label_encoder.classes_}")
    except FileNotFoundError:
        print("Model not found! Run train_model.py first.")
        print(f"Expected model at: {MODEL_PATH}")
        print(f"Expected encoder at: {ENCODER_PATH}")


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
    if model is None or label_encoder is None:
        return jsonify({
            'error': 'Model not loaded. Run train_model.py first.'
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
        predicted_type = label_encoder.inverse_transform([prediction])[0]

        # Create probabilities dictionary
        prob_dict = {
            label_encoder.classes_[i]: float(probabilities[i])
            for i in range(len(label_encoder.classes_))
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
    if label_encoder is None:
        return jsonify({
            'types': ['INTJ', 'INTP', 'ENTJ', 'ENTP', 'INFJ', 'INFP', 'ENFJ', 'ENFP',
                     'ISTJ', 'ISFJ', 'ESTJ', 'ESFJ', 'ISTP', 'ISFP', 'ESTP', 'ESFP']
        })
    
    return jsonify({
        'types': list(label_encoder.classes_)
    })


if __name__ == '__main__':
    load_model()
    print("\n" + "="*50)
    print("MBTI Prediction API")
    print("="*50)
    print("Endpoints:")
    print("  GET  /health  - Health check")
    print("  POST /predict - Predict personality type")
    print("  GET  /types   - Get all personality types")
    print("="*50 + "\n")
    app.run(host='0.0.0.0', port=5000, debug=True)
