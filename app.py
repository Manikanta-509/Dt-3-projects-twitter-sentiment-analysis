from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Dummy function for sentiment analysis (Replace with ML model)
def analyze_sentiment(message):
    sentiments = ["Positive 😊", "Negative 😞", "Neutral 😐"]
    return random.choice(sentiments)  # Returns a random sentiment

# Home Page Route
@app.route('/')
def home():
    return render_template('index.html')

# Prediction Page Route
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    sentiment = None  # Default value
    if request.method == 'POST':
        msg = request.form.get('message')  # Get user input
        print("User input:", msg)  # Debugging in terminal
        sentiment = analyze_sentiment(msg)  # Perform sentiment analysis
    return render_template('predict.html', sentiment=sentiment)  

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)