from flask import Flask, render_template, request, redirect, url_for, session
import joblib
from feature_extraction import extract_features
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Load model
model = joblib.load('phishing_model.pkl')

@app.route('/')
def home():
    return redirect(url_for('check_url'))

@app.route('/check', methods=['GET', 'POST'])
def check_url():
    if request.method == 'POST':
        url = request.form['url']
        features = extract_features(url)
        prediction = model.predict([features])[0]
        result = 'Phishing' if prediction == 1 else 'Legitimate'
        
        # Store in session history
        if 'history' not in session:
            session['history'] = []
        session['history'].append({'url': url, 'result': result})
        session.modified = True
        
        return render_template('result.html', url=url, result=result)
    return render_template('check.html')

@app.route('/history')
def history():
    checks = session.get('history', [])
    return render_template('history.html', checks=checks)

if __name__ == '__main__':
    app.run(debug=True)