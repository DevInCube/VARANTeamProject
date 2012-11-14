import tkMessageBox as tmb

from AuthForm import AuthForm
from User import User

class AuthModel(object):

    def __init__(self):
        self.users = []
        self.users.append(User('admin', '1234', True))
        self.users.append(User('reader', 'qwerty', False))
 
    def login(self, login, password):
        if self.validation(login, password):
            self.authentication(login, password)            

    def authentication(self, login, password):
        is_admin = ""
        user_found = ""
        password_found = ""
        # loop finds user
        for user in self.users :
            if user.login == login:
                user_found = True
                if user.password == password:
                    password_found = True
                    is_admin = user.is_admin
        if password_found == True:
            tmb.showinfo("Auth is OK", "Now we call DataController with is_admin = " + str(is_admin))
            # start point to MVC2
        else:
            if user_found == True:
                tmb.showerror("Auth", "Wrong password")
            else:
                tmb.showerror("Auth", "User not found")        
   
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

