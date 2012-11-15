import tkMessageBox as tmb

from AuthModel import AuthModel
from AuthForm import AuthForm
from User import User


class AuthController(object):

    def __init__(self):
        self.view = AuthForm()
        self.view.on_login_button_click(self.try_auth)
        self.model = AuthModel()
        # self.data_controller = DataController()
        self.view.run()

    def try_auth(self):
        login = self.view.get_login()
        password = self.view.get_password()
        user = self.model.login(login, password)
        if not (user is None):
            is_admin = user.is_admin
            # self.datacontroller.openConnection(is_admin)
            tmb.showinfo("Auth is OK", "Now we call DataController with is_admin = " + str(is_admin))
        self.view.set_password("")

app = AuthController()
