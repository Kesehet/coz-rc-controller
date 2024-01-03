from flask import Flask
from src.database import DB
from src.connection import Connection


app = Flask(__name__)

ConnectionDB = DB("connection_db.json")
Config = DB("config_db.json")


def apiRoute(route):
    return "/api/" + route


@app.route('/')
def home():

    return Config.get_saved_key("name")


@app.route(apiRoute("addconnection"))
def addconnection():

    conn = Connection("test", "test", "test").start()
    return "Connection Added"



@app.route('/myname/')
def name():
    return "My Name is RC-1"


@app.route('/getconnection/<name>')
def setname(name):
    return f"My name is {name}"







if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
