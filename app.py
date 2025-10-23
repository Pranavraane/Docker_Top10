from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "<h2>D06 Vulnerable App - Secret Leak</h2>Visit /secret to get secret."

@app.route('/secret')
def secret():
    secret_key = os.getenv('SECRET_KEY')
    return jsonify({"secret": secret_key})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
