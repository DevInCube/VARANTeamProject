import tkMessageBox as tmb

from AuthModel import AuthModel
from AuthForm import AuthForm


class AuthController(object):

    def __init__(self):
        self.state = None
        self.view = AuthForm()
        self.view.onLoginButtonClick(self.tryAuth)
        self.model = AuthModel()
        # self.model.sendMessage(self.messageFromModel)
        #
        self.model.message.addCallback(self.messageFromModel)
        # self.data_controller = DataController()
        # TODO : controller observs model.message
        # if model.message is not None -> send to view (like an example)
        self.view.run()

    def messageFromModel(self, message):
        # print "message"
        if not (message is None):
            self.view.showMessage(message, self.state)
            self.model.message.set(None)
            self.model.state = None

    def tryAuth(self):
        self.state = "Error"
        login = self.view.getLogin()
        password = self.view.getPassword()
        user = self.model.login(login, password)
        if not (user is None):
            is_admin = user.is_admin
            self.state = "Success"
            # self.datacontroller.openConnection(is_admin)
            self.model.message.set("Now we call" +
                "DataController with is_admin = " + str(is_admin))
            # tmb.showinfo("Auth is OK", ("Now we call" +
            #    "DataController with is_admin = " + str(is_admin)))
        self.view.setPassword("")
        self.state = None

app = AuthController()
