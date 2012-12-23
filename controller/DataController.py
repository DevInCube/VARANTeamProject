from view import DataForm as df
from view import EditItemForm as eif
from model import DataEntity as de
<<<<<<< HEAD
from identify import AuthForm as af
import tkMessageBox as tmb

'''DataController class'''


class DataController:
    '''Tree column headers'''
=======
import tkMessageBox as tmb


class DataController:
    '''DataController class'''
>>>>>>> 622575061fa66c73f9849fb2d2d735f4454e575b
    headers = ("ID", "CAD CDW ID", "CAD Event Number",
               "General Offense Number", "Event Clearance Code",
               "Event Clearance Description", "Event Clearance SubGroup",
               "Event Clearance Group", "Event Clearance Date",
               "Hundred Block Location", "District/Sector", "Zone/Beat",
               "Census Tract", "Longitude", "Latitude", "Incident Location")

<<<<<<< HEAD
    def __init__(self):
        '''DataController initialization'''
        self.view = None
        self.id = None
        self.page = 0
        self.record = None
        self.recordStartWith = 0
=======
    def __init__(self, onlogout=None):
        '''DataController initialization'''
        self.view = None
        self.page = 0
>>>>>>> 622575061fa66c73f9849fb2d2d735f4454e575b
        self.pageSize = 16
        self.totalPages = 0
        self.editView = None
        self.d = de.DataEntity()
        self.authView = None
<<<<<<< HEAD
        self.data = self.d.loadData("E:\\test.csv")
        self.searchResult = ()
=======
        self.edit_record = None
        self.lastSearch = None
        self.data = None
        self.lastSearch = None
        self.onLogout = onlogout
        gettext.install('DEMsg', './locale', unicode=True)
>>>>>>> 622575061fa66c73f9849fb2d2d735f4454e575b

    def openConnection(self, isadmin):
        '''Create new connection and show dataset in tree'''
        if self.view is None:
            self.view = df.DataForm(self.headers)
<<<<<<< HEAD
=======
            self.view.setOnClose(self.onClose)
>>>>>>> 622575061fa66c73f9849fb2d2d735f4454e575b
        status = 'readonly'
        if isadmin:
            status = 'admin'
        if not isadmin:
            self.view.disable_button('edit')
            self.view.disable_button('delete')
<<<<<<< HEAD
        self.view.set_account_status(status)
=======
            self.view.disable_button('new')
        self.view.set_account_status(status)
        self.data = self.d.loadData("/home/natalia/workspace/VARANTeamProject/model/Data.csv")
>>>>>>> 622575061fa66c73f9849fb2d2d735f4454e575b
        self.view.bind_button('next', self.nextPage)
        self.view.bind_button('prev', self.prevPage)
        self.view.bind_button('logout', self.logOut)
        self.view.bind_button('new', self.newRecord)
        self.view.bind_button('edit', self.editRecord)
        self.view.bind_button('delete', self.deleteRecord)
        self.view.bind_button('find', self.search)
        self.view.bind_button('about', self.showAbout)
        self.updateData()
        self.view.show()
<<<<<<< HEAD
        # self.updateData()
=======

    def onClose(self):
        self.logOut()
>>>>>>> 622575061fa66c73f9849fb2d2d735f4454e575b

    def closeConnection(self):
        '''Exit button implementation(Destroy the main window)'''
        if self.view is not None:
            self.view.hide()

    def logOut(self):
        '''Call Authorization Form and close Main Form'''
        self.closeConnection()
<<<<<<< HEAD
        self.d.saveData("E:\\test.csv")
        print "data saved"
        self.authView = af.AuthForm()
        self.authView.show()

    def newRecord(self,):
        '''Insert new record in treeview'''
        self.editView = eif.EditItemForm(self.headers, self.record)
        self.editView.root.title("New Record")
        self.editView.disableInput(0)
        self.editView.addButton("Save", self.save_new)
        self.editView.addButton("Cancel", self.cancelChanges)
=======
        self.d.saveData("/home/natalia/workspace/VARANTeamProject/model/Data.csv")
        if self.onLogout:
            self.onLogout()

    def newRecord(self):
        '''Insert new record in treeview'''
        self.d.newRecord()
        self.data = self.d.getRecords()
        record = self.data[len(self.data) - 1]
        self.editView = eif.EditItemForm(self.view, self.headers,
                                         _("Edit"), record)
        self.editView.disableInput(0)
        self.editView.addButton(_("Save"), self.save)
        self.editView.addButton(_("Cancel"), self.cancel)
>>>>>>> 622575061fa66c73f9849fb2d2d735f4454e575b
        self.editView.show()

    def editRecord(self):
        '''Edit existing record in treeview'''
