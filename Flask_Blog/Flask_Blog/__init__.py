from flask import Flask
from flask_sqlalchemy import SQLAlchemy # used to initialize database

app = Flask(__name__) # Creating 'app' variable and sending to instance of Flask 
app.config['SECRET_KEY'] = '66a01a439b51313a5dc57439a72ca3b2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from Flask_Blog import routes