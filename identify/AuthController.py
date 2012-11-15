'''
    slawek-kk: 15.11.2012
    Start point to MVC2:
    self.datacontroller.openConnection(is_admin)
'''
from AuthModel import AuthModel
from AuthForm import AuthForm


class AuthController(object):

    def __init__(self):
        self.state = None
        self.view = AuthForm()
        self.view.onLoginButtonClick(self.tryAuth)
        self.model = AuthModel()
        self.model.message.addCallback(self.messageFromModel)
        self.view.run()

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
            self.model.message.set("Now we call" +
                "DataController with is_admin = " + str(is_admin))
            # self.datacontroller.openConnection(is_admin)
        self.view.setPassword("")
        self.state = None

if __name__ == "__main__":
    app = AuthController()

