'''A test file for testing the login method'''
import unittest
#Importing the modules.py file to access its global variables
from app import models
#Importing the class Users from the module models.py
from app.models import Users

class LoginTestCase(unittest.TestCase):
    '''a class used to run tests on the Users class in models.py'''
    def setUp(self):
        '''creating an object from the models.py file'''
        self.user = Users()
    def test_login_entry_happy_path(self):
        '''a method to test that the login in works happy path'''
        models.users.clear()
        self.user.create_user("user1", "user1@gmail.com", "password1", "password1")
        boolean_for_login_user = self.user.login_user("user1@gmail.com", "password1")
        self.assertEqual(boolean_for_login_user, True)
    def test_login_entry_sad_path_1(self):
        '''a method to test that login does not work with wrong input of user email'''
        models.users.clear()
        self.user.create_user("user1", "user1@gmail.com", "password1", "password1")
        boolean_for_login_user = self.user.login_user("user2@gmail.com", "password1")
        self.assertEqual(boolean_for_login_user, None)
    def test_login_entry_sad_path_2(self):
        '''a method to test that login does not work with wrong input of password'''
        models.users.clear()
        self.user.create_user("user1", "user1@gmail.com", "password1", "password1")
        boolean_for_login_user = self.user.login_user("user1@gmail.com", "password2")
        self.assertEqual(boolean_for_login_user, None)
    def test_login_sets_right_user_id(self):
        '''a method to test that the right user id is set on login'''
        models.users.clear()
        self.user.create_user("user1", "user1@gmail.com", "password1", "password1")
        self.user.create_user("user2", "user2@gmail.com", "password2", "password2")
        self.user.create_user("user3", "user3@gmail.com", "password3", "password3")
        self.user.login_user("user3@gmail.com", "password3")
        self.assertEqual(models.user_id, 2)
        self.user.login_user("user2@gmail.com", "password2")
        self.assertEqual(models.user_id, 1)
        self.user.login_user("user1@gmail.com", "password1")
        self.assertEqual(models.user_id, 0)
    

    
if __name__ == '__main__':
    unittest.main()
