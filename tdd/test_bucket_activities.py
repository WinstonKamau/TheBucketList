'''A test file for testing the bucket_activities.py file'''
import unittest
#Importing the class BucketActivities from the file bucket_activities.py for testing
from bucket_activities import BucketActivities

class BucketActivitiesTestCase(unittest.TestCase):
    def setUp(self):
        '''creating an object from the bucket_activities.py file'''
        self.bucket = BucketActivities()
    def test_dict_length (self):
        '''Test that the create_bucket method only adds one bucket list
and not more'''
        self.bucket.create_bucket("pointer")
        self.assertEqual(len(self.bucket.list_items) , 1 )
    def test_entry_of_bucket_name(self):
        '''Test that the bucket name entered is not an empty string'''
        self.assertRaises (ValueError, self.bucket.create_bucket , "" )
    def test_entry_of_bucket_name_2(self):
        '''Test that the bucket name entered is not a number'''
        self.assertRaises (ValueError, self.bucket.create_bucket , 1 )
    def test_dict_length_2 (self):
        '''Test that the update method only adds one bucket list
and not more'''
        self.bucket.list_items = {"p" : self.bucket.activity_list} 
        self.bucket.update_bucket("p" , "q")
        self.assertEqual(len(self.bucket.list_items) , 1 )
    def test_entry_of_update_bucket_name(self):
        '''Test that the bucket name entered is not an empty string'''
        self.bucket.list_items = {"p" : self.bucket.activity_list}
        self.bucket.update_bucket ( "p" , "")
        self.assertEqual (self.bucket.list_items ,{"p" : self.bucket.activity_list}  )
    def test_entry_of_update_bucket_name_2(self):
        '''Test that the bucket name entered is not a number'''
        self.bucket.list_items = {"p" : self.bucket.activity_list}
        self.bucket.update_bucket ( "p" , "")
        self.assertEqual (self.bucket.list_items ,{"p" : self.bucket.activity_list}  )
    def test_delete_bucket(self):
        '''Test successful delete of a bucket list'''
        self.bucket.list_items = {"p" : ["q"]}
        self.bucket.delete_bucket ()
        self.assertEqual (self.bucket.list_items ,{"" :[]}  )
    def test_create_activity(self):
        '''Test activity not to be empty string'''
        list_length = len(self.bucket.activity_list)
        self.bucket.create_activity("")
        self.assertEqual (len(self.bucket.activity_list) , list_length)
    def test_create_activity_2(self):
        '''Test activity not to be a number'''
        list_length = len(self.bucket.activity_list)
        self.bucket.create_activity(1)
        self.assertEqual (len(self.bucket.activity_list) , list_length)
    def test_create_activity_3(self):
        '''Test that activity created is not repeated'''
        self.bucket.activity_list = [ "2" , "5"]
        self.assertRaises (ValueError , self.bucket.create_activity , "2" )
    def test_delete_activity(self):
        '''Test that activity chosen is deleted'''
        self.bucket.activity_list = [ "2" , "5"]
        self.bucket.delete_activity("2")
        self.assertEqual (self.bucket.activity_list , ["5"])
    def test_update_activity(self):
        '''Test that update world'''
        self.bucket.activity_list = [ "2" , "5"]
        self.bucket.update_activity("2" , "3")
        self.assertEqual (self.bucket.activity_list , ["3","5"])
    
