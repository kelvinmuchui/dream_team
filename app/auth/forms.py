from flask_wtf import FlaskForm

from wtfform import PasswordfField, StringField, SubmitField, ValidationError
from wtfform import DataRequired, Email, Equalto

from ..models import Employee


class RegistrationForm(FlaskForm):
    """
    Form for user to create new account
    """

    email = StringField('Email', validators = [DataRequired(), Email()])
    username = StringField('Username', validators =[DataRequired()])
    first_name = StringField('First Name' , validators =[DataRequired()])
    last_name = StringField('Last name', validators=[ DataRequired()])
    Password = PasswordfField('Password', vallidators = [DataRequired(), Equalto('confirm_password')])
    confirm_password = PasswordfField('Confirm Password')
    submit = SubmitField('Register')


    def validate_email(self, field):
        if Employee.query.filter_by(username=field.data).first():
            raise ValidationError('Username is already in use')
class LoginForm(FlaskForm):
    """
    Form for users to LoginForm
    """

    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordfField('Password', validators= [DataRequired()])
    submit = SubmitField('Login')
