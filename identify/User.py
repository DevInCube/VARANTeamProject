

class User(object):
    def __init__(self, login, password, is_admin):
        self.login = login
        self.password = password
        self.is_admin = is_admin
