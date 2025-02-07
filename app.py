from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict')
def precd():
    return render_template('predict.html')    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
    
