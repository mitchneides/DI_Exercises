from flask import Flask
from datetime import date

app = Flask(__name__)

@app.route('/lifetime/<int:year>/<int:month>/<int:day>')
def lifetime(year,month,day):
    birth_date = date(year,month,day)
    current_date = date.today()
    diff = current_date - birth_date
    minutes = int(diff.total_seconds())
    return f"You've lived for a total of {str(minutes)} minutes, but who's counting?"



if __name__ == "__main__":
    app.run(debug=True)