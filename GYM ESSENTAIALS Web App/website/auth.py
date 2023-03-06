from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user,login_required,logout_user,current_user


# Creating "views" Blueprint
auth = Blueprint('auth', __name__)

#Defining Login route 
@auth.route('/login', methods=['GET','POST'])
def login():
    # Accessing and Strong Data from Login From
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Return User from DB
        user = User.query.filter_by(email=email).first()

        if user:
            # Password Check
            if check_password_hash(user.password, password) :
                flash('Logged in Succesfully!.', category='success')

                # Loggging User in Dashboard after login
                login_user(user, remember=True)
                # Redirecting to dashboard after signup
                return redirect(url_for('views.home'))

            else:
                flash('Incorrect Password. Please try again!', category='error')
        else :
            flash('User does not exists. Please SignUp!', category='error')
            return redirect(url_for('auth.sign_up'))


    return render_template("login.html", user=current_user)

# Defining Logout route 
@auth.route('/logout')
@login_required
def logout():
    # Logging out the user
    logout_user()
    flash('Logged out of your account!.', category='success')
    return redirect(url_for('auth.login'))

# Defining SignUP route 
@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        mobile = request.form.get('mobile')

        user = User.query.filter_by(email=email).first()

        if user:
            flash('User Already Exists. Please Login!.', category="error")
            return redirect(url_for('auth.login'))
        elif len(name) < 4 :
            flash('Your name must be longer than 4 characters.', category="error")
        elif len(str(mobile)) < 8 :
            flash('Please Enter valid Mobile Number.', category="error")
        elif len (email) < 6 :
            flash('Please Enter valid Email id.', category="error")
        elif password1 != password2:
            flash('Entered passwords don\'t match!', category="error")
        elif len(password1) < 5 : 
            flash('Password must be at leat 7 characters.', category="error")
        else : 
            new_user = User(email=email,mobile=mobile,name=name,password=generate_password_hash(password1, method='sha256'))

            db.session.add(new_user)
            db.session.commit()
            
            flash('Account created Succesfully!.', category="success")
            login_user(new_user, remember=True)
            return redirect(url_for('views.home'))

    return render_template("sign-up.html",user=current_user)
