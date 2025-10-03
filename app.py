from flask import Flask, request, render_template_string
import subprocess

app = Flask(__name__)

# Existing vulnerable command execution route (RCE)
@app.route('/run_command', methods=['POST'])
def run_command():
    cmd = request.form.get('cmd', '')
    output = subprocess.getoutput(cmd)
    return f"<pre>{output}</pre>"

# New vulnerable SSTI route (D03 exploit)
@app.route('/ssti')
def ssti():
    name = request.args.get('name', 'User')
    # Unsafe rendering of user input in template string - vulnerable to SSTI
    template = f"Hello {name}!"
    return render_template_string(template)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
