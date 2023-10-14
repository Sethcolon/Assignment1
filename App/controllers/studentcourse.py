from App.database import db
from App.models import User, Student, Staff, Course, Programme, CourseHistory, CoursePlan

def create_CourseHistory(student, course):
#def create_CourseHistory(studentID, courseID):
    #newCourseHistory = CourseHistory(studentID=studentID, courseID=courseID)
    #db.session.add(newCourseHistory)
    #db.session.commit()
    #return newCourseHistory
    return student.selectPastCourse(course)

def remove_CourseHistory(student, courseHistory):
    return student.deletePastCourse(courseHistory)

def get_coursehistory(courseHistoryID):
    return CourseHistory.query.get(courseHistoryID)

def get_coursehistory_by_student(studentID): 
    return CourseHistory.query.filter_by(studentID=studentID).all()

def get_coursehistory_by_student_json(studentID): 
    coursehistory = CourseHistory.query.filter_by(studentID=studentID).all()
    if coursehistory:
        return [coursehistory.toJSON() for ch in coursehistory]
    return []

def get_all_coursehistory():
    return CourseHistory.query.all()

def get_all_coursehistory_json():
    coursehistory = CourseHistory.query.all()
    if coursehistory:
        return [coursehistory.toJSON() for ch in coursehistory]
    return []


def create_CoursePlan(student, course):
    #newCoursePlan = CoursePlan(studentID=studentID, courseID=courseID)
    #db.session.add(newCoursePlan)
    #db.session.commit()
    #return newCoursePlan
    return student.selectPlannedCourse(course)

def remove_CoursePlan(student, coursePlan):
    return student.deletePlannedCourse(coursePlan)

def get_courseplan(coursePlanID):
    return CoursePlan.query.get(coursePlanID)

def get_courseplan_by_student(studentID):
    return CoursePlan.query.filter_by(studentID=studentID).all()

def get_courseplan_by_student_json(studentID):
    courseplan = CoursePlan.query.filter_by(studentID=studentID).all()
    if courseplan:
        return [courseplan.toJSON() for cp in courseplan]
    return []

def get_all_courseplans():
    return CoursePlan.query.all()

def get_all_courseplans_json():
    courseplan = CoursePlan.query.all()
    if courseplan:
        return [courseplan.toJSON() for cp in courseplan]
    return []
