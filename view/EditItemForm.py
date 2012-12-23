# coding: utf-8

import TkForm as tkf
import Tkinter as Tk
from Tkinter import StringVar

class EditItemForm(tkf.TkForm):
    def __init__(self, headers, title, item=None):
        tkf.TkForm.__init__(self)
        searchFrame = Tk.Frame(self.root)
        searchFrame.pack(side='top', fill='both', expand=True)
        searchFrameLeft = Tk.Frame(searchFrame)
        searchFrameLeft.pack(side='left', fill='x', expand=True)
        searchFrameRight = Tk.Frame(searchFrame)
        searchFrameRight.pack(side='left', fill='both', expand=True)
        self.editInputs = {}
        for i in range(len(headers)) :
            label = Tk.Label(searchFrameLeft, text=headers[i])
            label.pack(side='top', fill='x', expand=True)
            inputText = StringVar()
            if item != None:
                inputText.set(item[i])
            self.editInputs[i] = Tk.Entry(searchFrameRight, textvariable=inputText)
            self.editInputs[i].pack(side='top', fill='both', expand=True)
        self.bottomFrame = Tk.Frame(self.root)
        self.bottomFrame.pack(side='bottom', fill='both', expand=True)
    def addButton(self, name, action):
        btn = Tk.Button(self.bottomFrame, text=name, width=10)
        btn.config(command=action)
        btn.pack(side='left')
    def enableInput(self, ind):
        self.editInputs[ind].config(state='normal')
    def disableInput(self, ind):
        self.editInputs[ind].config(state='disabled')
    def getRecord(self):
        sr = {}
        for i in range(len(self.editInputs)):
            value = self.editInputs[i].get()
            sr[i] = value
        return sr

def main():
    headers = ('test1', 'test2', 'test3')
    item = ('i1', 'i2', 'i3')
    eif = EditItemForm(headers, item)
    eif.title('EditItemForm demo')
    eif.addButton('TestBtn1', None)
    eif.show()
if __name__ == "__main__":
    main()
