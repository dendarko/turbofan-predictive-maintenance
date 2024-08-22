from flask import Flask, render_template, request, redirect, url_for
import joblib
import numpy as np
import os
from visualizations.visualization import plot_feature_importance, plot_predictions_vs_true

# Handle possible ImportError for url_quote
try:
    from werkzeug.urls import url_quote
except ImportError:
    from urllib.parse import quote as url_quote

app = Flask(__name__)

# Load models
model_paths = {
    'FD001': 'models/model_FD001.pkl',
    'FD002': 'models/model_FD002.pkl',
    'FD003': 'models/model_FD003.pkl',
    'FD004': 'models/model_FD004.pkl'
}
models = {key: joblib.load(model_paths[key]) for key in model_paths}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        dataset = request.form.get('dataset')
        # Process the features correctly
        features_str = request.form.get('feature')
        features = [float(x.strip()) for x in features_str.split(',') if x.strip()]
        
        if len(features) != 50:
            return "Error: Please enter exactly 50 features."

        prediction = predict(dataset, features)
        return redirect(url_for('result', dataset=dataset, prediction=prediction))
    return render_template('index.html')

def predict(dataset, features):
    model = models[dataset]
    prediction = model.predict([features])[0]

    # Generate visualizations
    feature_names = [f'Feature {i+1}' for i in range(len(features))]
    plot_feature_importance(model, feature_names, dataset)
    plot_predictions_vs_true([prediction], [prediction], dataset)

    return prediction

@app.route('/result')
def result():
    dataset = request.args.get('dataset')
    prediction = request.args.get('prediction')
    return render_template('result.html', dataset=dataset, prediction=prediction)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
