from flask import Flask
from src.database import DB
from src.connection import Connection


app = Flask(__name__)

ConnectionDB = DB("connection_db.json")
Config = DB("config_db.json")




@app.route('/')
def home():
    
    return Config.data






@app.route('/myname/')
def name():
    return "My Name is RC-1"


@app.route('/getconnection/<name>')
def setname(name):
    return f"My name is {name}"





def apiRoute(route):
    return "/api/" + route


if __name__ == '__main__':
    app.run(debug=True)
