from flask_sqlalchemy import SQLAlchemy
from App.database import db

class Programme(db.Model):

    programmeID = db.Column(db.Integer, primary_key=True)
    programmeName = db.Column(db.String(120), nullable=False, unique=True)
    levelOneCredits =  db.Column(db.Integer, nullable=False)
    advancedLevelCredits =  db.Column(db.Integer, nullable=False)
    foundationCredits =  db.Column(db.Integer, nullable=False)
    totalCredits =  db.Column(db.Integer, nullable=False)
    courses = db.relationship('CourseProgramme', backref=db.backref('programmeID', lazy='joined'))

    def __init__(self, programmeName, levelOneCredits, advancedLevelCredits, foundationCredits, totalCredits):
        self.programmeName = programmeName
        self.levelOneCredits = levelOneCredits
        self.advancedLevelCredits = advancedLevelCredits
        self.foundationCredits = foundationCredits
        self.totalCredits = totalCredits

    def toJSON(self):
        return{
            'programmeID' : self.programmeID,
            'programmeName' : self.programmeName,
            'levelOneCredits' : self.levelOneCredits,
            'advancedLevelCredits' : self.advancedLevelCredits,
            'foundationCredits' : self.foundationCredits,
            'totalCredits' : self.totalCredits
        }
