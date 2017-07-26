'''A module used to listen on the root of the application and will select
 title and text from the database '''
#importing the object render_template form flask for returning templates
from flask import render_template, request, redirect, url_for
from app import app
from app.user import Users
from app.user import BucketList

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
@app.route('/CreateBucketList', methods = ['GET', 'POST'])
def create_bucket_list():
    '''a method that returns the route of createbucketlist in the html'''
    if request.method == "POST":
        bucket_name = request.form['bucketlistcreated']
        BucketList().create_bucket(bucket_name)
        return redirect(url_for('view_bucket_list')) 
    return render_template("CreateBucketList.html")
@app.route('/EditBucketList/<index>', methods = ['GET', 'POST'])
def edit_bucket_list(index=None):
    if request.method == "POST":
        new_name = request.form['new_name']
        BucketList().edit_bucket( int(index), new_name)
        return redirect(url_for('view_bucket_list'))
    return render_template("EditBucketList.html")
@app.route('/DeleteBucketList/<index>', methods = ['GET', 'POST'])
def delete_bucket_list(index=None):
    if request.method == "POST":
        BucketList().delete_bucket(int(index))
        return redirect(url_for('view_bucket_list'))
    bucket_item_chosen = BucketList().bucket_list[int(index)].bucket_name
    return render_template("DeleteBucketList.html", bucket_item_chosen=bucket_item_chosen )
#binding view_bucket_list function to the url /ViewBucketList
@app.route('/ViewBucketList', methods = ['GET', 'POST' ])
def view_bucket_list():
    '''a method that returns the route of viewbucketlist in the html'''
    if request.method == "POST":
        return redirect (url_for('create_bucket_list'))
    else:
        bucket_items = BucketList().bucket_list
        return render_template("ViewBucketList.html", bucket_items=bucket_items)
#binding view_activities function to the url /ViewActivities
@app.route('/ViewActivities/<index>')
def view_activities(index):
    '''a method that returns the route of viewactivities in the html'''
    activity_items = BucketList().bucket_list[int(index)].activity_list
    spacer = "x"
    return render_template("ViewActivities.html", activity_items=activity_items, index=index, spacer=spacer)
#binding add_Activities function to the url /AddActivities
@app.route('/AddActivities/<bucket_index>', methods = ['GET', 'POST'])
def add_activities(bucket_index):
    '''a method that returns the route of addactivities in the html'''
    if request.method == "POST":
        activity = request.form['theActivity']
        BucketList().create_activity(int(bucket_index), activity)
        return redirect('/ViewActivities/'+bucket_index)
    return render_template("AddActivities.html")
#binding add_Activities function to the url /AddActivities
@app.route('/EditActivity/<indices>', methods = ['GET', 'POST'])
def edit_activities(indices):
    '''a method that returns the route of addactivities in the html'''
    if request.method == "POST":
        new_activity = request.form['new_activity']
        bucket_index = indices.split("x")[0]
        activity_index = indices.split("x")[1]
        BucketList().edit_activity(int(bucket_index), int(activity_index), new_activity)
        return redirect('/ViewActivities/'+bucket_index)
    return render_template("EditActivity.html")
@app.route('/DeleteActivity/<indices>', methods = ['GET','POST'])
def delete_activities(indices):
    '''a method that deletes an activity'''
    bucket_index = indices.split("x")[0]
    activity_index = indices.split("x")[1]
    if request.method == "POST":
        BucketList().delete_activity(int(bucket_index), int(activity_index))
        return redirect('/ViewActivities/'+bucket_index)
    activity_item_chosen = BucketList().bucket_list[int(bucket_index)].activity_list[int(activity_index)]
    return render_template("DeleteBucketList.html", activity_item_chosen=activity_item_chosen )


