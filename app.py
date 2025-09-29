from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <form action="/greet" method="post">
        <input name="name" placeholder="Enter your name">
        <input type="submit">
    </form>
    '''

# Vulnerable SSTI endpoint
@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('name', '')
    # Dangerous: rendering untrusted input directly as template
    return render_template_string(f'Hello, {name}!')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
