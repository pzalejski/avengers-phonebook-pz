from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[
                       DataRequired(), Length(min=2, max=20)])
    address = StringField('Address', validators=[DataRequired() ])
    phone = PasswordField('Phone', validators=[DataRequired(), Length(min=10)])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    phone = PasswordField('Phone', validators=[DataRequired()])
    submit = SubmitField('Login')
