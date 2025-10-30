from flask import Flask, request
import logging
import os

app = Flask(__name__)

log_file = "/var/log/myapp/access.log"
logging.basicConfig(filename=log_file, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/')
def home():
    logging.info(f"Home page accessed from {request.remote_addr}")
    return "Welcome to the vulnerable app!"

@app.route('/danger')
def danger():
    logging.info(f"Log tampering attempt from {request.remote_addr}")
    # Vulnerable: attacker can delete the log file to erase evidence
    try:
        os.remove(log_file)
        return "Logs erased!"
    except Exception as e:
        return f"Failed to erase logs: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
