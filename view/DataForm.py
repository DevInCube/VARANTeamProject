# coding: utf-8 

import TkForm as tkf
import Tkinter as Tk
import ttk 

class DataForm(tkf.TkForm):
    '''Main form for data pageview and items' manipulations'''
    def __init__(self,readonly,headers,c_records=25):
        tkf.TkForm.__init__(self)
        self.geometry("%dx%d%+d%+d" % (800, 600, 300, 50))                
        self.tree = None                
        self.readonly = readonly                
        self.mm = Tk.Menu(self) #Menu      
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
        am = Tk.Menu(self.mm) #About
        self.mm.add_cascade(label="About",menu=am)
        am.add_command(label="Developers")
        self.submenu[3] = am 
        self.mm.add_command(label="account",state='disabled') #account                              
        self.initTree(headers,c_records)
        self.initPageControl()
        
    def initTree(self,headers,c_records): 
        searchFrame = Tk.Frame(self)
        searchFrame.pack(side='top',fill='both', expand=True)         
        self.tree=ttk.Treeview(searchFrame,columns=range(len(headers)))
        self.tree.config(show='headings',height=c_records,selectmode='browse')        
        for i in range(len(headers)) :            
            self.tree.heading(i,text=headers[i])                
        self.tree.tag_configure("ttk")      
        self.tree.grid(column=0, row=0, sticky='nswe')                
        self.tree.pack(side='top',fill='both')
        hsb = ttk.Scrollbar(self,orient="horizontal",command=self.tree.xview)
        hsb.pack(fill='x') 
        # self.tree.configure(xscrollcommand=lambda f, l:autoscroll(hsb, f, l))
        
    def initPageControl(self):
        pageNaviFrame = Tk.Frame(self)
        pageNaviFrame.pack(fill='both', expand=True)
        self.prevButton = Tk.Button(pageNaviFrame,text='Prev', width=10)
        self.prevButton.pack(side='left')
        self.pageLabel = Tk.Label(pageNaviFrame,text='/', width=10)
        self.pageLabel.pack(side='left')
        self.nextButton = Tk.Button(pageNaviFrame,text='Next', width=10)
        self.nextButton.pack(side='left')       
    #
    def enableMenuItem(self,sm,item):
        self.submenu[sm].entryconfig(item,state='active')
    def disableMenuItem(self,sm,item):
        self.submenu[sm].entryconfig(item,state='disabled')
    def disableMenu(self,sm):
        self.mm.entryconfig(sm+1,state='disabled')
    
    def bindMenuItem(self,sm,item,action):      
        self.submenu[sm].entryconfig(item+1,command=action)   
    def insertRecord(self,pos,vals):
        self.tree.insert('', 'end', text=pos, values=(vals)) 
    def getRecord(self,pos):        
        item = self.tree.item(self.tree.get_children('')[pos])         
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
    def setPageStatus(self,status):
        self.pageLabel.config(text=status)
    def setAccountStatus(self,status):
        self.mm.entryconfig(5,label="| "+status)

def main():
    readonly = False
    headers = ('test1','test2','test3')
    df = DataForm(readonly,headers)
    df.title('DataForm demo')
    df.show()
if __name__ == "__main__":
    main()