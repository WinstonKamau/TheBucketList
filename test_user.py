'''A test file for testing the user.py file'''
import unittest
#Importing the class u from the file user.py for testing
from app.user import Users

class UsersTestCase(unittest.TestCase):
    '''a class used to run tests on the Users class in user.py'''
    def setUp(self):
        '''creating an object from the user.py file'''
        self.user = Users()
    def test_login_entry(self):
        '''a method to test that the login in works'''
        result = self.user.login_user("user1", "password1")
        print("The default users ", self.user.users)
        print("The user entered ", self.user.user_name)
        print("The password entered "+self.user.password)
        self.assertEqual(result, "user logged in")
    def test_log_out_user(self):
        '''a method to test that the log out user function worked'''
        result = self.user.log_out_user()
        self.assertEqual(result, "user logged out")
    def test_create_user(self):
        '''a method to test that a user was created successfully'''
        self.user.create_user("user2", "password2", "password2")
        self.assertEqual(self.user.users, {"user1": "password1", "user2": "password2"})
if __name__ == '__main__':
    unittest.main()
