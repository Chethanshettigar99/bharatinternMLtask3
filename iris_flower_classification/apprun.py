from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the model
model = pickle.load(open('saved_model.sav', 'rb'))

# Define the mapping from numerical labels to class names
label_mapping = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}

@app.route('/')
def home():
    result = ''
    # Initialize form values to empty strings
    form_values = {'sepal_length': '', 'sepal_width': '', 'petal_length': '', 'petal_width': ''}
    return render_template('index.html', form_values=form_values, result=result)

@app.route('/predict', methods=['POST'])
def predict():
    form_values = {
        'sepal_length': request.form['sepal_length'],
        'sepal_width': request.form['sepal_width'],
        'petal_length': request.form['petal_length'],
        'petal_width': request.form['petal_width']
    }

    try:
        # Convert inputs to float for prediction
        features = [float(form_values['sepal_length']), float(form_values['sepal_width']), float(form_values['petal_length']), float(form_values['petal_width'])]

        # Predict using the model
        prediction = model.predict([features])[0]

        # Map the prediction to the class name
        result = label_mapping[prediction]

    except Exception as e:
        result = str(e)

    return render_template('index.html', form_values=form_values, result=result)

if __name__ == '__main__':
    app.run(debug=True)
