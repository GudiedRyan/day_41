from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper_function(*args):
        return "<b>" + function() + "</b>"
    return wrapper_function

def make_emph(function):
    def wrapper():
        return "<emph>" + function() + "</emph>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route('/')
@make_bold
@make_emph
@make_underlined
def hello_world():
    return 'Hello world!'

@app.route('/bye')
def bye():
    return '<iframe src="https://giphy.com/embed/ICOgUNjpvO0PC" width="480" height="359" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/cat-humour-funny-ICOgUNjpvO0PC">via GIPHY</a></p>'

@app.route('/<string:name>')
def greet(name):
    return f"Hello {name.capitalize()}"

if __name__ == '__main__':
    app.run(debug=True)