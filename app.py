from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <h1>D07 Vulnerable Flask App</h1>
    <form method="post" action="/greet">
      Name: <input type="text" name="name">
      <input type="submit" value="Greet Me">
    </form>
    '''

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('name')
    # VULNERABLE: direct user input to template engine!
    template = f"Hello {name}!"
    return render_template_string(template)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
