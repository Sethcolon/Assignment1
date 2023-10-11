from flask_login import login_user, login_manager, logout_user, LoginManager
from flask_jwt_extended import create_access_token, jwt_required, JWTManager

from App.models import User

def jwt_authenticate(email, password):
    staff = Staff.query.filter_by(email=email).first()
    if staff and staff.check_password(password):
        return create_access_token(identity=email)
    student = Student.query.filter_by(email=email).first()
    if student and student.check_password(password):
        return create_access_token(identity=email)
    return None
    

def login(email, password):
    #user = User.query.filter_by(email=email).first()
    #if user and user.check_password(password):
    #    return user
    #return None
    staff = Staff.query.filter_by(email=email).first()
    if staff and staff.check_password(password):
        return staff
    student = Student.query.filter_by(email=email).first()
    if student and student.check_password(password):
        return student
    return None

def setup_flask_login(app):
    login_manager = LoginManager()
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
    
    return login_manager

def setup_jwt(app):
    jwt = JWTManager(app)

    @jwt.user_identity_loader
    def user_identity_lookup(identity):
        user = User.query.filter_by(email=identity).one_or_none()
        if user:
            return user.id
        return None

    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]
        return User.query.get(identity)

    return jwt