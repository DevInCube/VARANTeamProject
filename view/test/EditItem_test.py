'''
Created on Nov 9, 2012

@author: DevInCube
'''
import unittest
from view import EditItemForm


class Test(unittest.TestCase):


    def testName(self):
        item = {0,'34','test'}
        ef = EditItemForm(item,0)
        ef.show()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()