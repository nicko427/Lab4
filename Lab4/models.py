from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True, nullable=False)
  password = db.Column(db.String(120), nullable=False)

  def __init__(self, username, password):
    self.username= username
    self.set_password(password)

  def set_password(self, password):
    self.password = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password, password)
    
class Student(db.Model):
  id = db.Column(db.String(9), primary_key=True)
  first_name = db.Column(db.String(80), nullable=False)
  last_name = db.Column(db.String(80), nullable=False)
  image = db.Column(db.String(120), nullable=False)
  programme = db.Column(db.String(120), nullable=False)
  start_year = db.Column(db.Integer, nullable=False)


  def __init__(self, id, first_name, last_name, image, programme, start_year):
    self.id = id
    self.first_name = first_name
    self.last_name = last_name
    self.image = image
    self.programme = programme
    self.start_year = start_year



class Review(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  student_id = db.Column(db.String, db.ForeignKey('student.id'), nullable=False)
  user_id = db.Column(db.Integer, nullable=False)
  text = db.Column(db.String(80), nullable=False)
  rating = db.Column(db.Integer, nullable=False)


  def __init__(self, student_id, user_id, text, rating):
    self.student_id = student_id
    self.user_id = user_id
    self.text = text
    self.rating = rating
