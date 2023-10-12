from .User import User
from .CourseHistory import CourseHistory
from flask_login import UserMixin
from App.database import db

class Student(User):

    __tablename__ = 'student'

    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.set_password(password)
        self.userType = "student"

    def selectPastCourse(self, course):
        newCourseHistory = CourseHistory(self.id, course.courseID)
        try:
            db.session.add(newCourseHistory)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False
    
    def deletePastCourse(self, courseHistory):
        try:
            db.session.delete(courseHistory)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False

    def selectPlannedCourse(self, course):
        newCoursePlan = CoursePlan(self.id, course.courseID)
        try:
            db.session.add(newCoursePlan)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False
    
    def deletePlannedCourse(self, coursePlan):
        try:
            db.session.delete(coursePlan)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False

    def toJSON(self):
        return{
            'id': self.id,
            'email': self.email,
            'name': self.name,
            'userType': 'student'
        }

    

    
    def selectPlannedCourse():

    def removePlannedCourse():
