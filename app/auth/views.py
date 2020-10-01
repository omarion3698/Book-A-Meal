from flask import render_template,flash, request, redirect, url_for
from flask_login import login_user, logout_user,login_required
from app.auth import auth
from app.models import User
from .forms import RegForm,LoginForm
from ..email import mail_message
from .. import db

@auth.route('/login',methods = ['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user != None and user.verify_password(form.password.data):
            login_user(user,form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Wrong Username or Password')
    return render_template('auth/login.html',form = form)

@auth.route('/signup',methods = ["POST","GET"])
def signup():
    form = RegForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email = form.email.data, password=form.password.data)
        user.save()
        mail_message("Welcome to Royal food","email/welcome",user.email,user=user)
        return  redirect(url_for('auth.login'))
    return render_template('auth/signup.html',registration_form=form )

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    
    flash('You have been successfully logged out')
    return redirect(url_for("main.index"))


@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,firstname= form.firstname.data,lastname= form.lastname.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
        mail_message("Welcome to Royal food","email/welcome_user",user.email,user=user)
        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/register.html',registration_form = form)
