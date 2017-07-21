'''A module that allows a user to register login and logout '''
from flask import redirect , url_for

from app.bucket_activities import BucketActivities

class Users():
    '''A class for users of the app'''
    def __init__(self):
        '''Initialising the variables for the Users class'''
        self.users = {"user1" : "password1"}
        self.bucket = BucketActivities
        self.user_buckets = {"user1":self.bucket}
        self.test = ""
    def login_user (self, user_name , password):
        '''a method for login in a user and ensuring that the user name and password is not blank'''
        if (user_name != "" and password != "" ):
            self.user_name = user_name
            self.password = password
            if self.user_name in self.users:
                if self.users.get(self.user_name)==self.password:
                    self.test = "user logged in"
                    return self.test
                else:
                    self.test = "invalid password"
            else:
                self.test = "invalid username"
        else:
            self.test = "username and password cannot be blank"     
    def log_out_user (self):
        '''a method for logging out the user'''
        self.test = "user logged out"
    def create_user(self, user_name, password, password_confirm):
        '''a method for creating a user'''
        if (user_name != "" and password != "" and isinstance( user_name , str )and password == password_confirm):
            self.user_name = user_name
            self.password = password
            self.users.update({self.user_name:self.password})
            self.user_buckets.update({self.user_name:self.bucket})
