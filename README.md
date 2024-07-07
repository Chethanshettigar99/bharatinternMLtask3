# Iris flower Classification
This Flask application hosts a web interface for predicting the class of an iris flower based on its sepal and petal measurements. The app uses a pre-trained machine learning model saved in a pickle file to make predictions.

Key points of this code include:

Model Loading: The model is loaded from a file named saved_model.sav using Python's pickle module.

Label Mapping: Numerical predictions are mapped to class names ('setosa', 'versicolor', 'virginica') for easier interpretation.

Form Handling: The home route initializes an empty form and the predict route processes form inputs, converts them to floats, and makes predictions.

Error Handling: If an exception occurs during prediction, the error message is displayed to the user.

Templates: The index.html template displays the form and prediction results, with form_values ensuring that user inputs persist across submissions.
