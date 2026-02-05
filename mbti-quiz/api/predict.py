"""
Vercel Serverless Function for MBTI Prediction
This is the Vercel-compatible API endpoint
"""

from http.server import BaseHTTPRequestHandler
import json
import os
import sys

# Add the api directory to the path
sys.path.insert(0, os.path.dirname(__file__))

import joblib
import numpy as np

# Model paths (relative to this file)
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'xgb_model.joblib')
ENCODER_PATH = os.path.join(os.path.dirname(__file__), 'label_encoder.joblib')

# Load model at module level for better performance
model = None
label_encoder = None

try:
    model = joblib.load(MODEL_PATH)
    label_encoder = joblib.load(ENCODER_PATH)
except FileNotFoundError:
    print(f"Warning: Model files not found at {MODEL_PATH}")


class handler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        """Handle CORS preflight"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_POST(self):
        """Handle prediction requests"""
        # Set CORS headers
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        if model is None or label_encoder is None:
            response = {'error': 'Model not loaded'}
            self.wfile.write(json.dumps(response).encode())
            return

        try:
            # Read request body
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length)
            data = json.loads(body)
            
            answers = data.get('answers', [])

            if len(answers) != 60:
                response = {'error': f'Expected 60 answers, got {len(answers)}'}
                self.wfile.write(json.dumps(response).encode())
                return

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

            response = {
                'predicted_type': predicted_type,
                'confidence': confidence,
                'probabilities': prob_dict
            }

        except Exception as e:
            response = {'error': str(e)}

        self.wfile.write(json.dumps(response).encode())
