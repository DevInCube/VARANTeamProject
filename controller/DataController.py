#from view import DataForm as df
#from view import EditItemForm
import tkMessageBox as tmb

class DataController:
    headers = ('id','name','test1','test2')
    def __init__(self):
        self.view = None
        self.page = 0
        self.pageSize = 100
        self.totalPages = 10
        self.editView = None
    def openConnection(self, readonly):
        #if self.view is None:
            #self.view = df.DataForm(readonly, self.headers)
        status = 'admin'
        if readonly:
            status = 'readonly'
        self.view.setAccountSettings(status)
        self.view.setNextPageAction(self.nextPage)
        self.view.setPrevPageAction(self.prevPage)
        self.view.setFindAction(self.search)
        self.view.setResetFindAction(self.showAllRecords)
        self.view.bindMenuItem(0, 0, self.logOut)
        self.view.bindMenuItem(0, 1, self.closeConnection)
        self.view.bindMenuItem(1, 0, self.newRecord)
        self.view.bindMenuItem(1, 1, self.editRecord)
        self.view.bindMenuItem(1, 2, self.deleteRecord)
        self.view.bindMenuItem(2, 0, self.showAbout)
        self.updateData()
        self.view.show()
    def closeConnection(self):
        pass
    def logOut(self):
        self.closeConnection()
    def newRecord(self):
        return True
    def selectRecord(self):
        pass
    def editRecord(self):
        pass
    def saveChanges(self):
        pass
    def cancelChanges(self):
        pass
    def deleteRecord(self):
        pass
    def prevPage(self):
        pass
    def nextPage(self):
        pass
    def search(self):
        pass
    def showAllRecords(self):
        pass
    def showAbout(self):
        text = '''VARAN Team Squad: 
- Azhipa Natalia
- Hadyniak Ruslan
- Zhuk Andriy
- Kakovsky Viacheslav'''
        tmb.showinfo('About', text)

    


