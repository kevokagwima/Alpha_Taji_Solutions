from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField
from wtforms.validators import Length, EqualTo, Email, DataRequired, NumberRange

class registration(FlaskForm):
  first_name = StringField(label='First Name')
  second_name = StringField(label='Second Name')
  last_name = StringField(label='Last Name')
  email_address = StringField(label='Email Address', validators=[Email(), DataRequired()])
  phone_number = IntegerField(label='Phone number', validators=[NumberRange(min=10, max=10), DataRequired()])
  username = StringField(label='Username', validators=[Length(min=5, max=25), DataRequired()])
  password = PasswordField(label='Password', validators=[Length(min=5), DataRequired()])
  password1 = PasswordField(label='Confirm Password', validators=[EqualTo('password'), DataRequired()])
