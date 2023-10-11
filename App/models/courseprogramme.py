from flask_sqlalchemy import SQLAlchemy
from App.database import db

class CourseProgramme(db.Model):

    courseProgrammeID = db.Column(db.Integer, primary_key=True)
    courseID = db.Column(db.Integer, db.ForeignKey('course.courseID'), nullable=False)
    programmeID = db.Column(db.String(120), db.ForeignKey('programme.programmeID'), nullable=False)

    def __init__(self, courseID, programmeID):
        self.courseID = courseID
        self.programmeID = programmeID

    def toJSON(self):
        return{
            'courseProgrammeID' : self.courseProgrammeID,
            'course' : self.course.toJSON(),
            'programme' : self.programme.toJSON()
        }