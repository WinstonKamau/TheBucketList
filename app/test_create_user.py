'''A test file for testing the user.py file'''
import unittest
#Importing the class u from the file user.py for testing
from app.models import Users

class RegisterTestCase(unittest.TestCase):
    def setUp(self):
        '''creating an object from the user.py file'''
        self.user = Users()
    def test_create_user_happy_path(self):
        '''a method to test that a user was created successfully with all inputs'''
        self.user.create_user("user4", "user4@gmail.com", "password2", "password2")
        self.assertEqual(self.user.users[0].user_name, "user4")
        self.assertEqual(self.user.users[0].user_email, "user4@gmail.com")
        self.assertEqual(self.user.users[0].user_password, "password2")
    def test_create_user_sad_path(self):
        '''a method to test that a user was not created with non - matching passwords'''
        self.user.create_user("user2", "user2@gmail.com", "password1", "password2")
        self.assertEqual(len(self.user.users), 1)
    def test_create_user_sad_path_2(self):
        '''a method to test that a user was not created with empty user name'''
        self.user.create_user("", "user2@gmail.com", "password1", "password2")
        self.assertEqual(len(self.user.users), 1)
    def test_create_user_sad_path_3(self):
        '''a method to test that a user was not created with empty password'''
        self.user.create_user("user2", "user2@gmail.com", "", "")
        self.assertEqual(len(self.user.users), 1)
    def test_create_user_sad_path_4(self):
        '''a method to test that a user was not created with empty email'''
        self.user.create_user("user2", "", "ppp", "ppp")
        self.assertEqual(len(self.user.users), 1)
if __name__ == '__main__':
    unittest.main()