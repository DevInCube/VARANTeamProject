# coding: utf-8 

import Tkinter as Tk
import ttk 

class DataForm(Tk.Toplevel):
    def __init__(self,readonly,headers,c_records=25):
        self.root = Tk.Tk()
        self.root.withdraw()
        Tk.Toplevel.__init__(self, self.root) 
        self.geometry("%dx%d%+d%+d" % (800, 600, 300, 50))
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
        
        fm = Tk.Menu(self.mm) #Item
        self.mm.add_cascade(label="Find",menu=fm)
        fm.add_command(label="Find")       
        self.submenu[2] = fm 
                
        am = Tk.Menu(self.mm) #Item
        self.mm.add_cascade(label="About",menu=am)
        am.add_command(label="Developers") #About
        self.submenu[3] = am 
        self.mm.add_command(label="account",state='disabled') #account                      
        
        self.initTree(headers,c_records)
        
        pageNaviFrame = Tk.Frame(self)
        pageNaviFrame.pack(fill='both', expand=True)
        self.prevButton = Tk.Button(pageNaviFrame,text='Prev', width=10)
        self.prevButton.pack(side='left')
        self.pageLabel = Tk.Label(pageNaviFrame,text='/', width=10)
        self.pageLabel.pack(side='left')
        self.nextButton = Tk.Button(pageNaviFrame,text='Next', width=10)
        self.nextButton.pack(side='left')        
    def __initTree(self,headers,c_records): 
        searchFrame = Tk.Frame(self)
        searchFrame.pack(side='top',fill='both', expand=True)         
        self.tree=ttk.Treeview(searchFrame,columns=range(len(headers)),selectmode='browse',height=c_records)  #you can select only one item        
        for i in range(len(headers)) :
            self.tree.column(i)       
        for i in range(len(headers)) :            
            self.tree.heading(i,text=headers[i])                
        self.tree.tag_configure("ttk")      
        self.tree.grid(column=0, row=0, sticky='nswe')                
        self.tree.pack(side='top',fill='both')
        hsb = ttk.Scrollbar(self,orient="horizontal",command=self.tree.xview)
        hsb.pack(fill='x') 
        # self.tree.configure(xscrollcommand=lambda f, l:autoscroll(hsb, f, l))
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
    def getSelectedRecord(self):
        """returns None is there is no selected item"""        
        sel_item = self.tree.item(self.tree.selection())         
        if sel_item["text"] is '' :
            return None
        rec = {'id': sel_item['text'], 'values':sel_item['values']}               
        return rec
    #events    
    def setPrevPageAction(self,action):
        self.prevButton.config(command=action)
    def setNextPageAction(self,action):
        self.nextButton.config(command=action)      
    #    
    def show(self):        
        self.root.mainloop()
    def hide(self):
        self.master.destroy()
    #
    def setPageStatus(self,status):
        self.pageLabel.config(text=status)
    def setAccountStatus(self,status):
        self.mm.entryconfig(5,label="| "+status)