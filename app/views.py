'''A module used to listen on the root of the application and will select
 title and text from the database '''
#importing the object render_template form flask for returning templates
from flask import render_template, request, redirect, url_for
from app import app
from app.user import Users

#binding login function to the url /
@app.route('/', methods = ['GET', 'POST'])
def login():
    '''a method that returns the route of login in the html'''
    error = None
    if request.method =="POST":
        user_email = request.form['user_email_login']
        user_password = request.form['password_login']
        if Users().login_user(user_email, user_password) ==True :
            return redirect(url_for('view_bucket_list'))
        else:
            error = "Invalid email / password"
    return render_template("Login.html" , error = error)
#binding register function to the url /Register
@app.route('/Register', methods = ['GET', 'POST'])
def register():
    '''a method that returns the route of register in the html'''  
    if request.method == "POST":
        user_name = request.form['username_register']
        user_email = request.form['useremail_register']
        password = request.form['password_register']
        new_password = request.form['confirm_new_password']
        if Users().create_user(user_name, user_email, password , new_password):
            return redirect(url_for('login'))
    return render_template("Register.html")
#binding create_bucket_list function to the url /CreateBucketList
@app.route('/CreateBucketList', methods = [ 'POST'])
def create_bucket_list():
    '''a method that returns the route of createbucketlist in the html'''
    return render_template("CreateBucketList.html")
#binding add_Activities function to the url /AddActivities
@app.route('/AddActivities')
def add_activities():
    '''a method that returns the route of addactivities in the html'''
    return render_template("AddActivities.html")
#binding view_bucket_list function to the url /ViewBucketList
@app.route('/ViewBucketList', methods = ['GET', 'POST' ,"DELETE"])
def view_bucket_list():
    '''a method that returns the route of viewbucketlist in the html'''
    return render_template("ViewBucketList.html")
#binding view_activities function to the url /ViewActivities
@app.route('/ViewActivities')
def view_activities():
    '''a method that returns the route of viewactivities in the html'''
    return render_template("ViewActivities.html")
