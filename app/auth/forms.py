from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import User


class LoginForm(FlaskForm):
    username       = StringField('User')
    password       = PasswordField('Password')    
    submit_sing_in = SubmitField('Sing in')    

class RegistrationForm(FlaskForm):
    username  = StringField('Insert your username', validators=[DataRequired()])
    email     = StringField('Insert your email', validators=[DataRequired(), Email()]) 
    password  = PasswordField('Insert your password', validators=[DataRequired()])
    password2 = PasswordField('Repeat your password', validators=[DataRequired(), EqualTo('password')])
    submit    = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please choose a diffrent username')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please choose a diffrent email')
    