from App.models import User, Staff, Student, Course, Programme
from App.database import db

def create_course(courseID, courseName, type, credits, semester, prerequisite=None):
    newCourse = Course(courseID=courseID, courseName=courseName, type=type, credits=credits, semester=semester, prerequisite=prerequisite)
    db.session.add(newCourse)
    db.session.commit()
    return newCourse

def get_course(courseID):
    return Course.query.get(courseID)

def get_all_courses():
    return Course.query.all()

def get_available_courses():
    return Course.query.filter_by(status='Available').all()

def get_all_courses_json():
    courses = Course.query.all()
    return [course.toJSON() for course in courses]

def make_course_available(course)
    if course:
        return staff.makeCourseAvailable(course)
    return False

def make_course_unavailable(course)
    if course:
        return staff.makeCourseUnavailable(course)
    return False
