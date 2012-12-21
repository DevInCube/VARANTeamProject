'''
Created on Nov 15, 2012

@author: DevInCube
'''
import Tkinter as Tk


class TkForm(Tk.Toplevel):
    '''
    Parent form based on Tk.TopLevel
    '''
    def __init__(self, master=None):
        '''
        Constructor
        '''
        Tk.Toplevel.__init__(self)
    def setOnClose(self, action):
        self.protocol("WM_DELETE_WINDOW", action)

    def show(self):
        '''Opens this window'''
        self.wm_deiconify()
        # self.wm_deiconify()

    def hide(self):
        '''Closes this window'''
        self.destroy()
