class Observable(object):

    def __init__(self, value=None):
        self.value = value
        self.callbacks = []

    def addCallback(self, func):
        self.callbacks.append(func)

    def set(self, value):
        self.value = value
        for func in self.callbacks:
            func(self.value)
