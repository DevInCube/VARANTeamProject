from view import DataForm as df
from view import EditItemForm as eif
#import blabla as idf
import tkMessageBox as tmb

class DataController:
    headers = ('id','name','test1','test2')
    def __init__(self):
        self.view = None
        self.id = None
        self.page = 0
        self.__pageSize = 25
        self.totalPages = 5
        self.editView = None
        self.searchResult = ()
    def openConnection(self, readonly):
        if self.view is None:
            self.view = df.DataForm(readonly, self.headers)
        status = 'admin'
        if readonly:
            status = 'readonly'
        self.view.setAccountStatus(status)
        self.view.setNextPageAction(self.nextPage)
        self.view.setPrevPageAction(self.prevPage)
        #self.view.setFindAction(self.search)
        #self.view.setResetFindAction(self.showAllRecords)
        self.view.bindMenuItem(0, 0, self.logOut)
        self.view.bindMenuItem(0, 1, self.closeConnection)
        self.view.bindMenuItem(1, 0, self.newRecord)
        self.view.bindMenuItem(1, 1, self.editRecord)
        self.view.bindMenuItem(1, 2, self.deleteRecord)
        self.view.bindMenuItem(3, 0, self.showAbout)
        self.updateData()
        self.view.show()
    def closeConnection(self):
        if self.view is not None:
            self.view.hide()
    def logOut(self):
        self.closeConnection()
        #if self.id is None:
            #self.id = idf.IdentifyForm()
        #self.id.show()
    def newRecord(self):
        record = self.view.getSelectedRecord()
        self.editView = eif.EditItemForm(self.headers, record)
        self.editView.show()
        self.editView.setSaveAction(self.saveChanges)
        self.editView.setCancelAction(self.cancelChanges)
    def selectRecord(self):
        pass
    def editRecord(self):
        record = self.view.getSelectedRecord()
        if record is None:
            tmb.showinfo("Edit", "No item selected")
            return
        self.editView = eif.EditItemForm(self.headers, record)
        self.editView.show()
        self.editView.setSaveAction(self.saveChanges)
        self.editView.setCancelAction(self.cancelChanges)
    def saveChanges(self):
        #dataset writing function here
        self.editView.hide()
        #if self.page < self.totalPages:
            #return
        #self.updateData()
    def cancelChanges(self):
        self.editView.hide()
    def deleteRecord(self):
        record = self.view.getSelectedRecord()
        if record is None:
            tmb.showinfo("Delete", "No item selected")
    def updateData(self):
        status = str(self.page + 1) + "/" + str(self.totalPages)
        self.view.setPageStatus(status)
    def prevPage(self):
        if self.page > 0:
            self.page -= 1
        self.updateData()
    def nextPage(self):
        if self.page < self.totalPages -1:
            self.page += 1
        self.updateData()
    def search(self):
        self.searchResult = self.view.getSelectedRecord()
    def showAllRecords(self):
        self.view.clearRecords()
    def showAbout(self):
        text = '''VARAN Team Squad: 
- Azhipa Natalia
- Hadyniak Ruslan
- Zhuk Andriy
- Kakovskyi Viacheslav
VARAN(c)   2012'''
        tmb.showinfo('About', text)

    


