# coding: utf-8
import Tkinter as Tk
import tkMessageBox as tmb

class AuthForm(Tk.Toplevel):

    def __init__(self):
        self.root = Tk.Tk()
        self.root.withdraw()
        self.root.title('Lab1 VARAN')
        Tk.Toplevel.__init__(self, self.root)
        self.geometry("160x100+600+300")   
        self.protocol('WM_DELETE_WINDOW', self.master.destroy)
        self.loginLabel = Tk.Label(self, text='Enter login:')
        self.loginLabel.pack(side='top')
        login = Tk.StringVar()
        self.loginEntry = Tk.Entry(self, textvariable=login, width=10)
        self.loginEntry.pack(side='top')       
        self.passwordLabel = Tk.Label(self, text='Enter pass:')
        self.passwordLabel.pack(side='top')
        password = Tk.StringVar()
        self.passwordEntry = Tk.Entry(self, textvariable=password, width=10) 
        self.passwordEntry.pack(side='top')         
        self.loginButton = Tk.Button(self, text='Login', width=8)
        self.loginButton.configure(command = self.sendForm)
        self.loginButton.pack(side='bottom')
        # self.changeButton = Tk.Button(self, text='Change', width=8)
        
    def run(self):
        self.root.mainloop()

    def validate(self):
        pv = self.validate_password()
        lv = self.validate_login()
        if not (pv or lv == True):
            tmb.showerror("Validation", "Login and password are empty")
        else:
            if pv == False:
                tmb.showerror("Validation", "Password is empty")
            else:
                if lv == False:
                    tmb.showerror("Validation", "Login is empty")                
        return pv and lv
        
    def validate_password(self):
        if not (self.get_password()==""):
            return True
        else:
            return False

    def validate_login(self):
        if not (self.get_login()==""):
            return True
        else:
            return False

    def sendForm(self):       
        if self.validate():           
            tmb.showinfo("Auth", "Now we call authentication")
            
    def setPriceChanger(self, changer):
        self.changeButton.config(command=changer)

    def get_password(self):
        return self.passwordEntry.get()

    def get_login(self):
        return self.loginEntry.get()

    def set_password(self, value):
        r = Tk.StringVar()
        r.set(value)
        self.passwordEntry.config(textvariable=r)

    def set_login(self, value):
        r = Tk.StringVar()
        r.set(value)        
        self.loginEntry.config(textvariable=r)

    def setPrice(self, value):
        self.priceValue.config(text='Cost: %f' % value)
               
'''view = AuthForm()
view.run()
'''