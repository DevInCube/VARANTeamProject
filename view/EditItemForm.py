# coding: utf-8 

import TkForm as tkf
import Tkinter as Tk
import ttk 


class EditItemForm(tkf.TkForm):
    def __init__(self,headers,item=None):        
        tkf.TkForm.__init__(self)
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
        self.bottomFrame = Tk.Frame(self)
        self.bottomFrame.pack(side='bottom',fill='both', expand=True)        
    def addButton(self,name,action):
        btn = Tk.Button(self.bottomFrame,text=name, width=10)
        btn.config(command=action)
        btn.pack(side='left')        
    def disableInput(self,ind):
        self.editInputs[ind].config(state='disabled')
    def getRecord(self):
        sr = {}
        for i in range(len(self.editInputs)): 
            value = self.editInputs[i].get()             
            sr[i] = value
        return sr     