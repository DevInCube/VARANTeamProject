'''
    slawek-kk: 15.11.2012
    Start point to MVC2:
    self.datacontroller.openConnection(is_admin)
'''
from AuthModel import AuthModel
from AuthForm import AuthForm
from controller import DataController as dc
from Tkinter import *


class AuthController(object):

    def __init__(self, app):
        self.app = app
        self.state = None
        self.view = AuthForm()
        self.view.setOnClose(self.onClose)
        self.view.onLoginButtonClick(self.tryAuth)
        self.model = AuthModel()
        self.model.message.addCallback(self.messageFromModel)
        self.view.show()

    def onClose(self):
        self.app.quit()
        print 'quit'
        self.view.destroy()

    def messageFromModel(self, message):
        result = None
        if not (message is None):
            self.view.showMessage(message, self.state)
            self.model.message.set(None)
            self.model.state = None
            result = True
        return result

    def tryAuth(self):
        self.state = "Error"
        login = self.view.getLogin()
        password = self.view.getPassword()
        user = self.model.login(login, password)
        if not (user is None):
            is_admin = user.is_admin
            self.state = "Success"
            self.d = dc.DataController(self.logout)
            self.d.openConnection(is_admin)
            self.view.hide()
        # self.view.setPassword("")
        # self.state = None
    def logout(self):
        AuthController(self.app)

if __name__ == "__main__":
    app = Tk()
    app.withdraw()
    AuthController(app)
    app.mainloop()

