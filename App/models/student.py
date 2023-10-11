from .user import User
from flask_login import UserMixin
from App.database import db

class Student(User):

    __tablename__ = 'student'
    programme = db.Column(db.String(120), db.ForeignKey('programme.name'), nullable=False)

    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.set_password(password)
        self.userType = "student"

    def toJSON(self):
        return{
            'id': self.id,
            'email': self.email,
            'name': self.name,
            'userType': 'student'
        }

    def selectPastCourse():

    def removePastCourse():

    def selectPlannedCourse():

    def removePlannedCourse():
