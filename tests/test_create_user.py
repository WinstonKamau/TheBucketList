'''A test file for testing the user.py file on creating a new user.  '''
import unittest
from app.models import Users


class RegisterTestCase(unittest.TestCase):
    '''A class to test the registering function of the users for the bucket list.  '''


    def setUp(self):
        '''Creating an object of the Users class.  '''
        self.user = Users()

    def test_create_user_happy_path(self):
        '''A method to test that a user was created successfully with all inputs
        inserted correctly according to standards required.
        '''
        self.user.users.clear()
        self.user.create_user("user4", "user4@gmail.com", "password2", "password2")
        self.assertEqual(self.user.users[0].user_name, "user4")
        self.assertEqual(self.user.users[0].user_email, "user4@gmail.com")
        self.assertEqual(self.user.users[0].user_password, "password2")

    def test_create_user_sad_path(self):
        '''A method to test that a user was not created with non-matching passwords.  '''
        self.user.users.clear()
        self.user.create_user("user2", "user2@gmail.com", "password1", "password2")
        self.assertEqual(len(self.user.users), 0)

    def test_create_user_sad_path_2(self):
        '''A method to test that a user was not created with an empty user-name.  '''
        self.user.users.clear()
        self.user.create_user("", "user2@gmail.com", "password1", "password2")
        self.assertEqual(len(self.user.users), 0)

    def test_create_user_sad_path_3(self):
        '''A method to test that a user was not created with an empty password.  '''
        self.user.users.clear()
        self.user.create_user("user2", "user2@gmail.com", "", "")
        self.assertEqual(len(self.user.users), 0)

    def test_create_user_sad_path_4(self):
        '''A method to test that a user was not created with an empty email.  '''
        self.user.users.clear()
        self.user.create_user("user2", "", "ppp", "ppp")
        self.assertEqual(len(self.user.users), 0)

    def test_create_user_sad_path_5(self):
        '''A method to test that a second user was not created with a similar user-name
        as the first user.
        '''
        self.user.users.clear()
        self.user.create_user("user4", "user4@gmail.com", "password2", "password2")
        self.user.create_user("user4", "user3@gmail.com", "password3", "password3")
        self.assertEqual(len(self.user.users), 1)

    def test_create_user_sad_path_6(self):
        '''A method to test that a second user was not created with a similar email as the
        first user.
        '''
        self.user.users.clear()
        self.user.create_user("user1", "user1@gmail.com", "password2", "password2")
        self.user.create_user("user4", "user1@gmail.com", "password3", "password3")
        self.assertEqual(len(self.user.users), 1)

if __name__ == '__main__':
    unittest.main()
