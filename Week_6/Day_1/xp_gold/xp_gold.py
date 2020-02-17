from flask import Flask
import datetime
import random

app = Flask(__name__)

@app.route('/countdown')
def countdown():
    target_date = datetime.datetime(2021,1,1,1,1,1,1)
    current_date = datetime.datetime.now()
    diff = target_date - current_date
    return f"Until 1/1/2020: {diff}"

@app.route('/guess-num/<user_num>')
def guess_num(user_num):
    rand_num = random.randint(1,100)
    if int(user_num) == rand_num:
        return f"Wow! {user_num} was the right number!"
    else:
        return f"Nah, that's not the number."

@app.route('/birthday')
def bday_countdown():
    bday = datetime.datetime(2020,11,6,1,1,1,1)
    current_date = datetime.datetime.now()
    diff = bday - current_date
    return f"Days until bday: {diff}"



if __name__ == "__main__":
    app.run(debug=True)