import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle
import os

print("Starting model training script...")

# --- 1. Load the Dataset ---
# This script assumes you have 'insurance.csv' in the 'amlis1' directory.
try:
    df = pd.read_csv('insurance.csv')
    print("Dataset 'insurance.csv' loaded successfully.")
except FileNotFoundError:
    print("\nError: 'insurance.csv' not found.")
    print("Please download the dataset from https://www.kaggle.com/datasets/mirichoi0218/insurance")
    print("And place it in the 'c:\\amlis1\\' directory.\n")
    exit()

# --- 2. Preprocess the Data ---
# Convert categorical columns to the same numeric format as your HTML form.
df['sex'] = df['sex'].map({'male': 0, 'female': 1})
df['smoker'] = df['smoker'].map({'no': 0, 'yes': 1})

# Note: The region mapping must match your index.html values exactly.
region_mapping = {'northwest': 0, 'northeast': 1, 'southeast': 2, 'southwest': 3}
df['region'] = df['region'].map(region_mapping)

print("Data preprocessing complete.")

# --- 3. Define Features (X) and Target (y) ---
# The feature order must match the order in your HTML form.
features = ['age', 'sex', 'bmi', 'smoker', 'children', 'region']
X = df[features]
y = df['charges']

# --- 4. Train the Model ---
print("Training the RandomForestRegressor model...")
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)
print("Model training complete.")

# --- 5. Save the Model ---
# The model will be saved inside the 'webapp' folder.
output_path = os.path.join('webapp', 'model.pkl')
with open(output_path, 'wb') as f:
    pickle.dump(model, f)

print(f"Model saved successfully to '{output_path}'")