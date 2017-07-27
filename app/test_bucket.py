'''A test file for testing the BucketList class in models.py file'''
import unittest
#Importing the class BucketList from the file models.py for testing
from app.models import BucketList

class BucketActivitiesTestCase(unittest.TestCase):
    '''A class that tests the crud for creating updating reading
    and deleting bucket lists '''
    def setUp(self):
        '''creating an object from the models.py file'''
        self.bucket = BucketList()
    def test_create_bucket_happy_path(self):
        '''Testing that the create bucket does create a bucket list object'''
        self.bucket.create_bucket("Family")
        self.assertEqual(self.bucket.bucket_list[0].bucket_name, "Family")
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
