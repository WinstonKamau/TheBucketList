'''A test file for testing the bucket_class.py file'''
import unittest
#Importing the class BucketCrud from the file bucket_class.py for testing
from bucket_class import BucketCrud

class BucketTestCase(unittest.TestCase):
    def setUp(self):
        '''creating an object from the bucket_class.py file'''
        self.bucket_object = BucketCrud()
    def test_bucket_item_added_not_a_number(self):
        result = self.bucket_object.create(1)
        self.assertNotEqual( result , 1)
    def test_bucket_item_added_not_empty_string(self):
        result = self.bucket_object.create("")
        self.assertNotEqual( result , "")
    def test_bucket_item_added_not_repeated(self):
        self.bucket_object.list_items = ["Family"]
        self.assertRaises(ValueError, self.bucket_object.create , "Family" )
    def test_bucket_item_added_not_repeated_2(self):
        self.bucket_object.list_items = ["faMiLy"]
        self.assertRaises(ValueError, self.bucket_object.create , "Family" )
    def test_read(self):
        self.bucket_object.list_items = [ "p" , "o"]
        result = self.bucket_object.read()
        self.assertEqual ( result , [ "p" , "o"] )
    def test_delete(self):
        self.bucket_object.list_items = [ "p" , "o"]
        result = self.bucket_object.delete("o")
        self.assertEqual ( result , [ "p"] )
    def test_update(self):
        self.bucket_object.list_items = [ "p" , "o"]
        result = self.bucket_object.update("o" , "q")
        self.assertEqual ( result , [ "p" , "q"] )
