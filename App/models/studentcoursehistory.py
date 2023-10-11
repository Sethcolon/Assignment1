from App.database import db

class StudentCourseHistory(db.Model):

    historyID = db.Column(db.Integer, primary_key=True)
    studentID = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    courseID = db.Column(db.String(120), db.ForeignKey('course.courseID'), nullable=False)


    def toJSON(self):
        return{

        }