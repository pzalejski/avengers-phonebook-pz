from phonebook import app, db
from flask import render_template, redirect, request, flash, url_for

from phonebook.forms import UserForm, LoginForm, PostForm
from phonebook.models import User, check_password_hash, Post

from flask_login import login_required, login_user, current_user, logout_user


@app.route("/")
def index():  # fucntions that are called in the url_for('')
    return render_template("home.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = UserForm()
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

@app.route('/create', methods=['GET', 'POST'])
@login_required
def create_contact():
    form = PostForm()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        address = form.address.data
        user_id = current_user.id
        print(name, address)
        contact = Post(name, address, user_id)
        
        db.session.add(contact)
        db.session.commit()
        return redirect(url_for('create_contact'))
    else:
        flash('Please make sure all fields are filled out.','danger')
    return render_template('contactform.html', form = form)

@app.route('/logout')
def logout():
    logout_user()
    flash(f'Sucessfully logged out!', 'success')
    return redirect(url_for('index'))


@app.route('/phonebook/<int:post_id>')
# used to look up post id
def phonebook_detail(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('phonebook_detail.html', post=post)

@app.route('/phonebook/update/<int:post_id>', methods=['GET', 'POST', 'PUT'])
@login_required
def phonebook_update(post_id):
    postform=PostForm()
    post = Post.query.get_or_404(post_id)
    if request.method == 'POST' and postform.validate():

        #Todo use postform for update
        name = postform.name.data
        address = postform.address.data
        user_id = current_user.id
        print(name,address,user_id)

        post.name = name
        post.address = address
        post.user_id = user_id

        db.session.commit()
        return redirect(url_for('home'))
    return render_template('phonebook_update.html', form=postform)
    
@app.route('/phonebook/delete/<int:post_id>', methods=['POST'])
@login_required
def phonebook_delete(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/user/<int:user_id>')
def user_detail(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('user_detail.html', user=user)

@app.route('/user/update/<int:user_id>', methods=['GET','POST'])
@login_required
def user_update(user_id):
    updateuser = UserForm()
    user = User.query.get_or_404(user_id)
    if request.method == 'POST' and updateuser.validate():
        name = updateuser.name.data
        address = updateuser.address.data
        phone= updateuser.phone.data

        user.name = name
        user.address = address
        user.phone = user.set_password(phone)


        db.session.commit()
        return redirect(url_for('home'))
    return render_template('user_update.html', form=updateuser)
