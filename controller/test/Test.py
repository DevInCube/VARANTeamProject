'''
Created on 13 November 2012

@author: Andrew
'''
import unittest
from controller import DataController as dc
from view import DataForm as df


class Test(unittest.TestCase):

    def setUp(self):
        self.d = dc.DataController()
        self.headers = ('i1', 'i2', 'i3')
        self.d.view = df.DataForm(self.headers)
        self.d.data = self.d.d.loadData("E:\\new.csv")
        self.d.updateData()

    def testNewRecord(self):
        self.d.newRecord()
        unittest.TestCase.assertEqual(self, len(self.d.data), 122)

    def testNextPage(self):
        self.d.page = 2
        self.d.nextPage()
        unittest.TestCase.assertEqual(self, self.d.page, 3)

    def testPrevPage(self):
        self.d.page = 2
        self.d.prevPage()
        unittest.TestCase.assertEqual(self, self.d.page, 1)

    def testFirstPrevPage(self):
        self.d.page = 0
        self.d.prevPage()
        unittest.TestCase.assertEqual(self, self.d.page, 0)

    def testLastNextPage(self):
        self.d.page = self.d.totalPages - 1
        self.d.nextPage()
        unittest.TestCase.assertEqual(self, self.d.page, self.d.totalPages - 1)

    def testDeleteRecord(self):
        self.d.d.deleteRecord(0)
        unittest.TestCase.assertEqual(self, len(self.d.data), 120)

if __name__ == "__main__":
    unittest.main()
