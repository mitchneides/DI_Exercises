from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/lifetime/<int:year>/<int:month>/<int:day>')
def lifetime(year,month,day):
    birth_date = datetime.datetime(year,month,day)
    current_date = datetime.datetime.today()
    diff = current_date - birth_date
    minutes = int(diff.total_seconds())
    return f"You've lived for a total of {str(minutes)} minutes, but who's counting?"



if __name__ == "__main__":
    app.run(debug=True)