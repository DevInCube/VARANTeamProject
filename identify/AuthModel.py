import tkMessageBox as tmb

from User import User


class AuthModel(object):

    def __init__(self):
        self.users = []
        self.users.append(User('admin', '1234', True))
        self.users.append(User('reader', 'qwerty', False))

    def login(self, login, password):
        if self.validation(login, password):
            return self.authentication(login, password)
        else:
            return None

    def authentication(self, login, password):
        user_found = False
        password_found = False
        result = None
        for user in self.users:
            if user.login == login:
                user_found = True
                if user.password == password:
                    password_found = True
                    result = user
        if password_found == False:
            if user_found == True:
                # self.sendMessage("Wrong Password")
                tmb.showerror("Auth", "Model.Wrong password")
            else:
                tmb.showerror("Auth", "User not found")
        return result

    def validation(self, login, password):
        pv = self.validate(password)
        lv = self.validate(login)
        if not (pv or lv == True):
            tmb.showerror("Validation", "Login and password are empty")
        else:
            if pv == False:
                tmb.showerror("Validation", "Password is empty")
            else:
                if lv == False:
                    tmb.showerror("Validation", "Login is empty")
        return pv and lv

    def validate(self, elem):
        if not (elem == ""):
            return True
        else:
            return False

    def sendMessage(self, message):
        pass
