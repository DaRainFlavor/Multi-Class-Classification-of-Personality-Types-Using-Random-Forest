"""
Train and save XGBoost model for MBTI prediction
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier
import joblib
import os

# Paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
DATA_PATH = os.path.join(PARENT_DIR, '16P_eda_cleaned.csv')
MODEL_PATH = os.path.join(SCRIPT_DIR, 'xgb_model.joblib')
ENCODER_PATH = os.path.join(SCRIPT_DIR, 'label_encoder.joblib')

# XGBoost parameters (same as the original training)
XGBOOST_PARAMS = {
    'n_estimators': 500,
    'learning_rate': 0.1,
    'max_depth': 6,
    'min_child_weight': 1,
    'subsample': 0.8,
    'colsample_bytree': 0.8,
    'objective': 'multi:softprob',
    'num_class': 16,
    'random_state': 42,
    'n_jobs': -1,
    'verbosity': 1
}


def train_model():
    print("="*50)
    print("Training XGBoost Model for MBTI Prediction")
    print("="*50)
    
    # Load data
    print(f"\nLoading data from: {DATA_PATH}")
    df = pd.read_csv(DATA_PATH)
    print(f"Dataset shape: {df.shape}")
    
    # Split features and target
    X = df.iloc[:, :-1]  # All columns except last
    y = df.iloc[:, -1]   # Last column (Personality)
    
    print(f"Features shape: {X.shape}")
    print(f"Target classes: {y.nunique()} unique types")
    print(f"Classes: {sorted(y.unique())}")
    
    # Encode labels
    print("\nEncoding labels...")
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)
    print(f"Label mapping: {dict(zip(label_encoder.classes_, range(len(label_encoder.classes_))))}")
    
    # Train model
    print("\nTraining XGBoost model...")
    print(f"Parameters: {XGBOOST_PARAMS}")
    
    model = XGBClassifier(**XGBOOST_PARAMS)
    model.fit(X, y_encoded)
    
    # Calculate training accuracy
    train_acc = model.score(X, y_encoded)
    print(f"\nTraining accuracy: {train_acc:.4f} ({train_acc*100:.2f}%)")
    
    # Save model and encoder
    print(f"\nSaving model to: {MODEL_PATH}")
    joblib.dump(model, MODEL_PATH)
    
    print(f"Saving label encoder to: {ENCODER_PATH}")
    joblib.dump(label_encoder, ENCODER_PATH)
    
    print("\n" + "="*50)
    print("Model training complete!")
    print("="*50)
    
    # Test prediction
    print("\nTesting prediction with first sample...")
    sample = X.iloc[0:1]
    pred = model.predict(sample)[0]
    proba = model.predict_proba(sample)[0]
    predicted_class = label_encoder.inverse_transform([pred])[0]
    actual_class = y.iloc[0]
    
    print(f"Actual: {actual_class}")
    print(f"Predicted: {predicted_class}")
    print(f"Confidence: {max(proba)*100:.2f}%")
    
    return model, label_encoder


if __name__ == '__main__':
    train_model()
