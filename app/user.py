'''A module that allows a user to register login and logout '''
from flask import redirect , url_for

from app.bucket_activities import BucketActivities

class Users():
    def __init__(self):
        self.users = { "user1" : "password1"}
        self.bucket = BucketActivities
        self.user_buckets = {"user1":self.bucket}
    def login_user (self, user_name , password):
        if (user_name != "" and password != "" ):
                if isinstance ( user_name , str ):
                    self.user_name = user_name
                    self.password = password
                    if self.user_name in self.users:
                        if self.users.get(self.user_name)==self.password:
                            return "user logged in"

                    else:
                        return "user not logged in"
        
    def log_out_user (self):
        return "user logged out"
    def create_user(self, user_name, password, password_confirm):
            if user_name != "" and password != "" and isinstance ( user_name , str ) and password == password_confirm:
                self.user_name = user_name
                self.password = password
                self.users.update({self.user_name:self.password})
                self.user_buckets.update({self.user_name:self.bucket})



