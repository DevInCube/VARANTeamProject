from Tkinter import *
from ttk import Treeview
from TkForm import TkForm

class DataForm(TkForm):
    """
    Form to show data pages
    """
    def __init__(self, headers):
        """
        Class initializer with treeview columns' headers as a parameter
        """
        TkForm.__init__(self)
        self.tree_columns = headers
        self.title('Data Form')
        self.geometry('620x500+650+150')
        self.initComponents()

    def initComponents(self):
        """
        GUI components initialization
        """
        self.buttons = {}
        frame1 = Frame(self)
        frame1.place(relx=0.01, rely=0.03, width=600, height=30)
        self.accountLabel = Label(frame1, text='accStatus')
        self.accountLabel.place(x=0, width=80, height=30)
        self.buttons['logout'] = Button (frame1, text="Logout")
        self.buttons['logout'].place(x=85, height=24, width=80)
        self.buttons['about'] = Button (frame1, text="About")
        self.buttons['about'].place(x=170, height=24, width=80)
        frame2 = Frame(self)
        frame2.place(relx=0.01, rely=0.1, width=600, height=30)
        self.buttons['new'] = Button (frame2, text="New")
        self.buttons['new'].place(x=0, height=24, width=80)
        self.buttons['edit'] = Button (frame2, text="Edit")
        self.buttons['edit'].place(x=85, height=24, width=80)
        self.buttons['delete'] = Button (frame2, text="Delete")
        self.buttons['delete'].place(x=170, height=24, width=80)
        self.buttons['find'] = Button (frame2, text="Find")
        self.buttons['find'].place(x=255, height=24, width=80)
        frame3 = Frame(self)
        frame3.place(relx=0.01, rely=0.93, width=600, height=30)
        self.buttons['prev'] = Button (frame3, text="Prev")
        self.buttons['prev'].place(x=0, y=0, height=27, width=67)
        self.pageLabel = Label(frame3, text='pageStatus')
        self.pageLabel.place(x=85, width=80, height=30)
        self.buttons['next'] = Button (frame3, text="Next")
        self.buttons['next'].place(x=170, y=0, height=27, width=67)
        self.frame = Frame (self)
        self.frame.place(relx=0.01, rely=0.16, relheight=0.75, relwidth=0.98)
        self.frame.configure(relief=GROOVE)
        self.frame.configure(borderwidth="2")
        self.frame.configure(relief="groove")
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        container = self.frame
        tree = Treeview(container, columns=self.tree_columns, show="headings", selectmode='browse')
        self.tree = tree
        hsb = Scrollbar(container, orient="horizontal", command=self.tree.xview)
        self.tree.configure(xscrollcommand=hsb.set)
        # self.tree.grid(column=0, row=0, sticky='nsew', in_=container)
        self.tree.pack()
        hsb.grid(column=0, row=1, sticky='ew')
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)
        tree.grid(column=0, row=0, sticky='nsew')
        for col in self.tree_columns:
            self.tree.heading(col, text=col.title())

    def insert_record(self, pos, record):
        """
        Insert new record on the specified position of the Treeview
        """
        self.tree.insert('', pos, values=record)

    def get_record(self, pos):
        """
        Get record from the specified position,
        returns None if there is no record on such position
        """
        children = self.tree.get_children('')
        if pos < 0 or pos >= len(children):
            return None
        return self.tree.item(children[pos])['values']

    def clear_records(self):
        """
        Clear all the records in the Treeview
        """
        for item in self.tree.get_children():
            self.tree.delete(item)

    def get_selected_record(self):
        """
        Returns the record selected in the Treeview,
        returns None is there is no selected record
        """
        if self.tree.selection() is '':
            return None
        return self.tree.item(self.tree.selection())['values']

    def bind_button(self, btn_name, action):
        """
        Set command of a specified button of the form
        """
        self.buttons[btn_name].config(command=action)
    def enable_button(self, btn_name):
        """
        Enable a specified button of the form
        """
        self.buttons[btn_name].config(state='active')
    def disable_button(self, btn_name):
        """
        Disable a specified button of the form
        """
        self.buttons[btn_name].config(state='disabled')
    def set_page_status(self, status):
        """
        Set pageLabel Label text
        """
        self.pageLabel.config(text=status)

    def set_account_status(self, status):
        """
        Set accountLabel Label text
        """
        self.accountLabel.config(text=status)


if __name__ == '__main__':
    def add():
        df.insert_record(0, ('2', '1', '1', '1', '1'))
    def delete():
        df.clear_records()
    def show():
        print df.get_selected_record()
    def get():
        print df.get_record(3)
    headers = ("test", "ttt", "t1", "t2", "t3")
    df = DataForm(headers)
    df.set_account_status("account")
    df.set_page_status("test/test")
    df.bind_button("new", add)
    df.bind_button("edit", show)
    df.bind_button("delete", delete)
    df.bind_button("find", get)
    df.disable_button("about")
    df.disable_button("logout")
    df.enable_button("logout")
    df.insert_record(0, ('1', '1', '1', '1', '1'))
    df.insert_record(0, ('2', '1', '1', '1', '1'))
    df.show()
