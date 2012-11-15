import unittest

from AuthForm import AuthForm


class TestEmpty(unittest.TestCase):

    def setUp(self):
        self.view = AuthForm()

    def testValidatePassword(self):
        self.assertEqual(self.view.validate_password(), False,
            "Validation failed. Password is empty")

    def testValidateLogin(self):
        self.assertEqual(self.view.validate_login(), False,
            "Validation failed. Login is empty")

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testValidate']
    unittest.main()
