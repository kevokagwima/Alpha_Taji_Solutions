from operator import length_hint
import os

from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

class user(db.Model):
    __tablename__ = 'new_members'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(length=50), nullable=False)
    second_name = db.Column(db.String(length=50), nullable=False)
    last_name = db.Column(db.String(length=50), nullable=False)
    email = db.Column(db.String(length=100), nullable=False)
    phone_number = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(length=50), nullable=False)
    password = db.Column(db.String(length=50), nullable=False)
