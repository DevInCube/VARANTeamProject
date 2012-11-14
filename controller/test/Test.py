'''
Created on 13 November 2012

@author: Andrew
'''
import unittest
from controller import DataController


class Test(unittest.TestCase):


    def testNewRecord(self):
        d = DataController.DataController()
        self.assertEqual(d.newRecord(), True);


if __name__ == "__main__":
    unittest.main()