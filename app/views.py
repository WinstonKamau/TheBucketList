'''A module used to listen on the root of the application and will select
 title and text from the database '''
#importing the object render_template form flask for returning templates
from flask import render_template, request
from app import app
from app.user import Users
from flask.ext.login import LoginManager
 
login_manager = LoginManager()
login_manager.init_app(app)

#binding login function to the url /
@app.route('/', methods = ['GET', 'POST'])
def login():
    '''a method that returns the route of login in the html'''
    return render_template("Login.html")
#binding register function to the url /Register
@app.route('/Register')
def register():
    '''a method that returns the route of register in the html'''
    return render_template("Register.html")
#binding create_bucket_list function to the url /CreateBucketList
@app.route('/CreateBucketList', methods = ['POST'])
def create_bucket_list():
    '''a method that returns the route of createbucketlist in the html'''
    return render_template("CreateBucketList.html")
#binding add_Activities function to the url /AddActivities
@app.route('/AddActivities')
def add_activities():
    '''a method that returns the route of addactivities in the html'''
    return render_template("AddActivities.html")
#binding view_bucket_list function to the url /ViewBucketList
@app.route('/ViewBucketList', methods = ['POST'])
def view_bucket_list():
    '''a method that returns the route of viewbucketlist in the html'''
    return render_template("ViewBucketList.html")
#binding view_activities function to the url /ViewActivities
@app.route('/ViewActivities')
def view_activities():
    '''a method that returns the route of viewactivities in the html'''
    return render_template("ViewActivities.html")
