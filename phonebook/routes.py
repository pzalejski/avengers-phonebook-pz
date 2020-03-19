from phonebook import app, db
from flask import render_template, redirect, request, flash, url_for

from phonebook.forms import RegistrationForm, LoginForm
from phonebook.models import User, check_password_hash

from flask_login import login_required, login_user, current_user, logout_user


@app.route("/")
def index():  # fucntions that are called in the url_for('')
    return render_template("home.html")


@app.route("/blackwidow")
def blackwidow():
    return render_template('blackwidow.html')


@app.route("/dr-strange")
def dr_strange():
    return render_template('dr_strange.html')


@app.route("/ironman")
def ironman():
    return render_template('ironman.html')


@app.route("/thor")
def thor():
    return render_template('thor.html')


@app.route("/hawkeye")
def hawkeye():
    return render_template('hawkeye.html')


@app.route('/captain-america')
def captain_america():
    return render_template('captain_america.html')


@app.route('/hulk')
def hulk():
    return render_template('hulk.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    # creates instance of the form
    if request.method =='POST' and form.validate():
        flash(f"Account created for {form.name.data}!", 'success')
        name = form.name.data
        address = form.address.data
        phone = form.phone.data
        print(name, address, phone)
        user = User(name, address, phone)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    else:
        flash('Invalid input', 'danger')
    return render_template('register.html', title='Register', form=form)


# login route
@app.route('/login', methods=['Get', 'Post'])
def login():
    loginform = LoginForm()
    if request.method == 'POST' and loginform.validate():
        name = loginform.name.data
        phone = loginform.phone.data
        logged_user = User.query.filter(User.name == name).first()
        if logged_user and check_password_hash(logged_user.phone,phone):
            flash(f"Successfully logged in {loginform.name.data}!", 'success')
            login_user(logged_user)
            print(current_user.name)
        else:
            flash(f'Name or Phone do not match. Please check again', 'danger')
        print(name,phone)
        return redirect(url_for('index'))
    return render_template('login.html', title='Login', form=loginform)

@app.route('/logout')
def logout():
    logout_user()
    flash(f'Sucessfully logged out!', 'success')
    return redirect(url_for('index'))
