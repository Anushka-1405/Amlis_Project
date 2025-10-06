# Medical Cost Prediction Project

This project implements a medical cost prediction model using machine learning techniques. The model predicts medical insurance charges based on various factors such as age, sex, BMI, smoking status, number of children, and region.

## Project Structure

- **Medical_Cost_Insurance_.ipynb**: Jupyter notebook containing the data analysis, model training, and evaluation.
- **insurance.csv**: Dataset used for training the prediction model.
- **rf_tuned.pkl**: Serialized Random Forest model used for making predictions.
- **webapp/**: Directory containing the web application files.
  - **app.py**: Main entry point for the web application, setting up the Flask server and handling predictions.
  - **templates/**: Contains HTML templates for the web application.
    - **index.html**: Main page of the web application with a form for user input and displaying predictions.
  - **static/**: Contains static files such as CSS.
    - **style.css**: Styles for the web application.

## Running the Web Application

1. Ensure you have Flask installed. You can install it using pip:
   ```
   pip install Flask
   ```

2. Navigate to the `webapp` directory:
   ```
   cd webapp
   ```

3. Run the application:
   ```
   python app.py
   ```

4. Open your web browser and go to `http://localhost:5000` to access the application.

## Usage

- Enter the required details in the form (age, sex, BMI, smoker status, number of children, and region).
- Click on the submit button to get the predicted medical insurance charges.

## Dependencies

- Flask
- pandas
- numpy
- scikit-learn
- seaborn
- matplotlib

Make sure to install all necessary dependencies before running the application.