from flask_sqlalchemy import SQLAlchemy
from TeamApp.app import app
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), unique = True)
    email_id = db.Column(db.String(64), unique = True, index= True)
    gender = db.Column(db.String(32), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    position = db.Column(db.String(64), nullable=False)
    reports_to = db.Column(db.String(64))

    def __init__(self, name, email, age, gender, position, reports_to):
        self.name = name
        self.email = email
        self.email_id = email[:email.index("@")]
        self.age = age
        self.gender = gender
        self.position = position
        self.reports_to = reports_to


    def __repr__(self):
        return f"Name: {self.name} Email: {self.email}"
        