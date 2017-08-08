'''A module called models.py that has two classes for Users and Bucket Lists
that is used to create and log in users and to create edit view and delete bucket
names and activities.
'''

USER_ID = 0
class Users(object):
    '''A class for users of the app.  '''


    users = []
    def __init__(self, user_name=None, user_email=None, user_password=None):
        '''Initialising the variables for the Users class.  '''
        if user_name and user_password and user_email:
            self.user_name = user_name
            self.user_email = user_email
            self.user_password = user_password
            self.user_bucket = []
        else:
            self.user_name = None
            self.user_email = None
            self.user_password = None

    def create_user(self, user_name, user_email, password, password_confirm):
        '''A method for creating a user.  '''
        for user_object in self.users:
            if user_object.user_email == user_email:
                return "similar email"
        for user_object in self.users:
            if user_object.user_name == user_name:
                return "similar name"
        if user_name != "" and user_email != "" and password != "" and password == password_confirm:
            user = Users(user_name, user_email, password)
            self.users.append(user)
            return "all values okay"

    def login_user(self, user_email, password):
        '''A method for login in a user and ensuring that the user name and password is
        not blank.
        '''
        global USER_ID
        for member in self.users:
            if member.user_email == user_email and member.user_password == password:
                USER_ID = self.users.index(member)
                return True

    @classmethod
    def get_id(cls):
        '''A method to return the user_id'''
        return USER_ID

class BucketList(object):
    '''A class for the bucketlist.  '''


    def __init__(self, bucket_name=None):
        '''Initialising the attributes for the BucketList.  '''
        if bucket_name:
            self.bucket_name = bucket_name
            self.activity_list = []
        else:
            self.bucket_name = None
            self.activity_list = []

    @staticmethod
    def create_bucket(bucket_name):
        '''A method to create a bucket.  '''
        similar_names = False
        for bucket_object in Users().users[Users().get_id()].user_bucket:
            if bucket_object.bucket_name.lower() == bucket_name.lower():
                similar_names = True
        if bucket_name != "" and similar_names is False:
            bucket = BucketList(bucket_name)
            Users().users[Users().get_id()].user_bucket.append(bucket)
            return True

    @staticmethod
    def view_bucket():
        '''A method to return a bucket for a user.  '''
        return Users().users[Users().get_id()].user_bucket

    @staticmethod
    def edit_bucket(bucket_index, new_name):
        '''A method to edit a bucket object its bucket name.  '''
        similar_names = False
        for bucket_object in Users().users[Users().get_id()].user_bucket:
            if bucket_object.bucket_name.lower() == new_name.lower():
                similar_names = True
        if new_name != "" and similar_names is False:
            Users().users[Users().get_id()].user_bucket[bucket_index].bucket_name = new_name
            return True

    @staticmethod
    def delete_bucket(bucket_index):
        '''A method to remove a bucket object.  '''
        Users().users[Users().get_id()].user_bucket.pop(bucket_index)

    @staticmethod
    def create_activity(bucket_index, new_activity):
        '''A method to create an activity.  '''
        similar_names = False
        for activity_object in Users().users[Users().get_id()].user_bucket[bucket_index].activity_list:
            if activity_object.lower() == new_activity.lower():
                similar_names = True
        if new_activity != "" and similar_names is False:
            Users().users[Users().get_id()].user_bucket[bucket_index].activity_list.append(new_activity)
            return True

    @staticmethod
    def view_activity(bucket_index):
        '''A method to return an activity list for a user.  '''
        return Users().users[Users().get_id()].user_bucket[bucket_index].activity_list

    @staticmethod
    def edit_activity(bucket_index, index_of_activity, edited_activity):
        '''A method to edit an activity.  '''
        similar_names = False
        for activity_object in Users().users[Users().get_id()].user_bucket[bucket_index].activity_list:
            if activity_object.lower() == edited_activity.lower():
                similar_names = True
        if edited_activity != "" and similar_names is False:
            Users().users[Users().get_id()].user_bucket[bucket_index].activity_list[index_of_activity] = edited_activity
            return True

    @staticmethod
    def delete_activity(bucket_index, index_of_activity):
        '''A method to delete an activity.  '''
        Users().users[Users().get_id()].user_bucket[bucket_index].activity_list.pop(index_of_activity)
