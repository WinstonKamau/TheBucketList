'''A test file for testing the user.py file'''
import unittest
#Importing the class u from the file user.py for testing
from app.user import Users

class RegisterTestCase(unittest.TestCase):
    def setUp(self):
        '''creating an object from the user.py file'''
        self.user = Users()
    def test_create_user(self):
        '''a method to test that a user was created successfully'''
        self.user.create_user("user2", "password2", "password2")
        self.assertEqual(self.user.users, {"user1": "password1", "user2": "password2"})
    def test_create_user_1(self):
        '''a method to test that a user was not created with blank username'''
        self.user.create_user("", "password2", "password2")
        self.assertEqual(self.user.users, {"user1": "password1"})
    def test_create_user_2(self):
        '''a method to test that a user was not created with blank password'''
        self.user.create_user("user2", "", "")
        self.assertEqual(self.user.users, {"user1": "password1"})
    def test_create_user_3(self):
        '''a method to test that a user was not created with non - matching passwords password'''
        self.user.create_user("user2", "password1", "Password1")
        self.assertEqual(self.user.users, {"user1": "password1"})
if __name__ == '__main__':
    unittest.main()