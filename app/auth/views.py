from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError



@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "BOOK A MEAL LOGIN"
    return render_template('auth/login.html',login_form = login_form,title=title)

@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,firstname= form.firstname.data,lastname= form.lastname.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()

        mail_message("Welcome to BOOK A MEAL","email/welcome_user",user.email,user=user)

        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/register.html',registration_form = form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()