# coding: utf-8
import Tkinter as Tk
import tkMessageBox as tmb
from view import TkForm


class AuthForm(TkForm.TkForm):

    def __init__(self):
        TkForm.TkForm.__init__(self)
        self.title('Lab1 VARAN')
        self.geometry("160x100+600+300")
        self.loginLabel = Tk.Label(self, text='Enter login:')
        self.loginLabel.pack(side='top')
        login = Tk.StringVar()
        self.loginEntry = Tk.Entry(self, textvariable=login, width=10)
        self.loginEntry.pack(side='top')
        self.passwordLabel = Tk.Label(self, text='Enter pass:')
        self.passwordLabel.pack(side='top')
        password = Tk.StringVar()
        self.passwordEntry = Tk.Entry(self, textvariable=password, width=10,
            show="*")
        self.passwordEntry.pack(side='top')
        self.loginButton = Tk.Button(self, text='Login', width=8)
        self.loginButton.pack(side='bottom')

    def onLoginButtonClick(self, sender):
        self.loginButton.configure(command=sender)

    def getPassword(self):
        return self.passwordEntry.get()

    def getLogin(self):
        return self.loginEntry.get()

    def setPassword(self, value):
        r = Tk.StringVar()
        r.set(value)
        self.passwordEntry.config(textvariable=r)

    def setLogin(self, value):
        r = Tk.StringVar()
        r.set(value)
        self.loginEntry.config(textvariable=r)

    def showMessage(self, message, state):
        result = None
        if state == "Error":
            self.showErrorMessage(message)
            result = True
        if state == "Success":
            self.showInfoMessage(message)
            result = True
        return result

    def showErrorMessage(self, message):
        tmb.showerror("Error", message)

    def showInfoMessage(self, message):
        tmb.showinfo("Info", message)
