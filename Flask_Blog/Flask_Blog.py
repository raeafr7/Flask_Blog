from flask import Flask;
app = Flask(__name__) # Creating 'app' variable and sending to instance of Flask 

#__name__ is a python variable that is the name of the module

@app.route("/") # root page of our website
@app.route("/home")
def home():
    return "<h1>Home Page!</h1>"

@app.route("/about") # about page of our website
def about():
    return "<h1>About page</h1>"


if __name__ == '__main__': ## if running directly with python
    app.run(debug=True) 