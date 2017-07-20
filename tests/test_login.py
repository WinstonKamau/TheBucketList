'''A test file for testing the user.py file'''
import unittest
#Importing the class u from the file user.py for testing
from app.user import Users

class LoginTestCase(unittest.TestCase):
    '''a class used to run tests on the Users class in user.py'''
    def setUp(self):
        '''creating an object from the user.py file'''
        self.user = Users()
    def test_login_entry(self):
        '''a method to test that the login in works'''
        self.user.login_user("user1", "password1")
        print("The default users ", self.user.users)
        print("The user entered ", self.user.user_name)
        print("The password entered "+self.user.password)
        self.assertEqual(self.user.test, "user logged in")
    def test_login_entry_1(self):
        '''a method to test that username is not blank'''
        self.user.login_user("", "password1")
        self.assertEqual(self.user.test, "username and password cannot be blank")
    def test_login_entry_2(self):
        '''a method to test that password is not blank'''
        self.user.login_user("user1", "")
        self.assertEqual(self.user.test, "username and password cannot be blank")
    def test_login_entry_3(self):
        '''a method to test that user entered invalid user name'''
        self.user.login_user("user", "password1")
        self.assertEqual(self.user.test, "invalid username")
    def test_login_entry_4(self):
        '''a method to test that user entered invalid password'''
        self.user.login_user("user1", "password")
        self.assertEqual(self.user.test, "invalid password")
    def test_log_out_user(self):
        '''a method to test that the log out user function worked'''
        self.user.log_out_user()
        self.assertEqual(self.user.test, "user logged out")
    
if __name__ == '__main__':
    unittest.main()
