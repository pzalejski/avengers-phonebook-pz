from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length


class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[
                       DataRequired(), Length(min=2, max=20)])
    address = StringField('Address', validators=[DataRequired(), ])
    phone = StringField('Phone', validators=[DataRequired(), Length(min=10)])
    submit = SubmitField('Sign Up')
