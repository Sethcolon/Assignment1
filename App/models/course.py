from flask_sqlalchemy import SQLAlchemy
from App.database import db

class Course(db.Model):

    courseID = db.Column(db.String(30), primary_key=True)
    courseName =  db.Column(db.String(80), nullable=False)
    type = db.Column(db.Enum("Level One", "Advanced Level", "Foundation"), nullable=False)
    credits =  db.Column(db.Integer, nullable=False)
    semester =  db.Column(db.Integer, nullable=False)
    programmes = db.relationship('CourseProgramme', backref=db.backref('courseID', lazy='joined'))

    def __init__(self, courseID, courseName, type, credits, semester):
        self.courseID = courseID
        self.courseName = courseName
        self.type = type
        self.credits = credits
        self.semester = semester

    def toJSON(self):
        return{
            'courseID' : self.courseID,
            'courseName' : self.courseName,
            'type' : self.type,
            'credits' : self.credits,
            'semester' : self.semester,
        }