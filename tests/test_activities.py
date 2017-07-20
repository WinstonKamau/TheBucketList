'''A test file for testing the bucket_activities.py file'''
import unittest
#Importing the class BucketActivities from the file bucket_activities.py for testing

from .. import bucket_activities

class ActivitiesTestCase(unittest.TestCase):
    '''A class that tests the crud for creating updating reading
    and deleting bucket lists and activities'''
    def setUp(self):
        '''creating an object from the bucket_activities.py file'''
        self.activity = BucketActivities()
    def test_create_activity(self):
        '''Testing that the create activity does create an activity list'''
        self.activity.list_items = {"Adventure" : ["hiking"]}
        self.activity.create_activity("Adventure", "snowing")
        self.assertEqual(self.activity.list_items, {"Adventure" : ["hiking", "snowing"]})
    def test_create_activity_1(self):
        '''Testing that the create activity does not create an activity list if it is blank'''
        self.activity.list_items = {"Adventure" : ["hiking"]}
        self.activity.create_activity("Adventure", "")
        self.assertEqual(self.activity.list_items, {"Adventure" : ["hiking"]})
    def test_update_activity(self):
        '''Testing that the update activity does update an activity list appropriately'''
        self.activity.list_items = {"Family": ["visit"]}
        self.activity.update_activity("Family", "visit", "gettogether")
        self.assertEqual(self.activity.list_items, {"Family":["gettogether"]})
    def test_update_activity_1(self):
        '''Testing that the update activity does update an activity list if it is blank'''
        self.activity.list_items = {"Family": ["visit"]}
        self.activity.update_activity("Family", "visit", "")
        self.assertEqual(self.activity.list_items, {"Family":["visit"]})
    def test_delete_activity(self):
        '''Testing that the delete activity does delete an activity appropriately'''
        self.activity.list_items = {"Family": ["visit", "gettogether"]}
        self.activity.delete_activity("Family", "visit")
        self.assertEqual(self.activity.list_items, {"Family":["gettogether"]})

if __name__ == '__main__':
    unittest.main()
