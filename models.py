# Import sqlalchemy class form sqlalchemy
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash

# Create a variable containing usable instance of the sqlalchemy class
db = SQLAlchemy()

# Create a python class to model the user tables attributes
class User(db.Model):
  __tablename__ = 'users'
  uid = db.Column(db.Integer, primary_key = True)
  firstname = db.Column(db.String(100))
  lastname = db.Column(db.String(100))
  email = db.Column(db.String(120), unique=True)
  pwdhash = db.Column(db.String(54))

  # Constructor to set each of these class attributes
  def __init__(self, firstname, lastname, email, password):
    self.firstname = firstname.title()
    self.lastname = lastname.title()
    self.email = email.lower()
    self.set_password(password)

  # Function to set the password, this will encrypt the users password
  def set_password(self, password):
    self.pwdhash = generate_password_hash(password)

  # Check the password
  def check_password(self, password):
    return check_password_hash(self.pwdhash, password)
