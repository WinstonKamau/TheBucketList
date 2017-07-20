'''A test file for testing the bucket_activities.py file'''
import unittest
#Importing the class BucketActivities from the file bucket_activities.py for testing
from app.bucket_activities import BucketActivities

class BucketActivitiesTestCase(unittest.TestCase):
    '''A class that tests the crud for creating updating reading
    and deleting bucket lists and activities'''
    def setUp(self):
        '''creating an object from the bucket_activities.py file'''
        self.bucket = BucketActivities()
    def test_create_bucket(self):
        '''Testing that the create bucket does create a bucket list'''
        self.bucket.create_bucket("Family")
        self.assertEqual(self.bucket.list_items.__contains__("Family"), True)
    def test_create_bucket_1(self):
        '''Testing that the create bucket does not create a bucket list if argument is an empty string'''
        self.bucket.create_bucket("")
        self.assertEqual(self.bucket.list_items, {"":[]})
    def test_update_bucket(self):
        '''Testing that the update bucket does update a bucket list appropriately'''
        self.bucket.list_items = {"Family": ["visit"]}
        self.bucket.update_bucket("Family", "Travel")
        self.assertEqual(self.bucket.list_items, {"Travel": ["visit"]})
    def test_update_bucket_1(self):
        '''Testing that the update bucket does not update a bucket list if string is empty'''
        self.bucket.list_items = {"Family": ["visit"]}
        self.bucket.update_bucket("Family", "")
        self.assertEqual(self.bucket.list_items, {"Family": ["visit"]})
    def test_delete_bucket(self):
        '''Testing that the delete bucket does delete a bucket list appropriately'''
        self.bucket.list_items = {"Family":["visit"], "Travel" : ["Algeria"]}
        self.bucket.delete_bucket("Family")
        self.assertEqual(self.bucket.list_items, {"Travel": ["Algeria"]})
    def test_create_activity(self):
        '''Testing that the create activity does create an activity list'''
        self.bucket.list_items = {"Adventure" : ["hiking"]}
        self.bucket.create_activity("Adventure", "snowing")
        self.assertEqual(self.bucket.list_items, {"Adventure" : ["hiking", "snowing"]})
    def test_update_activity(self):
        '''Testing that the update activity does update an activity list appropriately'''
        self.bucket.list_items = {"Family": ["visit"]}
        self.bucket.update_activity("Family", "visit", "gettogether")
        self.assertEqual(self.bucket.list_items, {"Family":["gettogether"]})
    def test_delete_activity(self):
        '''Testing that the delete activity does delete an activity appropriately'''
        self.bucket.list_items = {"Family": ["visit", "gettogether"]}
        self.bucket.delete_activity("Family", "visit")
        self.assertEqual(self.bucket.list_items, {"Family":["gettogether"]})

if __name__ == '__main__':
    unittest.main()
