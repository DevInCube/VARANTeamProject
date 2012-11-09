import Tkinter as Tk
import ttk
import DataForm as df
import EditItemForm as eif


def find():
    print dataForm.clearSearchRecord()
dataForm = df.DataForm(0,('id','tree'))
dataForm.setFindAction(find)
dataForm.insertRecord(0, "goog gkkg")
dataForm.insertRecord(1, "goog55 gkkgsa")
dataForm.disableMenuItem(1, 0)
#dataForm.disableMenu(1)
#dataForm.enableMenuItem(1, 1)
dataForm.setAccountStatus("readonly")
dataForm.bindMenuItem(1, 1,find)
dataForm.show()
"""
def close():
    print ef.getRecord()
headers = ('id','num','action')
item = {0,'34','test'}
ef = eif.EditItemForm(headers,item)
ef.setSaveAction(close)
ef.disableInput(0)
ef.show()
"""
"""
 def about(self):
        win = Tk.Toplevel()
        lab = Tk.Label(win,text="oppa\ngangnam\nstyle")
        lab.pack()     
"""
"""

#dataForm.clearRecords()
dataForm.show()
"""