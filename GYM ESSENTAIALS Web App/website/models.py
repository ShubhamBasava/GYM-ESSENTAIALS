from . import db
from flask_login import UserMixin

#----001----User Table
class User(db.Model, UserMixin) :
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    mobile = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)


#----005----Feedback Table
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    subject = db.Column(db.String(150), nullable=False)
    message = db.Column(db.String(1000), nullable=False)