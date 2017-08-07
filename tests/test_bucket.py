'''A test file for testing the BucketList class in models.py file'''
import unittest
#Importing the module models.py to access its global variable users
from app import models
#Importing the class Users from the file models.py
from app.models import Users
#Importing the class BucketList from the file models.py for testing
from app.models import BucketList

class BucketActivitiesTestCase(unittest.TestCase):
    '''A class that tests the crud for creating updating reading
    and deleting bucket lists '''
    def test_create_bucket_happy_path(self):
        '''Testing that the create bucket does create a bucket list object'''
        models.users.clear()
        Users().create_user("user1", "user1@gmail.com", "password", "password")
        Users().login_user("user1@gmail.com", "password")
        BucketList().create_bucket("Family")
        self.assertEqual(len(models.users[0].user_bucket), 1)
    def test_create_bucket_happy_path_1(self):
        '''Testing that the create bucket does create a bucket list object with the right bucket name'''
        models.users.clear()
        Users().create_user("user1", "user1@gmail.com", "password", "password")
        Users().login_user("user1@gmail.com", "password")
        BucketList().create_bucket("Family")
        self.assertEqual(models.users[0].user_bucket[0].bucket_name, "Family")
    def test_create_bucket_sad_path(self):
        '''Testing that the create bucket does not create a bucket list object with an empty bucket name'''
        models.users.clear()
        Users().create_user("user1", "user1@gmail.com", "password", "password")
        Users().login_user("user1@gmail.com", "password")
        BucketList().create_bucket("Family")
        BucketList().create_bucket("")
        self.assertEqual(len(models.users[0].user_bucket), 1)
    def test_create_bucket_sad_path_1(self):
        '''Testing that the create bucket does not create a bucket list object
        that is similar in name to a previous bucket object name created'''
        models.users.clear()
        Users().create_user("user1", "user1@gmail.com", "password", "password")
        Users().login_user("user1@gmail.com", "password")
        BucketList().create_bucket("Family")
        BucketList().create_bucket("Family")
        self.assertEqual(len(models.users[0].user_bucket), 1)
    def test_edit_bucket_happy_path(self):
        '''Testing that the edit bucket edit a particular bucket list object with 
        right arguments entered'''
        models.users.clear()
        Users().create_user("user1", "user1@gmail.com", "password", "password")
        Users().login_user("user1@gmail.com", "password")
        BucketList().create_bucket("Family")
        BucketList().edit_bucket(0, "Travel")
        self.assertEqual(models.users[0].user_bucket[0].bucket_name, "Travel")
    def test_edit_bucket_sad_path(self):
        '''testing that the edit bucket does not edit once an empty string is given
        or when a bucket name entered already exists in the user's bucket list'''
        models.users.clear()
        Users().create_user("user1", "user1@gmail.com", "password", "password")
        Users().login_user("user1@gmail.com", "password")
        BucketList().create_bucket("Family")
        BucketList().edit_bucket(0, "")
        self.assertEqual(models.users[0].user_bucket[0].bucket_name, "Family")
        BucketList().create_bucket("Travel")
        BucketList().edit_bucket(0, "Travel")
        self.assertEqual(models.users[0].user_bucket[0].bucket_name, "Family")
    def test_delete_bucket_happy_path(self):
        '''Testing that the delete bucket does work'''
        models.users.clear()
        Users().create_user("user1", "user1@gmail.com", "password", "password")
        Users().login_user("user1@gmail.com", "password")
        BucketList().create_bucket("Family")
        BucketList().delete_bucket(0)
        self.assertEqual(len(models.users[0].user_bucket), 0)

if __name__ == '__main__':
    unittest.main()
