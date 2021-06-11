from flask import Flask
import random

app = Flask(__name__)

NUM = random.randint(1,10)

@app.route('/')
def number():
    return '<h1>Guess a number from 1 to 10 <h1> \
        <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route('/<int:guess>')
def answer(guess):
    if guess == NUM:
        return f"{NUM} is correct" + '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    if guess > NUM:
        return "Too high!" + '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    else:
        return "Too low!" + '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'

if __name__ == '__main__':
    app.run(debug=True)