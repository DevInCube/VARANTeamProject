import tkMessageBox as tmb

from AuthModel import AuthModel
from AuthForm import AuthForm


class AuthController(object):

    def __init__(self):
        self.view = AuthForm()
        self.view.on_login_button_click(self.send_form)
        self.model = AuthModel()
        self.view.run()

    def send_form(self):
        login = self.view.get_login()
        password = self.view.get_password()
        self.model.login(login, password)

app = AuthController()