<<<<<<< HEAD
        record = self.view.get_selected_record()
        if record is None:
            tmb.showerror("Error", "There is no record selected")
            return
        self.editView = eif.EditItemForm(self.headers, record)
        self.editView.disableInput(0)
        self.editView.addButton("Save", self.save_edit)
        self.editView.addButton("Cancel", self.cancelChanges)
=======
        self.edit_record = self.view.get_selected_record()
        if self.edit_record is None:
            tmb.showerror("Error", _("There is no record selected"))
            return
        self.editView = eif.EditItemForm(self.view, self.headers,
                                         _("Edit"), self.edit_record)
        self.editView.disableInput(0)
        self.editView.addButton(_("Save"), self.save)
        self.editView.addButton(_("Cancel"), self.cancel)
>>>>>>> 622575061fa66c73f9849fb2d2d735f4454e575b
        self.editView.show()

    def save_new(self):
        '''Save data in dataset and update tree'''
        self.editView.hide()
<<<<<<< HEAD
=======
        self.d.newRecord()
        self.updateData()

    def save(self):
        '''Save data in dataset and update tree'''
        self.d.changeRecord(self.editView.getRecord())
        self.editView.hide()
>>>>>>> 622575061fa66c73f9849fb2d2d735f4454e575b
        self.updateData()

    def cancel(self):
        '''Cancel the changes done'''
        self.editView.hide()

    def deleteRecord(self):
        '''Open Delete Record window and delete selected record'''
<<<<<<< HEAD
        record = self.view.get_selected_record()
        if record is not None:
            rid = record[0]
            print str(rid)
        if record is None:
            tmb.showerror("Error", "There is no record selected")
            return
        self.d.deleteRecord(rid)
=======
        try:
            record = self.view.get_selected_record()
            rid = record[0]
        except:
            tmb.showerror("Error", _("There is no record selected"))
            return
        self.d.deleteRecord(rid)
        self.data = self.d.searchRecords(self.lastSearch)
>>>>>>> 622575061fa66c73f9849fb2d2d735f4454e575b
        self.updateData()

    def updateData(self):
        '''Update tree to show changes done'''
        self.view.clear_records()
        self.totalPages = len(self.data) / self.pageSize
        if len(self.data) % self.pageSize is not 0:
            self.totalPages += 1
        end = (self.page + 1) * self.pageSize
        if end > len(self.data):
            end = len(self.data)
        for i in range(self.page * self.pageSize, end):
            self.view.insert_record(i, self.data[i])
        status = str(self.page + 1) + "/" + str(self.totalPages)
        self.view.set_page_status(status)

    def prevPage(self):
        '''Previous tree page action'''
        if self.page > 0:
            self.page -= 1
        self.updateData()

    def nextPage(self):
        '''Next tree page action'''
        if self.page < self.totalPages - 1:
            self.page += 1
        self.updateData()

    def search(self):
        '''Search record by parameters'''
<<<<<<< HEAD
        self.editView = eif.EditItemForm(self.headers, self.searchResult)
        self.editView.addButton("Find", self.save)
        self.editView.addButton("Cancel", self.cancel)
        self.editView.show()

    def showAllRecords(self):
        '''Clear search results and show all dataset'''
        self.searchResult = ()
        self.view.hide()
        self.recordStartWith = 0
        self.view.show()

    def showAbout(self):
        '''Show messagebox about the developers team'''
        text = "VARAN Team Squad:\n - Azhipa Natalia\n- Hadyniak Ruslan\n- \
Zhuk Andriy\n- Kakovskyi Viacheslav\nVARAN(c)   2012"
        tmb.showinfo('About', text)
=======
        self.editView = eif.EditItemForm(self.view, self.headers,
                                         _("Search"), self.lastSearch)
        self.editView.addButton(_("Find"), self.find)
        self.editView.addButton(_("Cancel"), self.cancel)
        self.editView.addButton(_("Show All"), self.showAllRecords)
        self.editView.show()

    def find(self):
        self.lastSearch = self.editView.getRecord()
        self.editView.hide()
        self.data = self.d.searchRecords(self.lastSearch)
        self.page = 0
        self.updateData()

    def showAllRecords(self):
        '''Clear search results and show all dataset'''
        self.lastSearch = None
        self.data = self.d.getRecords()
        self.editView.hide()
        self.updateData()

    def showAbout(self):
        '''Show messagebox about the developers team'''
        text = _("VARAN Team Squad:\n - Azhipa Natalia\n- Hadyniak Ruslan\n- \
Zhuk Andriy\n- Kakovskyi Viacheslav\nVARAN(c)   2012")
        tmb.showinfo(_('About'), text)
>>>>>>> 622575061fa66c73f9849fb2d2d735f4454e575b
