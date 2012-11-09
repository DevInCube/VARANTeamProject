'''
Created on Nov 8, 2012

@author: DevInCube
'''
import unittest
from view import DataForm as df

class Test(unittest.TestCase):

    def testDataForm(self):
        readonly = False;
        headers = ('id','test','all')  
        form = df.DataForm(readonly,headers)
        #form.show()           
        form.setPageStatus('1/2')        
        form.setFindAction(0)
        form.setResetFindAction(0)   
        form.setPrevPageAction(0)
        form.setNextPageAction(0) 
        form.insertRecord(0, 'vals')  
        self.assertEquals(form.getRecord(0),'vals')
        form.clearRecords()
        self.assertEquals(form.getRecord(0), None)
        form.getSearchRecord()        
        #form.hide()        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()