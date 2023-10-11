from App.models import User, Course, Programme
from App.database import db

def get_course(courseID):
    return Course.query.get(courseID)

def get_all_courses():
    return Course.query.all()