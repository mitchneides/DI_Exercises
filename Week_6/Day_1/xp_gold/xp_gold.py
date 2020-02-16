from flask import Flask
from datetime import date
import random

app = Flask(__name__)

@app.route('/countdown')
def countdown():
    target_date = date(2021,1,1)
    current_date = date.today()
    diff = target_date - current_date
    return f"Until 1/1/2020: {str(diff)}"

@app.route('/guess-num/<user_num>')
def guess_num(user_num):
    rand_num = random.randint(1,100)
    if int(user_num) == rand_num:
        return f"Wow! {user_num} was the right number!"
    else:
        return f"Nah, that's not the number."

@app.route('/birthday')
def bday_countdown():
    bday = date(2020,11,6)
    current_date = date.today()
    diff = bday - current_date
    return f"Days until bday: {str(diff)}"



if __name__ == "__main__":
    app.run(debug=True)