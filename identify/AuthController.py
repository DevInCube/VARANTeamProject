import tkMessageBox as tmb

from AuthModel import AuthModel
from AuthForm import AuthForm


class AuthController(object):

    def __init__(self):
        self.view = AuthForm()
        self.view.onLoginButtonClick(self.tryAuth)
        self.model = AuthModel()
        # self.data_controller = DataController()
        self.view.run()

    def tryAuth(self):
        login = self.view.getLogin()
        password = self.view.getPassword()
        user = self.model.login(login, password)
        if not (user is None):
            is_admin = user.is_admin
            # self.datacontroller.openConnection(is_admin)
            tmb.showinfo("Auth is OK", ("Now we call" +
                "DataController with is_admin = " + str(is_admin)))
        self.view.setPassword("")

app = AuthController()
