# coding: utf-8 

import Tkinter as Tk
import ttk 


class EditItemForm(Tk.Toplevel):
    def __init__(self,headers,item=None):        
        self.root = Tk.Tk()
        self.root.withdraw()
        Tk.Toplevel.__init__(self, self.root) 
        self.protocol('WM_DELETE_WINDOW', self.hide)
        searchFrame = Tk.Frame(self)
        searchFrame.pack(side='top',fill='both', expand=True)
        searchFrameLeft = Tk.Frame(searchFrame)
        searchFrameLeft.pack(side='left',fill='x', expand=True)
        searchFrameRight = Tk.Frame(searchFrame)
        searchFrameRight.pack(side='left',fill='both', expand=True)
        self.editInputs = {}        
        for i in range(len(headers)) :    
            label = Tk.Label(searchFrameLeft,text=headers[i])
            label.pack(side='top',fill='x', expand=True)          
            inputText = ''
            if item != None:
                inputText = item[i]
            self.editInputs[i] = Tk.Entry(searchFrameRight,text=inputText)
            self.editInputs[i].pack(side='top',fill='both', expand=True)
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