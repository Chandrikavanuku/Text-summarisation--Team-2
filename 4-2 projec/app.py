import os
import joblib
import pickle
from flask import Flask, render_template, request, jsonify

# Use the .pyc file located in __pycache__
from __pycache__ import article_summarize

app = Flask(__name__)

# Load the model using pickle (you need to have the model saved as 'summarizes.pkl')
model_path = "summarizes.pkl"  # Update with correct path to your model

def load_model():
    try:
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
            print("Model loaded successfully.")
            return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

# Load the model when the application starts
model = load_model()

@app.route('/')
def index():
    return render_template('index.html')  # Make sure you have index.html in the templates folder

@app.route('/summarize', methods=['POST'])
def summarize_article():
    if request.method == 'POST':
        article_text = request.form['article']  # Assuming article is passed via a form in HTML
        
        # Check if the model is loaded correctly
        if model is None:
            return jsonify({'error': 'Model not loaded correctly.'})

        # Call the article_summarize function from the article_summarize module
        summaries = article_summarize.article_summarize(article_text)  # Ensure the function exists

        # Return the first summary as a JSON response
        return jsonify({'summary': summaries[0]})  # You can modify this part depending on the output format

if __name__ == '__main__':
    app.run(debug=True)
