# app.py
from flask import Flask, render_template
import requests
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/')
def index():
    response = requests.get('http://localhost:8000/api/tokens')
    tokens = response.json()
    enumerated_tokens = list(enumerate(tokens, start=1))
    logging.info(f"Received data: {tokens[:2]}...")  # Log the first two tokens
    return render_template('index.html', enumerated_tokens=enumerated_tokens)
    
    

if __name__ == '__main__':
    app.run(debug=True, port=5000)