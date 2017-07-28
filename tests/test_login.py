'''A test file for testing the login method'''
import unittest
from app.models import Users

class LoginTestCase(unittest.TestCase):
    '''a class used to run tests on the Users class in models.py'''
    def setUp(self):
        '''creating an object from the models.py file'''
        self.user = Users()
    def test_login_entry_happy_path(self):
        '''a method to test that the login in works happy path'''
        self.user.create_user("user1", "user1@gmail.com", "password1", "password1")
        print("The default users ", self.user.users)
        print("The user entered ", self.user.users[0].user_name)
        print("The user email entered ", self.user.users[0].user_email)
        print("The password entered "+self.user.users[0].user_password)
        boolean_for_login_user = self.user.login_user("user1@gmail.com", "password1")
        self.assertEqual(boolean_for_login_user, True)
    def test_login_entry_sad_path_1(self):
        '''a method to test that login does not work with wrong input of username'''
        self.user.create_user("user1", "user1@gmail.com", "password1", "password1")
        print("The default users ", self.user.users)
        print("The user entered ", self.user.users[0].user_name)
        print("The password entered "+self.user.users[0].user_password)
        boolean_for_login_user = self.user.login_user("user2@gmail.com", "password1")
        self.assertEqual(boolean_for_login_user, False)
    def test_login_entry_sad_path_2(self):
        '''a method to test that login does not work with wrong input of password'''
        self.user.create_user("user1", "user1@gmail.com", "password1", "password1")
        print("The default users ", self.user.users)
        print("The user entered ", self.user.users[0].user_name)
        print("The password entered "+self.user.users[0].user_password)
        boolean_for_login_user = self.user.login_user("user1@gmail.com", "password2")
        self.assertEqual(boolean_for_login_user, False)

    
if __name__ == '__main__':
    unittest.main()
