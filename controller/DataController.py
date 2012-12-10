from view import DataForm as df
from view import EditItemForm as eif
#import blabla as idf
import tkMessageBox as tmb
import gettext


class DataController:
    headers = ("CAD CDW ID", "CAD Event Number", "General Offense Number",
               "Event Clearance Code", "Event Clearance Description",
               "Event Clearance SubGroup", "Event Clearance Group",
               "Event Clearance ", "Date", "Hundred Block Location",
               "District/Sector", "Zone/Beat", "Census Tract", "Longitude",
               "Latitude", "Incident Location")

    def __init__(self):
        self.view = None
        self.id = None
        self.page = 0
        self.record = None
        self.recordStartWith = 0
        self.pageSize = 25
        self.totalPages = 5
        self.editView = None
        self.searchResult = ()
        gettext.install('DCMsg', './locale', unicode=True)

    def openConnection(self, readonly):
        if self.view is None:
            self.view = df.DataForm(readonly, self.headers)
        status = 'admin'
        if readonly:
            status = 'readonly'
            self.view.disableMenu(1)
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
        self.editView = eif.EditItemForm(self.headers, self.record)
        self.editView.addButton(_("Save"), self.saveChanges)
        self.editView.addButton(_("Cancel"), self.cancelChanges)
        self.editView.show()

    def editRecord(self):
        record = self.view.getSelectedRecord()
        if record is None:
            return
        self.view.enableMenuItem(1, 2)
        self.editView = eif.EditItemForm(self.headers, record)
        self.editView.show()
        self.editView.addButton(_("Save"), self.saveChanges)
        self.editView.addButton(_("Cancel"), self.cancelChanges)

    def saveChanges(self):
        #dataset writing function here
        print _("changes saved")
        #self.view.insertRecord(0, self.record)
        self.editView.hide()
        if self.page < self.totalPages:
            return
        #self.updateData()

    def cancelChanges(self):
        self.editView.hide()

    def deleteRecord(self):
        record = self.view.getSelectedRecord()
        if record is None:
            return
        self.view.enableMenuItem(1, 3)
        self.editView.addButton(_("Delete"), self.saveChanges)
        self.editView.addButton(_("Cancel"), self.cancelChanges)
        #delete record here

    def updateData(self):
        status = str(self.page + 1) + "/" + str(self.totalPages)
        self.view.setPageStatus(status)

    def prevPage(self):
        if self.page > 0:
            self.page -= 1
            self.recordStartWith -= self.pageSize
        self.updateData()

    def nextPage(self):
        if self.page < self.totalPages - 1:
            self.page += 1
            self.recordStartWith += self.pageSize
        self.updateData()

    def search(self):
        self.searchResult = (1, 2)

    def showAllRecords(self):
        self.view.clearRecords()

    def showAbout(self):
        text = _("VARAN Team Squad:\n - Azhipa Natalia\n- Hadyniak Ruslan\n- Zh\
uk Andriy\n- Kakovskyi Viacheslav\nVARAN(c)   2012")
        tmb.showinfo(_("About"), text)
