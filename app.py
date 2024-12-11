from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/user/<name>/<l_name>')
def user(name,l_name):
    return f'<h1>Hello, {name} {l_name}!</h1>'