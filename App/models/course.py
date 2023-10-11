from App.database import db

class Course(db.Model):

    courseID = db.Column(db.String(30), primary_key=True)
    courseName =  db.Column(db.String(80), nullable=False)
    type = db.Column(db.Enum("Level One", "Advanced Level", "Foundation"), nullable=False)
    credits =  db.Column(db.Integer, nullable=False)
    semester =  db.Column(db.Integer, nullable=False)
    programmes = db.relationship('CourseProgramme', backref=db.backref('courseID', lazy='joined'))

    def toJSON(self):
        return{

        }