from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class UserForm(FlaskForm):
    name = StringField('Name', validators=[
                       DataRequired(), Length(min=2, max=20)])
    address = StringField('Address', validators=[DataRequired() ])
    phone = PasswordField('Phone', validators=[DataRequired(), Length(min=10)])
    confirm_phone = PasswordField('Confirm Phone', validators=[DataRequired(), EqualTo('phone')])
    submit = SubmitField('Sign Up')
    submit2 = SubmitField('Update')


class LoginForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    phone = PasswordField('Phone', validators=[DataRequired()])
    submit = SubmitField('Login')


class PostForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    address = TextAreaField('Address', validators=[DataRequired()])
    submit = SubmitField()

