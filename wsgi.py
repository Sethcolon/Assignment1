import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.main import create_app
from App.controllers import (
    create_user, get_all_users_json, get_all_users, 
    create_course, get_course, get_all_courses,
    create_programme, get_programme, get_all_programmes )

# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def initialize():
    db.drop_all()
    db.create_all()
    create_user('bob@uwimail.com', 'bob', 'bobpass', 'staff')
    create_user('jane@uwimail.com', 'jane', 'janepass', 'student')
    create_programme('CS_Spec', 'BSc Computer Science (Special)' 'FST' 24, 60, 9, 93)
    create_programme('CS_Mgmt', 'BSc Computer Science (Management)' 'FST' 24, 60, 9, 93)
    create_programme('CS_Major', 'Major in Computer Science' 'FST' 24, 60, 9, 93)
    create_course(COMP1600, 'Introduction to Computing Concepts', 'Level One', 3, 1)
    create_course(COMP1601, 'Computer Programming I', 'Level One', 3, 1)
    create_course(INFO1600, 'Introduction to Information Technology Concepts', 'Level One', 3, 1)
    create_course(MATH1115, 'Fundamental Mathematics for General Sciences I', 'Level One', 3, 1)
    create_course(FOUN1101, 'Caribbean Civilisation', 'Foundation', 3, 1)
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("email", default="rob@uwimail.com")
@click.argument("name", default="rob")
@click.argument("password", default="robpass")
@click.argument("userType", default="staff")
def create_user_command(email, name, password):
    create_user(email, name, password)
    print(f'{email} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)