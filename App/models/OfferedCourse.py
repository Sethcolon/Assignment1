from flask_sqlalchemy import SQLAlchemy
from App.database import db

class OfferedCourse(db.Model):

    courseID = db.Column(db.String(30), db.ForeignKey('course.courseID'), nullable=False)
    remarks = db.Column(db.String(120), nullable=True)

    def __init__ (self, courseID, remarks=None)
        self.courseID = courseID
        self.remarks = remarks 


    def toJSON(self):
        return{
            'course' : self.course.toJSON(),
            'remarks' : self.remarks
        }