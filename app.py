import pickle
import numpy as np
from flask import Flask, request, render_template
import os

# Create a Flask web application
app = Flask(__name__)

# --- Get the absolute path to the directory of the current script ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'model.pkl')

# Load the trained machine learning model
# Make sure 'model.pkl' is in the same 'webapp' directory
try:
    model = pickle.load(open(MODEL_PATH, 'rb'))
except FileNotFoundError:
    print("Error: 'model.pkl' not found. Make sure the model file is in the 'webapp' directory.")
    model = None

# Define the route for the home page
@app.route('/')
def home():
    # Render the main page with the form
    return render_template('index.html', prediction=None)

# Define the route for handling the prediction
@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return "Model not loaded. Please check the server logs.", 500

    try:
        # Get data from the form by name to ensure correct order
        form_features = [
            float(request.form['age']),
            float(request.form['sex']),
            float(request.form['bmi']),
            float(request.form['smoker']),
            float(request.form['children']),
            float(request.form['region'])
        ]
        features = [np.array(form_features)]
        
        # Make a prediction using the loaded model
        prediction = model.predict(features)
        
        # Render the home page again, but this time with the prediction result
        return render_template('index.html', prediction=prediction[0])
    except (ValueError, KeyError) as e:
        # Handle cases where form data is missing or not a valid number
        error_message = f"Invalid input. Please check all fields. Error: {e}"
        return render_template('index.html', prediction=None, error=error_message), 400

# Run the app
if __name__ == "__main__":
    app.run(debug=True)