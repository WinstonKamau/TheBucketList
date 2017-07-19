'''A test file for testing the login.py file'''
import unittest
#Importing the class Login assert from the file login.py for testing
from login import LoginAssert

class LoginTestCase(unittest.TestCase):
    def setUp(self):
        '''creating an object from the login.py file'''
        self.login_object = LoginAssert()
    def test_setting_all_blanks(self):
        '''Testing that the user_name and password are not set to blank
and that the method returns an error if this is done'''
        self.assertRaises(ValueError, self.login_object.set , "" , "" )
    def test_setting_one_blanks(self):
        '''Testing that if either username or password is blank that a
n error is raised'''  
        self.assertRaises(ValueError, self.login_object.set , "" , "ppp" )
        self.assertRaises(ValueError, self.login_object.set , "ppp" , "" )
    def test_username_not_number (self):
        '''Testing that the username is not a number'''
        self.assertRaises(ValueError, self.login_object.set , 1231 , "ppppp" )
    def test_password_checker(self):
        '''Testing that the password checker method is picking the right
password for the username'''
        self.assertRaises (ValueError , self.login_object.set , "Crispus" ,"poin" )
