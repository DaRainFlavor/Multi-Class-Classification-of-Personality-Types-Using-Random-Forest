"""
Create Fixed Data Splits for Reproducibility
==============================================

This script creates and saves fixed train/validation/test splits
so all models use exactly the same data.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Fixed random seed
RANDOM_STATE = 42
np.random.seed(RANDOM_STATE)

# Data splits
TEST_SIZE = 0.15      # 15% for test
VAL_SIZE = 0.176      # 15% of remaining 85% ≈ 15% of total

print("=" * 80)
print("CREATING FIXED DATA SPLITS FOR REPRODUCIBILITY")
print("=" * 80)

# Load data
print("\n[1] Loading data...")
df = pd.read_csv('16P_eda_cleaned.csv')
print(f"  -> Loaded {len(df):,} rows")

# Separate features and target
X = df.drop(columns=['Personality'])
y = df['Personality']

# Encode labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

print(f"\n[2] Creating splits with random_state={RANDOM_STATE}...")

# First split: 85% train+val, 15% test
X_temp, X_test, y_temp, y_test = train_test_split(
    X, y_encoded, 
    test_size=TEST_SIZE, 
    random_state=RANDOM_STATE, 
    stratify=y_encoded
)

# Second split: 70% train, 15% val
X_train, X_val, y_train, y_val = train_test_split(
    X_temp, y_temp, 
    test_size=VAL_SIZE, 
    random_state=RANDOM_STATE, 
    stratify=y_temp
)

print(f"  -> Training:   {len(X_train):,} samples ({len(X_train)/len(df)*100:.1f}%)")
print(f"  -> Validation: {len(X_val):,} samples ({len(X_val)/len(df)*100:.1f}%)")
print(f"  -> Test:       {len(X_test):,} samples ({len(X_test)/len(df)*100:.1f}%)")

# Save the indices
print(f"\n[3] Saving split indices...")
train_indices = X_train.index.tolist()
val_indices = X_val.index.tolist()
test_indices = X_test.index.tolist()

# Save to CSV
import json
splits = {
    'train_indices': train_indices,
    'val_indices': val_indices,
    'test_indices': test_indices,
    'random_state': RANDOM_STATE
}

with open('data_split_indices.json', 'w') as f:
    json.dump(splits, f)

print(f"  -> Saved: data_split_indices.json")

# Also save the actual split datasets
X_train.to_csv('X_train.csv', index=False)
X_val.to_csv('X_val.csv', index=False)
X_test.to_csv('X_test.csv', index=False)

pd.DataFrame({'y_train': y_train}).to_csv('y_train.csv', index=False)
pd.DataFrame({'y_val': y_val}).to_csv('y_val.csv', index=False)
pd.DataFrame({'y_test': y_test}).to_csv('y_test.csv', index=False)

print(f"  -> Saved: X_train.csv, X_val.csv, X_test.csv")
print(f"  -> Saved: y_train.csv, y_val.csv, y_test.csv")

print("\n" + "=" * 80)
print("✓ FIXED SPLITS CREATED SUCCESSFULLY")
print("=" * 80)
print("\nAll models should now use these saved splits for 100% reproducibility!")
