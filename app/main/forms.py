from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms import StringField,TextAreaField, SubmitField,ValidationError,PasswordField,FormField,TimeField, SelectField
from wtforms.validators import Required,Email,DataRequired,Length
from flask_login import current_user
from ..models import User

class UpdateProfile(FlaskForm):
    username = StringField('Enter Your Username', validators=[Required()])
    email = StringField('Email Address', validators=[Required(),Email()])
    bio = TextAreaField('Write a brief bio about you.',validators = [Required()])
    profile_picture = FileField('profile picture', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')

    def validate_email(self,email):
        if email.data != current_user.email:
            if User.query.filter_by(email = email.data).first():
                raise ValidationError("The Email has already been taken!")
    
    def validate_username(self, username):
        if username.data != current_user.username:
            if User.query.filter_by(username = username.data).first():
                raise ValidationError("The username has already been taken")

# class SelectFavMeal(FlaskForm):
#     title = StringField('Title',validators=[Required()])
#     content = TextAreaField('Blog Content',validators=[Required()])
#     submit = SubmitField('Post')
    
class SignupForm(FlaskForm): 
    first_name = StringField("First Name", validators=[DataRequired("Please enter your First Name.")])    
    last_name = StringField("Last Name", validators=[DataRequired("Please enter your Last Name.")])    
    email = StringField("Email", validators=[DataRequired("Please enter your email address."), Email("Pelase enter a valid email. name@host.com")])   
    password = PasswordField("Password", validators=[DataRequired("Please enter your password"), Length(min=6,message="Passwords must be at least 6 characters in length.")])   
    submit = SubmitField("Sign Up")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired("Please enter your email address.")])    
    password = PasswordField("Password", validators=[DataRequired("Please enter a password.")])   
    submit = SubmitField("Sign In")

class OrderForm(FlaskForm):    
    meal = StringField("What type of meal would you like?", validators=[DataRequired("Please enter a meal.")]) 
    time = FormField(TimeField)
    now_or_later = SelectField("Do you want your meal now or later?", choices=[("NOW", "Now"), ("LATER", "Later")])    
    delivery = SelectField("Would you like your food delivered or take out?",choices=[("DELIVERY", "Delivery"), ("TAKEOUT", "Take Out")])   
    submit = SubmitField("Place Order")
  