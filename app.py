from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def info():
    # Exposes environment variables publicly, potentially leaking secrets
    return "Environment variables: " + str(dict(os.environ))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
