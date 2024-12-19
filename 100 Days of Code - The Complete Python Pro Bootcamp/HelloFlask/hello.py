from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return "<p>Hello, World</p>"

def make_bold(function):
    def wrapper(*args, **kwargs):
        return f'<b>{function()}</b>'
    return wrapper

def make_emphasis(function):
    def wrapper(*args, **kwargs):
        return f'<em>{function()}</em>'
    return wrapper

def make_underline(function):
    def wrapper(*args, **kwargs):
        return f'<u>{function()}</u>'
    return wrapper
@app.route('/bye')
@make_bold
@make_emphasis
@make_underline
def say_bye():
    return "Bye"

@app.route('/username/<name>')
def say_hello(name):
    return f"Hello, {name}!"

if __name__ == '__main__':
    app.run(debug=True)