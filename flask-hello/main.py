
from flask import Flask

app = Flask(__name__)

@app.route('/message')
def greeting():
    return("Hello CSC330!")

@app.route('/add/<x>/<y>')
def add(x,y):
    return str(int(x)+int(y))

@app.route('/temperature/<city>')
def getTemp(city):
    return ""


@app.route('/<name>')
def sayHello(name):
    return(f"Hello {name}")


