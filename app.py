from flask import Flask, render_template, request, jsonify
import random
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

# Dummy function for sentiment analysis (Replace with ML model)
def analyze_sentiment(message):
    sentiments = ["Positive 😊", "Negative 😞", "Neutral 😐"]
    return random.choice(sentiments)  # Returns a random sentiment

class TextTONum:
    def __init__(self, text):
        self.text = text
        self.cleaned_text = None
        self.tokens = None
        self.filtered_tokens = None
        self.stemmed_tokens = None
    
    def cleaner(self):
        self.cleaned_text = self.text.lower()
    
    def token(self):
        self.tokens = self.cleaned_text.split()
    
    def removeStop(self):
        stop_words = set(["is", "in", "at", "the", "a", "an", "and", "or", "to", "of"])
        self.filtered_tokens = [word for word in self.tokens if word not in stop_words]
    
    def stemmed(self):
        self.stemmed_tokens = [word[:-1] if word.endswith("ing") else word for word in self.filtered_tokens]
        return self.stemmed_tokens

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
        
        ob = TextTONum(msg)
        ob.cleaner()
        ob.token()
        ob.removeStop()
        st = ob.stemmed()
        
        with open("vectorizer.pickle", "rb") as vcfile:
            vc = pickle.load(vcfile)
        
        stvc = " ".join(st)
        data = vc.transform([stvc])
        
        with open("model.pickle", "rb") as modelfile:
            model = pickle.load(modelfile)
        
        pred = model.predict(data)
        return jsonify({"result": str(pred[0])})
    
    return render_template('predict.html', sentiment=sentiment)

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
