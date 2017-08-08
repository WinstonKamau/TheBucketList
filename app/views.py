'''A module used to return views.  '''
#importing the object render_template form flask for returning templates
from flask import render_template, request, redirect, url_for
from app import app
from app.models import Users
from app.models import BucketList

#binding register function to the url /Register
@app.route('/Register', methods=['GET', 'POST'])
def register():
    '''A method that returns the route of register in the html.  '''
    error = ""
    if request.method == "POST":
        user_name = request.form['username_register']
        user_email = request.form['useremail_register']
        password = request.form['password_register']
        new_password = request.form['confirm_new_password']
        if Users().create_user(user_name, user_email, password, new_password) == "all values okay":
            return redirect(url_for('login'))
        elif Users().create_user(user_name, user_email, password, new_password) == "similar email":
            error = user_email+" is already registered"
        elif Users().create_user(user_name, user_email, password, new_password) == "similar name":
            error = user_name+" is already registered"
        else:
            error = "Ensure that all fields have been inserted and that the passwords are the same!"
    return render_template("Register.html", error=error)

#binding create_bucket_list function to the url /CreateBucketList
#binding login function to the url /
@app.route('/', methods=['GET', 'POST'])
def login():
    '''A method that returns the route of login in the html.  '''
    error = ""
    if request.method == "POST":
        user_email = request.form['user_email_login']
        user_password = request.form['password_login']
        if Users().login_user(user_email, user_password):
            return redirect(url_for('view_bucket_list'))
        else:
            error = "Invalid email / password!"
    return render_template("Login.html", error=error)

@app.route('/CreateBucketList', methods=['GET', 'POST'])
def create_bucket_list():
    '''A method that returns the route of createbucketlist in the html.  '''
    error = ""
    if request.method == "POST":
        bucket_name = request.form['bucketlistcreated']
        if BucketList().create_bucket(bucket_name):
            return redirect(url_for('view_bucket_list'))
        else:
            if bucket_name == "":
                error = "Ensure that the bucket name is not an empty word!"
            else:
                error = "'"+bucket_name+"' already exists in the bucket list!"
    return render_template("CreateBucketList.html", error=error)

@app.route('/EditBucketList/<index>', methods=['GET', 'POST'])
def edit_bucket_list(index=None):
    '''A method that returns the route of the views if right input is made.  '''
    error = ""
    if request.method == "POST":
        new_name = request.form['new_name']
        if BucketList().edit_bucket(int(index), new_name):
            return redirect(url_for('view_bucket_list'))
        else:
            if new_name == "":
                error = "Bucket cannot be replaced with an empty string!"
            else:
                error = "'"+new_name+"' already exists in the bucket list!"
    bucket_items = BucketList().view_bucket()
    index_integer = int(index)
    return render_template("EditBucketList.html", error=error,
                           bucket_items=bucket_items, index_integer=index_integer)

@app.route('/DeleteBucketList/<index>', methods=['GET', 'POST'])
def delete_bucket_list(index=None):
    '''A method that returns the view for viewbucketlist after the user has opted to delete
    or to not delete.  '''
    if request.method == "POST":
        BucketList().delete_bucket(int(index))
        return redirect(url_for('view_bucket_list'))
    bucket_item_chosen = BucketList().view_bucket()[int(index)].bucket_name
    return render_template("DeleteBucketList.html", bucket_item_chosen=bucket_item_chosen)

#binding view_bucket_list function to the url /ViewBucketList
@app.route('/ViewBucketList', methods=['GET', 'POST'])
def view_bucket_list():
    '''A method that returns the route of viewbucketlist in the html.  '''
    prompt = "You currently have no bucketlists on the bucket list,"
    prompt += " press the create new bucket list button to create a new bucket!"
    if request.method == "POST":
        return redirect(url_for('create_bucket_list'))
    bucket_items = BucketList().view_bucket()
    name_of_user = Users().users[Users.get_id()].user_name
    if name_of_user.endswith('s'):
        name_of_user += "'"
    else:
        name_of_user += "'s"
    return render_template("ViewBucketList.html", bucket_items=bucket_items, prompt=prompt, name_of_user=name_of_user)

#binding view_activities function to the url /ViewActivities
@app.route('/ViewActivities/<index>')
def view_activities(index):
    '''A method that returns the route of viewactivities in the html.  '''
    activity_items = BucketList().view_activity(int(index))
    bucket_name = BucketList().view_bucket()[int(index)].bucket_name
    spacer = "x"
    prompt = "You currently have no activities on the activity list, "
    prompt += "press the create activity button to create a new activity!"
    return render_template("ViewActivities.html", activity_items=activity_items,
                           index=index, spacer=spacer, prompt=prompt, bucket_name=bucket_name)

#binding add_Activities function to the url /AddActivities
@app.route('/AddActivities/<bucket_index>', methods=['GET', 'POST'])
def add_activities(bucket_index):
    '''A method that returns the route of addactivities in the html.  '''
    error = ""
    if request.method == "POST":
        activity = request.form['theActivity']
        if BucketList().create_activity(int(bucket_index), activity):
            return redirect('/ViewActivities/'+bucket_index)
        else:
            if activity == "":
                error = "Ensure that the activity inserted is not an empty string!"
            else:
                error = "'"+activity+"' already exists in the activity list!"
    return render_template("AddActivities.html", error=error, bucket_index=bucket_index)

#binding add_Activities function to the url /AddActivities
@app.route('/EditActivity/<indices>', methods=['GET', 'POST'])
def edit_activities(indices):
    '''A method that returns the route of addactivities in the html.  '''
    error = ""
    bucket_index = indices.split("x")[0]
    activity_index = indices.split("x")[1]
    if request.method == "POST":
        new_activity = request.form['new_activity']
        if BucketList().edit_activity(int(bucket_index), int(activity_index), new_activity):
            return redirect('/ViewActivities/'+bucket_index)
        else:
            if new_activity == "":
                error = "An activity cannot be replaced with an empty string"
            else:
                error = "'"+new_activity+"' already exists in the activity list"
    the_activity = BucketList().view_bucket()[int(bucket_index)].activity_list[int(activity_index)]
    return render_template("EditActivity.html", error=error, the_activity=the_activity, bucket_index=bucket_index)

@app.route('/DeleteActivity/<indices>', methods=['GET', 'POST'])
def delete_activities(indices):
    '''A method that deletes an activity.  '''
    bucket_index = indices.split("x")[0]
    activity_index = indices.split("x")[1]
    if request.method == "POST":
        BucketList().delete_activity(int(bucket_index), int(activity_index))
        return redirect('/ViewActivities/'+bucket_index)
    activity_item_chosen = BucketList().view_bucket()[int(bucket_index)].activity_list[int(activity_index)]
    return render_template("DeleteActivity.html", activity_item_chosen=activity_item_chosen, bucket_index=bucket_index)

@app.route('/Logout')
def log_out():
    '''A method that logs out the user.  '''
    return redirect('/')
