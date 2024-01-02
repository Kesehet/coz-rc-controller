from flask import Flask
from src.database import DB
from src.connection import Connection


app = Flask(__name__)

ConnectionDB = DB("connection_db.json")

@app.route('/')
def home():
    conn = Connection("SubscriptionID", "ResourceGroup", "CustShortName", "RegionName", "VNetName", 12345)
    conn.set_public_ip_address("192.169.1.1")
    ConnectionDB.insert_row(conn.getConnection())
    return conn.get_public_ip_address()

@app.route('/myname/')
def name():
    return "My Name is RC-1"


@app.route('/getconnection/<name>')
def setname(name):
    return f"My name is {name}"




if __name__ == '__main__':
    app.run(debug=True)
