from .user import User
from flask_login import UserMixin
from App.database import db

class Staff(User):

    __tablename__ = 'staff'

    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.set_password(password)
        self.user_type = "staff"

    def toJSON(self):
        return{
            'id': self.id,
            'email': self.email,
            'name': self.name,
            'type': 'staff'
        }
