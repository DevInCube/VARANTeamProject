'''
Created on 13 November 2012

@author: Andrew
'''
import unittest
from controller import DataController


class Test(unittest.TestCase):


    def testNewRecord(self):
        d = DataController.DataController()
        self.assertEqual(True, True);


if __name__ == "__main__":
    unittest.main()