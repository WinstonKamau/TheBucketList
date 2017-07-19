'''A test file for testing the activities.py file'''
import unittest
#Importing the class ActivitiesCrud from the file bucket_class.py for testing
from activities import ActivitiesCrud

class ActivitiesTestCase(unittest.TestCase):
    def setUp(self):
        '''creating an object from the activities.py file'''
        self.activities_object = ActivitiesCrud()
    def test_item_added_not_a_number(self):
        result = self.activities_object.create(1)
        self.assertNotEqual( result , 1)
    def test_item_added_not_empty_string(self):
        result = self.activities_object.create("")
        self.assertNotEqual( result , "")
    def test_item_added_not_repeated(self):
        self.activities_object.list_items = ["Family"]
        self.assertRaises(ValueError, self.activities_object.create , "Family" )
    def test_item_added_not_repeated_2(self):
        self.activities_object.list_items = ["faMiLy"]
        self.assertRaises(ValueError, self.activities_object.create , "Family" )
    def test_read(self):
        self.activities_object.list_items = [ "p" , "o"]
        result = self.activities_object.read()
        self.assertEqual ( result , [ "p" , "o"] )
    def test_delete(self):
        self.activities_object.list_items = [ "p" , "o"]
        result = self.activities_object.delete("o")
        self.assertEqual ( result , [ "p"] )
    def test_update(self):
        self.activities_object.list_items = [ "p" , "o"]
        result = self.activities_object.update("o" , "q")
        self.assertEqual ( result , [ "p" , "q"] )

