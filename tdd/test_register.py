'''A test file for testing the register_class.py file'''
import unittest
#Importing the class RegisterCrud from the file register.py for testing
from register import RegisterCrud

class RegisterTestCase(unittest.TestCase):
    def setUp(self):
        '''creating an object from the register_class.py file'''
        self.register_object = RegisterCrud()
    def test_add_user_name (self):
        '''Test that the user name added is not an empty string'''
        self.assertRaises ( ValueError,self.register_object.create , "" , "password" )
    def test_add_password (self):
        '''Test that the password added is not an empty string'''
        self.assertRaises ( ValueError,self.register_object.create , "Name" , "" )
    def test_add_user_name_2 (self):
        '''Test that the user name added is not a number'''
        self.assertRaises ( ValueError,self.register_object.create , 123 , "password" )    
    
