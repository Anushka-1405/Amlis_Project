import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle

# Load your data
data = pd.read_csv('insurance.csv')

# Convert categorical columns to numbers
data['sex'] = data['sex'].map({'male': 0, 'female': 1})
data['smoker'] = data['smoker'].map({'no': 0, 'yes': 1})
data['region'] = data['region'].map({'southwest': 0, 'southeast': 1, 'northwest': 2, 'northeast': 3})

# Prepare features and target
X = data[['age', 'sex', 'bmi', 'smoker', 'children', 'region']]
y = data['charges']

# Train the model
rf_tuned = RandomForestRegressor()
rf_tuned.fit(X, y)

# Save the trained model
with open('rf_tuned.pkl', 'wb') as f:
    pickle.dump(rf_tuned, f)