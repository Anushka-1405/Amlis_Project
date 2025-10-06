# Web Application for Medical Insurance Charge Prediction

This web application allows users to predict medical insurance charges based on various input parameters such as age, sex, BMI, smoker status, number of children, and region.

## Project Structure

The project consists of the following files:

- **app.py**: The main entry point for the web application. It sets up a Flask server, handles routing, and integrates the prediction model for medical insurance charges.
- **templates/index.html**: The HTML structure for the web application's main page. It includes a form for user input and displays the predicted charges.
- **static/style.css**: The CSS styles for the web application, enhancing the user interface.

## Requirements

To run this application, you need to have the following installed:

- Python 3.x
- Flask
- scikit-learn
- pandas
- numpy
- pickle

You can install Flask using pip:

```
pip install Flask
```

## Running the Application

1. Navigate to the `webapp` directory:
   ```
   cd amlis/webapp
   ```

2. Run the application:
   ```
   python app.py
   ```

3. Open your web browser and go to `http://localhost:5000` to access the application.

## Usage

- Fill in the form with the required parameters.
- Click the "Predict" button to see the predicted medical insurance charges based on your input.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.