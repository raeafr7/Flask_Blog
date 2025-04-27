from flask import Flask, render_template, url_for, flash, redirect
from sqlalchemy import Nullable;
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__) # Creating 'app' variable and sending to instance of Flask 
app.config['SECRET_KEY'] = '66a01a439b51313a5dc57439a72ca3b2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model): # table name automatically set to 'user' (lowercase)
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    post = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model): # table name automatically set to 'post' (lowercase)
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

posts = [
    {
        'author': 'Raea Freund',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted':'April 26th, 2025'
     },
    {
        'author': 'Raea Freund',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted':'April 27th, 2025'
     }
]

@app.route("/") # root page of our website
@app.route("/home")
def home():
    return render_template('home.html', posts=posts); # whatever we name variable as arg name that we pass in, we will have access to that variable in our template and will be equal to post data

@app.route("/about") # about page of our website
def about():
    return render_template('about.html', title='About');

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home')) # home is the name of the function for that route
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__': ## if running directly with python
    app.run(debug=True) 