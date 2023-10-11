from App.database import db

class CourseProgramme(db.Model):

    courseProgrammeID = db.Column(db.Integer, primary_key=True)
    courseID = db.Column(db.Integer, db.ForeignKey('course.courseID'), nullable=False)
    programmeName = db.Column(db.String(120), db.ForeignKey('programme.programmeName'), nullable=False)


    def toJSON(self):
        return{

        }