'''A module that allows a user to register login and logout '''
from flask import redirect , url_for

from bucket_activities import BucketActivities
users = { "user1" : "password1"}

user_buckets = {"user1":BucketActivities()}
def login_user (self, user_name , password):
    if (user_name != "" and password != "" ):
            if isinstance ( user_name , str ):
                self.user_name = user_name
                self.password = password
                if self.user_name in users == True:
                    if users.get(self.user_name)== self.password:
                        return redirect(url_for('view_bucket_list'))
    
def log_out_user (self):
    return redirect(url_for('login'))
def create_user(self, user_name, password, password_confirm):
        if user_id != "" and password != "" and isinstance ( user_id , str ) and password == password_confirm:
            self.user_name = user_name
            self.password = password
            users.update({self.user_name:self.password})
            user_buckets.update({self.user_name:Bucket(self)})
        return redirect(url_for('view_bucket_list'))



