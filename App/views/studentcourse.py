from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import login_required, login_user, current_user, logout_user

from App.controllers import(
    get_available_courses_json
)

studentcourse_views = Blueprint('student-course_views', __name__, template_folder='../templates')