'''A test file for testing the Activity List in the BucketList class in models.py file.  '''
import unittest
from app import models
from app.models import Users
from app.models import BucketList


class ActivitiesTestCase(unittest.TestCase):
    '''A class that tests the crud for creating updating reading
    and deleting activities.
    '''


    def test_create_activity_happy_path(self):
        '''Testing that the create activity does create an activity object
        with the right inputs.
        '''
        models.users.clear()
        Users().create_user("user1", "user1@gmail.com", "password", "password")
        Users().login_user("user1@gmail.com", "password")
        BucketList().create_bucket("Family")
        BucketList().create_activity(0, "Visit")
        self.assertEqual(models.users[0].user_bucket[0].activity_list[0], "Visit")

    def test_create_activity_sad_path(self):
        '''Testing that the create activity does not create an activity object with an
         empty string.
        '''
        models.users.clear()
        Users().create_user("user1", "user1@gmail.com", "password", "password")
        Users().login_user("user1@gmail.com", "password")
        BucketList().create_bucket("Family")
        BucketList().create_activity(0, "Visit my aunt")
        BucketList().create_activity(0, "")
        self.assertEqual(len(models.users[0].user_bucket[0].activity_list), 1)

    def test_create_activity_sad_path_1(self):
        '''Testing that the create activity does not create an activity that was created
        before.
        '''
        models.users.clear()
        Users().create_user("user1", "user1@gmail.com", "password", "password")
        Users().login_user("user1@gmail.com", "password")
        BucketList().create_bucket("Family")
        BucketList().create_activity(0, "Visit my aunt")
        BucketList().create_activity(0, "Visit my aunt")
        self.assertEqual(len(models.users[0].user_bucket[0].activity_list), 1)

    def test_edit_activity_happy_path(self):
        '''Testing that edit activity does edit an activity with the right input.  '''
        models.users.clear()
        Users().create_user("user1", "user1@gmail.com", "password", "password")
        Users().login_user("user1@gmail.com", "password")
        BucketList().create_bucket("Family")
        BucketList().create_activity(0, "Visit")
        BucketList().edit_activity(0, 0, "Buy Gifts")
        self.assertEqual(models.users[0].user_bucket[0].activity_list[0], "Buy Gifts")

    def test_edit_activity_sad_path(self):
        '''Testing that edit activity does not edit the activity if the activity input
        is an empty string.
        '''
        models.users.clear()
        Users().create_user("user1", "user1@gmail.com", "password", "password")
        Users().login_user("user1@gmail.com", "password")
        BucketList().create_bucket("Family")
        BucketList().create_activity(0, "Visit")
        BucketList().edit_activity(0, 0, "")
        self.assertEqual(models.users[0].user_bucket[0].activity_list[0], "Visit")

    def test_edit_activity_sad_path_1(self):
        '''Testing that edit activity does not edit the activity if the activity input
        was already entered.
        '''
        models.users.clear()
        Users().create_user("user1", "user1@gmail.com", "password", "password")
        Users().login_user("user1@gmail.com", "password")
        BucketList().create_bucket("Family")
        BucketList().create_activity(0, "Visit aunt")
        BucketList().create_activity(0, "Visit sister")
        BucketList().edit_activity(0, 0, "Visit sister")
        self.assertEqual(models.users[0].user_bucket[0].activity_list[0], "Visit aunt")

    def test_delete_activity_happy_path(self):
        '''Testing that delete activity deletes an activity object.  '''
        models.users.clear()
        Users().create_user("user1", "user1@gmail.com", "password", "password")
        Users().login_user("user1@gmail.com", "password")
        BucketList().create_bucket("Family")
        BucketList().create_activity(0, "Visit")
        BucketList().delete_activity(0, 0)
        self.assertEqual(len(models.users[0].user_bucket[0].activity_list), 0)

if __name__ == '__main__':
    unittest.main()
