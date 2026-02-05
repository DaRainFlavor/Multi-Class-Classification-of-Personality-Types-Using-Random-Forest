import joblib
import numpy as np
from onnxmltools.convert import convert_xgboost
from onnxmltools.convert.common.data_types import FloatTensorType

# Load model
try:
    print("Loading XGBoost model...")
    model = joblib.load('mbti-quiz/api/xgb_model.joblib')
    # Rename features to generic f0, f1... to match ONNX expectation
    model.get_booster().feature_names = [f'f{i}' for i in range(60)]
    print("Model loaded and features renamed.")
except Exception as e:
    print(f"Error loading model: {e}")
    exit(1)

# Define initial types (60 floats)
# The input name 'float_input' can be anything, but we'll use 'input' for clarity
initial_type = [('input', FloatTensorType([None, 60]))]

# Convert
print("Converting to ONNX...")
onnx_model = convert_xgboost(model, initial_types=initial_type)
print("Conversion complete.")

# Save
output_path = "mbti-quiz/api/mbti_model.onnx"
with open(output_path, "wb") as f:
    f.write(onnx_model.SerializeToString())

print(f"Model saved to {output_path}")
