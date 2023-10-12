from App.models import User, Course, Programme
from App.database import db

def create_programme(programmeID, programmeName, faculty, levelOneCredits, advancedLevelCredits, foundationCredits, totalCredits):
    newProgramme = Programme(programmeID=programmeID, programmeName=programmeName, faculty=faculty, levelOneCredits=levelOneCredits, advancedLevelCredits=advancedLevelCredits, foundationCredits=foundationCredits, totalCredits=totalCredits)
    db.session.add(newProgramme)
    db.session.commit()
    return newProgramme

def get_programme(programmeID):
    return Programme.query.get(programmeID)

def get_all_programmes():
    return Programme.query.all()

def get_programmes_json():
    programmes = Programme.query.all()
    return [programme.toJSON() for programme in programmes]