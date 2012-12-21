import unittest

from AuthForm import AuthForm


class TestMessage(unittest.TestCase):

    def setUp(self):
        self.view = AuthForm()

    def testShowMessage_NoneData(self):
        self.assertEqual(self.view.showMessage(None, None), None,
            "Function returns not None on None data")

    def testShowMessage_EmptyData(self):
        self.assertEqual(self.view.showMessage("", ""), None,
            "Function returns not None on Empty data")

    def testShowMessage_NonValid1(self):
        self.assertEqual(self.view.showMessage("foo", ""), None,
            "Function returns not None on empty data")

    def testShowMessage_NonValid2(self):
        self.assertEqual(self.view.showMessage("", "bar"), None,
            "Function returns not None on Non Valid data")

    def testShowMessage_Error(self):
        self.assertEqual(self.view.showMessage("", "Error"), True,
            "Function returns not True on Valid data (state=Error)")

    def testShowMessageSuccess(self):
        self.assertEqual(self.view.showMessage("", "Success"), True,
            "Function returns not True on Valid data (state=Success)")

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testValidate']
    unittest.main()
