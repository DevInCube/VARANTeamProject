# coding: utf-8 

import Tkinter as Tk
import ttk 


class EditItemForm(Tk.Toplevel):
    def __init__(self,headers,item):        
        self.root = Tk.Tk()
        self.root.withdraw()
        Tk.Toplevel.__init__(self, self.root) 
        self.protocol('WM_DELETE_WINDOW', self.hide)
        labelsFrame = Tk.Frame(self)
        labelsFrame.pack(side='top',fill='both', expand=True)
        for i in range(len(headers)) :            
            l = Tk.Label(labelsFrame, text=headers[i])
            l.pack(side='left',fill='both', expand=True)
        editFrame = Tk.Frame(self)
        editFrame.pack(side='top',fill='both', expand=True)
        self.editInputs = {}        
        for i in range(len(item)) :            
            self.editInputs[i] = Tk.Entry(editFrame)
            self.editInputs[i].pack(side='left',fill='both', expand=True)
        bottomFrame = Tk.Frame(self)
        bottomFrame.pack(side='bottom',fill='both', expand=True)
        self.saveButton = Tk.Button(bottomFrame,text='Save', width=10)
        self.saveButton.pack(side='left')        
        self.cancelButton = Tk.Button(bottomFrame,text='Cancel', width=10)
        self.cancelButton.pack(side='left')
    def disableInput(self,ind):
        self.editInputs[ind].config(state='disabled')
    def getRecord(self):
        sr = {}
        for i in range(len(self.editInputs)): 
            value = self.editInputs[i].get()             
            sr[i] = value
        return sr 
    def setSaveAction(self,action):
        self.saveButton.config(command=action)
    def setCancelAction(self,action):
        self.cancelButton.config(command=action)
    def show(self):
        self.root.mainloop()
    def hide(self):            
        self.master.destroy()