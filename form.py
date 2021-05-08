from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField
from wtforms.validators import Length, EqualTo, Email, DataRequired, NumberRange, ValidationError
from models import user

class registration(FlaskForm):
  first_name = StringField(label='First Name', validators=[DataRequired()])
  second_name = StringField(label='Second Name', validators=[DataRequired()])
  last_name = StringField(label='Last Name', validators=[DataRequired()])
  email_address = StringField(label='Email Address', validators=[Email(), DataRequired()])
  phone_number = IntegerField(label='Phone number', validators=[NumberRange(min=10, max=10), DataRequired()])
  username = StringField(label='Username', validators=[Length(min=5, max=25), DataRequired()])
  password = PasswordField(label='Password', validators=[Length(min=5), DataRequired()])
  password1 = PasswordField(label='Confirm Password', validators=[EqualTo('password'), DataRequired()])

  def validate_username(self, username_to_validate):
    username = user.query.filter_by(username=username_to_validate.data).first()
    if username:
      raise ValidationError("Username already exists, Please try again")

  def validate_email_address(self, email_to_validate):
    email = user.query.filter_by(email=email_to_validate.data).first()
    if email:
      raise ValidationError("Email already exists, Please try again")

  def validate_phone_number(self, phone_number_to_validate):
    phone = user.query.filter_by(phone_number=phone_number_to_validate.data).first()
    if phone:
      raise ValidationError("Phone number already exists, Please try again")

class signin(FlaskForm):
  username = StringField(label='Username', validators=[DataRequired()])
  password = PasswordField(label='Password', validators=[DataRequired()])
