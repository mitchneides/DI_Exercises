from flask import Flask
from datetime import date
from Week_6.Day_1.exercises import multiply
from flask import render_template

app = Flask(__name__)


@app.route('/date')
def display_date():
    today = date.today()
    return f"Current date: {today}"


@app.route('/CV', defaults={'username': 'The Donald', 'picture': 'https://pmcdeadline2.files.wordpress.com/2019/10/shutterstock_editorial_10434333bm.jpg?crop=0px%2C0px%2C2903px%2C1627px&resize=681%2C383', 'hobbies': ['Wall building'],
                            'skills': ['Patience for hours in a spray tan booth'], 'strengths': ['Epidermal Fortitude'],
                            'weaknesses': ['Liberal Conspiracies']})
@app.route('/CV/<username>/<picture>/<hobbies>/<skills>/<strengths>/<weaknesses>')
def display_CV(username, picture, hobbies, skills, strengths, weaknesses):
    html = render_template('CV.html', name=username, pic=picture, hobbs=hobbies, sklls=skills, strongs=strengths, weaks=weaknesses)
    return html


if __name__ == "__main__":
    app.run(debug=True)
