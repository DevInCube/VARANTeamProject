from AuthModel import AuthModel
from AuthForm import AuthForm


class AuthController(object):

    def __init__(self):
        self.view = AuthForm()
        self.view.setPriceChanger(self.changePrice)
        self.model = AuthModel()
        self.model.price.addCallback(self.priceChanged)
        self.view.run()

    def changePrice(self):
        self.model.calcPrice(int(self.view.getPrice()))

    def priceChanged(self, price):
        self.view.setPrice(price)

app = AuthController()
