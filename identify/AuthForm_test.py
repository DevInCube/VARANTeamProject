'''
Created on 13.11.2012

@author: NetbookKakoff
'''
import unittest
import Tkinter as Tk
from AuthForm import AuthForm

class TestEmpty(unittest.TestCase):

    def setUp(self):
        self.view = AuthForm()
        
    def test_Validate_Password(self):
        self.assertEqual(self.view.validate_password(), False, "Validation failed. Password is empty")

    def test_Validate_Login(self):
        self.assertEqual(self.view.validate_login(), False, "Validation failed. Login is empty")

class TestNonAuthentified(unittest.TestCase):

    def setUp(self):
        self.view = AuthForm()
        self.view.set_login("3")    
        self.view.set_password("4")

    def test_Validate_Password(self):
        self.assertEqual(self.view.validate_password(), True, "Password is not empty")

    def test_Validate_Login(self):
        self.assertEqual(self.view.validate_login(), True, "Login is not empty")

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testValidate']
    unittest.main()
