import unittest
import gettext
from AuthForm import AuthForm


class TestMessage(unittest.TestCase):

    def setUp(self):
        self.view = AuthForm()
        gettext.install('IMsg', './locale', unicode=True)

    def testShowMessage_NoneData(self):
        self.assertEqual(self.view.showMessage(None, None), None,
            _("Function returns not None on None data"))

    def testShowMessage_EmptyData(self):
        self.assertEqual(self.view.showMessage("", ""), None,
            _("Function returns not None on Empty data"))

    def testShowMessage_NonValid1(self):
        self.assertEqual(self.view.showMessage("foo", ""), None,
            _("Function returns not None on empty data"))

    def testShowMessage_NonValid2(self):
        self.assertEqual(self.view.showMessage("", "bar"), None,
            _("Function returns not None on Non Valid data"))

    def testShowMessage_Error(self):
        self.assertEqual(self.view.showMessage("", "Error"), True,
            _("Function returns not True on Valid data (state=Error)"))

    def testShowMessageSuccess(self):
        self.assertEqual(self.view.showMessage("", "Success"), True,
            _("Function returns not True on Valid data (state=Success)"))

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testValidate']
    unittest.main()
