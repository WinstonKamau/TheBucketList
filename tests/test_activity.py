'''A test file for testing the BucketList class in models.py file'''
import unittest
#Importing the class BucketList from the file models.py for testing
from app.models import BucketList

class ActivitiesTestCase(unittest.TestCase):
    '''A class that tests the crud for creating updating reading
    and deleting activities '''
    def test_create_activity_happy_path(self):
        '''Testing that the create activity does create an activity object'''
        BucketList().create_bucket("Family")
        BucketList().create_activity(0, "Visit")
        self.assertEqual(BucketList().bucket_list[0].activity_list[0], "Visit")
    def test_create_activity_sad_path(self):
        '''Testing that the create activity does not create an activity object with an empty string'''
        BucketList().create_bucket("Family")
        BucketList().create_activity(0, "")
        self.assertEqual(len(BucketList().bucket_list[0].activity_list), 1)
    def test_edit_activity_happy_path(self):
        '''Testing that edit activity does edit the activity'''
        BucketList().create_bucket("Family")
        BucketList().create_activity(0, "Visit")
        BucketList().edit_activity(0 ,0 ,"Buy Gifts")
        self.assertEqual(BucketList().bucket_list[0].activity_list[0], "Buy Gifts")
    def test_edit_activity_sad_path(self):
        '''Testing that edit activity does not edit the activity if the activity is an empty string'''
        BucketList().create_bucket("Family")
        BucketList().create_activity(0, "Visit")
        BucketList().edit_activity(0 ,0 ,"")
        self.assertEqual(BucketList().bucket_list[0].activity_list[0], "")
    def test_delete_activity_happy_path(self):
        '''Testing that the delet activity deletes an activity object'''
        BucketList().delete_activity(0 , 0 )
        self.assertEqual(len(BucketList().bucket_list[0].activity_list), 0)

if __name__ == '__main__':
    unittest.main()
