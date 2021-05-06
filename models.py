from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import UserMixin

db = SQLAlchemy()
bcrypt = Bcrypt()

class user(db.Model, UserMixin):
    __tablename__ = 'new_members'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(length=50), nullable=False)
    second_name = db.Column(db.String(length=50), nullable=False)
    last_name = db.Column(db.String(length=50), nullable=False)
    email = db.Column(db.String(length=100), nullable=False)
    phone_number = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(length=50), nullable=False)
    password = db.Column(db.String(length=100), nullable=False)

    @property
    def passwords(self):
        return self.passwords
    
    @passwords.setter
    def passwords(self, plain_text_password):
        self.password = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password, attempted_password)
