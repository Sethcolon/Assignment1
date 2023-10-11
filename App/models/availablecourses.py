from flask_sqlalchemy import SQLAlchemy
from App.database import db

class AvailableCourses(db.Model):

    courseID = db.Column(db.String(120), db.ForeignKey('course.courseID'), nullable=False)


    def toJSON(self):
        return{
            'course' : self.course.toJSON()
        }