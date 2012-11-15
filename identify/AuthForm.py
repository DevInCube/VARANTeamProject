# coding: utf-8
import Tkinter as Tk
import tkMessageBox as tmb

class AuthForm(Tk.Toplevel):

    def __init__(self):
        self.root = Tk.Tk()
        self.root.withdraw()
        self.root.title('Lab1 VARAN')
        Tk.Toplevel.__init__(self, self.root)
        self.geometry("160x100+600+300")   
        self.protocol('WM_DELETE_WINDOW', self.master.destroy)
        self.loginLabel = Tk.Label(self, text='Enter login:')
        self.loginLabel.pack(side='top')
        login = Tk.StringVar()
        self.loginEntry = Tk.Entry(self, textvariable=login, width=10)
        self.loginEntry.pack(side='top')       
        self.passwordLabel = Tk.Label(self, text='Enter pass:')
        self.passwordLabel.pack(side='top')
        password = Tk.StringVar()
        self.passwordEntry = Tk.Entry(self, textvariable=password, width=10, show="*") 
        self.passwordEntry.pack(side='top')         
        self.loginButton = Tk.Button(self, text='Login', width=8)
        self.loginButton.pack(side='bottom')
        
    def run(self):
        self.root.mainloop()

    def on_login_button_click(self, sender):
        self.loginButton.configure(command = sender)

    def get_password(self):
        return self.passwordEntry.get()

    def get_login(self):
        return self.loginEntry.get()

    def set_password(self, value):
        r = Tk.StringVar()
        r.set(value)
        self.passwordEntry.config(textvariable=r)

    def set_login(self, value):
        r = Tk.StringVar()
        r.set(value)        
        self.loginEntry.config(textvariable=r)
