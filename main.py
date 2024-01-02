from flask import Flask

app = Flask(__name__)

@app.route('/myname/')
def home():
    return "My Name is RC Number 1"

if __name__ == '__main__':
    app.run(debug=True)
