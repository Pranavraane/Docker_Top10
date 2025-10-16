from flask import Flask, request
import jinja2

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <h2>OWASP D05: Maintain Security Contexts</h2>
    <form method="POST" action="/vuln">
        <input type="text" name="payload" placeholder="Enter payload">
        <input type="submit" value="Run">
    </form>
    '''

@app.route('/vuln', methods=['POST'])
def vuln():
    data = request.form.get('payload')
    # Unescaped user input = SSTI vulnerability
    template = jinja2.Template(data)
    return template.render()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
