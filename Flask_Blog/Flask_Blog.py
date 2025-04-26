from flask import Flask, render_template, url_for, flash, redirect;
from forms import RegistrationForm, LoginForm

app = Flask(__name__) # Creating 'app' variable and sending to instance of Flask 

app.config['SECRET_KEY'] = '66a01a439b51313a5dc57439a72ca3b2'

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