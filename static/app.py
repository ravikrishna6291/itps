from flask import Flask


app = Flask(__name__)
@app.route("/")
def homepage():
    return "<h1>HEllo WorlD</h1>"
@app.route("/bye")
def downpage():
    return "<h1>Good Bye</h1>"

@app.route("/meet")
def uppage():
    return "<h1>I am comming</h1>"

if __name__ =="__main__":
    app.run(host='0.0.0.0',port=8080)

/flaskapplication# python3 app.py
