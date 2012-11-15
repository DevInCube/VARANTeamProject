'''
Created on Nov 15, 2012

@author: DevInCube
'''
import Tkinter as Tk
import ttk 

class TkForm(Tk.Toplevel):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.root = Tk.Tk()
        self.root.withdraw()
        Tk.Toplevel.__init__(self, self.root) 
        self.protocol('WM_DELETE_WINDOW', self.hide)       
    def show(self):        
        self.root.mainloop()
    def hide(self):
        self.master.destroy()