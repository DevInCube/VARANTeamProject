# coding: utf-8 

import Tkinter as Tk
import ttk 


class DataForm(Tk.Toplevel):
    def __init__(self,readonly,headers):
        self.root = Tk.Tk()
        self.root.withdraw()
        Tk.Toplevel.__init__(self, self.root) 
        self.protocol('WM_DELETE_WINDOW', self.hide)                
        self.tree = None                
        self.readonly = readonly            
        #gui
        self.mm = Tk.Menu(self)
        self.submenu = {}
        self.config(menu=self.mm)
        fm = Tk.Menu(self.mm) #Main
        self.mm.add_cascade(label="Main",menu=fm)
        fm.add_command(label="Logout")             
        fm.add_command(label="Exit")
        self.submenu[0] = fm
        
        im = Tk.Menu(self.mm) #Item
        self.mm.add_cascade(label="Item",menu=im)
        im.add_command(label="New")
        im.add_command(label="Edit")            
        im.add_command(label="Delete")
        self.submenu[1] = im 
                
        self.mm.add_command(label="About") #About
        self.mm.add_command(label="account",state='disabled') #account                      
        searchFrame = Tk.Frame(self)
        searchFrame.pack(side='top',fill='both', expand=True)
        self.searchInputs = {}        
        for i in range(len(headers)+1) :            
            self.searchInputs[i] = Tk.Entry(searchFrame)
            self.searchInputs[i].pack(side='left',fill='both', expand=True)
        searchBtnsFrame = Tk.Frame(self)
        searchBtnsFrame.pack(side='top',fill='both', expand=True)
        self.findButton = Tk.Button(searchBtnsFrame,text='Find', width=10)
        self.findButton.pack(side='left')        
        self.allButton = Tk.Button(searchBtnsFrame,text='All', width=10)
        self.allButton.pack(side='left')
        self.initTree(headers)
        
        pageNaviFrame = Tk.Frame(self)
        pageNaviFrame.pack(fill='both', expand=True)
        self.prevButton = Tk.Button(pageNaviFrame,text='Prev', width=10)
        self.prevButton.pack(side='left')
        self.pageLabel = Tk.Label(pageNaviFrame,text='/', width=10)
        self.pageLabel.pack(side='left')
        self.nextButton = Tk.Button(pageNaviFrame,text='Next', width=10)
        self.nextButton.pack(side='left')        
    def initTree(self,headers):
        self.tree=ttk.Treeview(self,columns=range(len(headers)),selectmode='browse')  #you can select only one item
        for i in range(len(headers)) :            
            self.tree.heading(i,text=headers[i])                
        self.tree.tag_configure("ttk")
        self.tree.pack(side='top',fill='x')    
    #
    def enableMenuItem(self,sm,item):
        self.submenu[sm].entryconfig(item,state='active')
    def disableMenuItem(self,sm,item):
        self.submenu[sm].entryconfig(item,state='disabled')
    def disableMenu(self,sm):
        self.mm.entryconfig(sm+1,state='disabled')
        
    def bindMenuItem(self,sm,item,action):      
        self.submenu[sm].entryconfig(item+1,command=action)   
    def insertRecord(self,id,vals):
        self.tree.insert('', 'end', text=id, values=(vals)) 
    def getRecord(self,id):        
        item = self.tree.item(self.tree.get_children('')[id])         
        return item['values']
    def clearRecords(self):        
        self.tree.delete(self.tree.get_children(''))
    def getSearchRecord(self):
        sr = {}
        for i in range(len(self.searchInputs)): 
            value = self.searchInputs[i].get()             
            sr[i] = value
        return sr 
    def clearSearchRecord(self):
        for i in range(len(self.searchInputs)): 
            v = Tk.StringVar()
            self.searchInputs[i].config(textvariable=v)
            v.set('')   
    def getSelectedRecord(self):
        """returns None is there is no selected item"""        
        sel_item = self.tree.item(self.tree.selection())         
        if sel_item["text"] is '' :
            return None
        rec = {'id': sel_item['text'], 'values':sel_item['values']}               
        return rec
    #events
    def setFindAction(self,action):
        self.findButton.config(command=action)
    def setResetFindAction(self,action):
        self.allButton.config(command=action)
    def setPrevPageAction(self,action):
        self.prevButton.config(command=action)
    def setNextPageAction(self,action):
        self.nextButton.config(command=action)  
    def setOnTreeItemSelect(self,action):        
        self.tree.bind("<CLICK>", action)#? itemselect???  
    #    
    def show(self):        
        self.root.mainloop()
    def hide(self):
        self.master.destroy()
    #
    def setPageStatus(self,status):
        self.pageLabel.config(text=status)
    def setAccountStatus(self,status):
        self.mm.entryconfig(4,label="| "+status)