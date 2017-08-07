users = []
user_id = 0
class Users(object):
    '''A class for users of the app'''
    def __init__(self, user_name = None, user_email= None, user_password= None):
        '''Initialising the variables for the Users class'''
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
        '''a method for creating a user'''
        global users
        for user_object in users:
            if user_object.user_email==user_email:
                return "similar email"
        for user_object in users:
            if user_object.user_name==user_name:
                return "similar name"
        if user_name != "" and user_email != "" and password != "" and password == password_confirm:
            user = Users(user_name, user_email, password)
            users.append(user)
            return "all values okay"
    def login_user(self, user_email, password):
        '''a method for login in a user and ensuring that the user name and password is not blank'''
        global users
        global user_id
        for member in users:
            if member.user_email == user_email and member.user_password == password:
                user_id = users.index(member)
                return True
class BucketList(object):
    '''a class for the bucketlist'''
    def __init__(self, bucket_name=None):
        if bucket_name:
            self.bucket_name = bucket_name
            self.activity_list = []
        else:
            self.bucket_name = None
            self.activity_list = []
    def create_bucket(self, bucket_name):
        ''' a method to create a bucket'''
        global users
        global user_id
        similar_names = False
        for bucket_object in users[user_id].user_bucket:
            if bucket_object.bucket_name.lower() == bucket_name.lower():
                similar_names = True
        if bucket_name != "" and similar_names == False:
            bucket = BucketList ( bucket_name )
            users[user_id].user_bucket.append (bucket)
            return True
    def view_bucket(self):
        global users
        global user_id
        return users[user_id].user_bucket
    def edit_bucket(self, bucket_index, new_name):
        ''' a method to edit a bucket object its bucket name'''
        global users
        global user_id
        similar_names = False
        for bucket_object in users[user_id].user_bucket:
            if bucket_object.bucket_name.lower() == new_name.lower():
                similar_names = True
        if new_name != "" and similar_names == False:
            users[user_id].user_bucket[bucket_index].bucket_name = new_name
            return True
    def delete_bucket(self, bucket_index):
        ''' a method to remove a bucket object'''
        global users
        global user_id
        users[user_id].user_bucket.pop(bucket_index)
    def create_activity(self, bucket_index, new_activity):
        '''a method to create an activity '''
        global users
        global user_id
        similar_names = False
        for activity_object in users[user_id].user_bucket[bucket_index].activity_list:
            if activity_object.lower() == new_activity.lower():
                similar_names = True
        if new_activity != "" and similar_names == False:
            users[user_id].user_bucket[bucket_index].activity_list.append(new_activity)
            return True
    def view_activity(self, bucket_index):
        global users
        global user_id
        return users[user_id].user_bucket[bucket_index].activity_list
    def edit_activity(self, bucket_index, index_of_activity, edited_activity):
        ''' a method to edit an activity'''
        global users
        global user_id
        similar_names = False
        for activity_object in users[user_id].user_bucket[bucket_index].activity_list:
            if activity_object.lower() == edited_activity.lower():
                similar_names = True
        if edited_activity != "" and similar_names == False:
            users[user_id].user_bucket[bucket_index].activity_list[index_of_activity]= edited_activity
            return True
    def delete_activity(self, bucket_index, index_of_activity):
        ''' a method to delet an activity'''
        global users
        global user_id
        users[user_id].user_bucket[bucket_index].activity_list.pop(index_of_activity)
