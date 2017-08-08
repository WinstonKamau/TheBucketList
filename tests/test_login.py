'''A test file for testing the login method.  '''
import unittest
from app import models
from app.models import Users


class LoginTestCase(unittest.TestCase):
    '''A class used to run tests on the Users class in models.py.  '''


    def setUp(self):
        '''Creating an object from the models.py file for the class Users.  '''
        self.user = Users()

    def test_login_entry_happy_path(self):
        '''A method to test that the login in works with the right inputs.  '''
        self.user.users.clear()
        self.user.create_user("user1", "user1@gmail.com", "password1", "password1")
        boolean_for_login_user = self.user.login_user("user1@gmail.com", "password1")
        self.assertEqual(boolean_for_login_user, True)

    def test_login_entry_sad_path_1(self):
        '''A method to test that login does not work with wrong input of user email.  '''
        self.user.users.clear()
        self.user.create_user("user1", "user1@gmail.com", "password1", "password1")
        boolean_for_login_user = self.user.login_user("user2@gmail.com", "password1")
        self.assertEqual(boolean_for_login_user, None)

    def test_login_entry_sad_path_2(self):
        '''A method to test that login does not work with wrong input of password.  '''
        self.user.users.clear()
        self.user.create_user("user1", "user1@gmail.com", "password1", "password1")
        boolean_for_login_user = self.user.login_user("user1@gmail.com", "password2")
        self.assertEqual(boolean_for_login_user, None)

    def test_login_sets_right_user_id(self):
        '''A method to test that the right user id is set on login.  '''
        self.user.users.clear()
        self.user.create_user("user1", "user1@gmail.com", "password1", "password1")
        self.user.create_user("user2", "user2@gmail.com", "password2", "password2")
        self.user.create_user("user3", "user3@gmail.com", "password3", "password3")
        self.user.login_user("user3@gmail.com", "password3")
        self.assertEqual(models.USER_ID, 2)
        self.user.login_user("user2@gmail.com", "password2")
        self.assertEqual(models.USER_ID, 1)
        self.user.login_user("user1@gmail.com", "password1")
        self.assertEqual(models.USER_ID, 0)

if __name__ == '__main__':
    unittest.main()
