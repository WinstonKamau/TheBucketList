'''A module that allows a user to register login and logout '''
from flask import redirect, url_for

from app.bucket_activities import BucketActivities

class Users(object):
    '''A class for users of the app'''
    users = []
    def __init__(self, user_name = None, user_email= None, user_password= None):
        '''Initialising the variables for the Users class'''
        if user_name and user_password and user_email:
            self.user_name = user_name
            self.user_email = user_email
            self.user_password = user_password
        else:
            self.user_name = None
            self.user_email = None
            self.user_password = None
    def login_user (self, user_email, password):
        '''a method for login in a user and ensuring that the user name and password is not blank'''
        for member in self.users:
            if member.user_email == user_email:
                if member.user_password == password:
                    return True

    def log_out_user (self):
        '''a method for logging out the user'''
        self.test = "user logged out"
    def create_user(self, user_name, user_email, password, password_confirm):
        '''a method for creating a user'''
        if (user_name != "" and password != "" and isinstance( user_name , str )and password == password_confirm):
            user = Users(user_name, user_email, password)
            self.users.append(user)
            return True
class BucketList(object):
    '''a class for the bucketlist'''
    bucket_list = []
    def __init__(self, bucket_name=None):
        if bucket_name:
            self.bucket_name = bucket_name
            self.activity_list = []
        else:
            self.bucket_name = None
            self.activity_list = []
    def create_bucket(self, bucket_name):
        bucket = BucketList ( bucket_name )
        self.bucket_list.append(bucket)
    def view_bucket(self):
        return self.bucket_list
    def edit_bucket(self, the_index, new_name):
        self.bucket_list[the_index].bucket_name = new_name
    def delete_bucket(self, the_index):
        self.bucket_list.pop(the_index)
    def create_activity(self, the_index, new_activity):
        self.bucket_list[the_index].activity_list.append(new_activity)
    def edit_activity(self, the_index, index_of_activity, edited_activity):
        self.bucket_list[the_index].activity_list[index_of_activity] = edited_activity
    def delete_activity(self, the_index, index_of_activity):
        self.bucket_list[the_index].activity_list.pop(the_index)