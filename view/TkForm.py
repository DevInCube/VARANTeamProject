'''
Created on Nov 15, 2012

@author: DevInCube
'''
import Tkinter as Tk


class TkForm(Tk.Toplevel):
    '''
    Parent form based on Tk.TopLevel
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.root = Tk.Tk()

    def show(self):
        '''Opens this window'''
        self.root.mainloop()

    def hide(self):
        '''Closes this window'''
        self.root.destroy()
