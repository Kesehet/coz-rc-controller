from flask import Flask
from src import connection

app = Flask(__name__)

@app.route('/')
def home():
    return str(Connection("SubscriptionID", "ResourceGroup", "CustShortName", "RegionName", "VNetName", 12345))

@app.route('/myname/')
def name():
    return "My Name is RC-1"


@app.route('/getconnection/<name>')
def setname(name):
    return f"My name is {name}"




if __name__ == '__main__':
    app.run(debug=True)
