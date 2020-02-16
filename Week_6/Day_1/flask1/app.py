from flask import Flask
from Week_6.Day_1.flask1 import pizza
from flask import request
from flask import render_template, render_template_string

#create Flask App
app = Flask(__name__)

#Routes
@app.route('/')
def hello_world():
    return 'Hello, Mitch!'

# @app.route('/home')
# def home():
#     return """<h1 style='color: red;'>Welcome Home</h1>
#                 <p>This is para1</p>
#                 <p>This is para2</p>"""

@app.route('/home', defaults={'name': 'Stranger'})
@app.route('/home/<string:name>')
def home(name):
    html = f"<h1 style='color: red;'>Welcome {name}</h1>"
    return html

@app.route('/pizza/<int:size>/<string:top1>/<string:top2>')
def pizza1(size, top1, top2):
    return pizza.make_pizza(size, top1, top2)

@app.route('/custompizza/<path:args>')
def order_custom_pizza(args):
    args = args.split("/")
    return pizza.make_pizza(args[0], *args[1:])

@app.route('/getpizza', methods=['GET'])
# /getpizza?size=10&topping1=olives ... etc
def get_pizza():
    size = request.args.get('size')
    top1 = request.args.get('top1')
    top2 = request.args.get('top2')
    top3 = request.args.get('top3')
    return pizza.make_pizza(size, top1, top2, top3)

@app.route('/menu', defaults={'username': 'Stranger'})
@app.route('/menu/<string:username>')
def menu(username):
    html = render_template('menu.html',name=username, items=['apples','bananas','pears'])
    return html



#Start the app
if __name__ == "__main__":
    app.run(debug=True)