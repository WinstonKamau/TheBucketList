'''A test file for testing the BucketList class in models.py file'''
import unittest
#Importing the class BucketList from the file models.py for testing
from app.models import BucketList

class BucketActivitiesTestCase(unittest.TestCase):
    '''A class that tests the crud for creating updating reading
    and deleting bucket lists '''
    def test_create_bucket_happy_path(self):
        '''Testing that the create bucket does create a bucket list object'''
        BucketList().create_bucket("Family")
        self.assertEqual(len(BucketList().bucket_list), 1)
    def test_create_bucket_happy_path_1(self):
        '''Testing that the create bucket does create a bucket list object with the right bucket name'''
        self.assertEqual(BucketList().bucket_list[0].bucket_name, "Family")
    def test_create_bucket_sad_path_(self):
        '''Testing that the create bucket does not create a bucket list object with an empty bucket name'''
        BucketList().create_bucket("")
        self.assertEqual(len(BucketList().bucket_list), 1)
    def test_edit_bucket_happy_path(self):
        '''Testing that the edit bucket does not edit a particulart bucket list object'''
        BucketList().edit_bucket(0, "Travel")
        self.assertEqual(BucketList().bucket_list[0].bucket_name, "Travel")
    def test_edit_bucket_sad_path(self):
        '''testing that the edit bucket does not edit once an empty string is given'''
        BucketList().edit_bucket(0, "")
        self.assertEqual(BucketList().bucket_list[0].bucket_name, "Travel")
    def test_delete_bucket_happy_path(self):
        '''Testing that the delete bucket does work'''
        BucketList().create_bucket("Adventure")
        BucketList().delete_bucket(1)
        self.assertEqual(len(BucketList().bucket_list), 1)

if __name__ == '__main__':
    unittest.main()
