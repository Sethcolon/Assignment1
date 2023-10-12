from App.models import User, Course, Programme, CourseHistory, CoursePlan
from App.database import db

def create_CourseHistory(studentID, courseID):
    newCourseHistory = CourseHistory(studentID=studentID, courseID=courseID)
    db.session.add(newCourseHistory)
    db.session.commit()
    return newCourseHistory

def get_coursehistory(courseHistoryID):
    return CourseHistory.query.get(courseHistoryID)

def get_coursehistory_by_student(studentID):
    return CourseHistory.query.filter_by(studentID=studentID).all()

def get_all_coursehistory():
    return CourseHistory.query.all()

def get_coursehistory_json():
    coursehistory = CourseHistory.query.all()
    return [coursehistory.toJSON() for ch in coursehistory]



def create_CoursePlan(studentID, courseID):
    newCoursePlan = CoursePlan(studentID=studentID, courseID=courseID)
    db.session.add(newCoursePlan)
    db.session.commit()
    return newCoursePlan

def get_courseplan(coursePlanID):
    return CoursePlan.query.get(coursePlanID)

def get_courseplan_by_student(studentID):
    return CoursePlan.query.filter_by(studentID=studentID).all()

def get_all_courseplans():
    return CoursePlan.query.all()

def get_courseplans_json():
    courseplan = CoursePlan.query.all()
    return [courseplan.toJSON() for cp in courseplan]