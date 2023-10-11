from App.database import db

class Programme(db.Model):

    programmeName = db.Column(db.String(120), primary_key=True)
    faculty =  db.Column(db.String(80), nullable=False)
    department = db.Column(db.String(80), nullable=False)
    levelOneCredits =  db.Column(db.Integer, nullable=False)
    advancedLevelCredits =  db.Column(db.Integer, nullable=False)
    foundationCredits =  db.Column(db.Integer, nullable=False)
    totalCredits =  db.Column(db.Integer, nullable=False)
    courses = db.relationship('CourseProgramme', backref=db.backref('programmeName', lazy='joined'))

    def toJSON(self):
        return{

        }