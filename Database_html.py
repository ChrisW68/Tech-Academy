from tkinter import *
from tkinter.ttk import *
import sqlite3
import webbrowser


class setup:
    def __init__(self):

        conn=sqlite3.connect('myHtml.db')
        cur=conn.cursor()
        cur.execute('''DROP TABLE IF EXISTS Html''')            #delete old table so can add records
        cur.execute('''CREATE TABLE IF NOT EXISTS Html(title TEXT)''')
        cur.execute("INSERT INTO Html VALUES ('This is a new page')")
        cur.execute("INSERT INTO Html VALUES ('Would you like to see more')")
        conn.commit()
        conn.close()

        #self.Entry=Entry(root)
        #self.Entry.focus()
        #self.Entry.grid(column=0,row=0)
        #self.Entry.bind("Return", self.singleRec)
        #Label(root, text="HTML text inquiry").grid(column=1,row=0)
        Button(root, text="Press for listbox", command=self.getAll).grid(column=0,row=1)
        Button(root, text="Add Html text", command=self.addRec).grid(column=0,row=2)
        Button(root, text="Send to webbrowser", command=self.sendRec).grid(column=0,row=3)

        self.mFrame=LabelFrame(root, text='Message Area', width=400,height=30)
        self.mFrame.grid(column=0, columnspan=4,row=6, sticky='nsew')


    def getAll(self):                                                        #This will display in a listbox my database
        searchWin=Toplevel()
        searchWin.geometry("325x200+300+190")                                   #Width, Height, x location, y location
        searchFrame=LabelFrame(searchWin, text="My list of HTML text")
        searchFrame.grid(column=0, row=0, sticky = (N,W,E,S))
        self.searchBox=Listbox(searchFrame, selectmode=SINGLE, width=50, height=10)
        self.searchBox.grid(column=0, row=0,sticky=NW)
        scrollBar=Scrollbar(searchFrame, orient=VERTICAL, command=self.searchBox.yview)
        scrollBar.grid(column=1, row=0,sticky=(N,S))
        self.searchBox['yscrollcommand']=scrollBar.set
        scrollBar=Scrollbar(searchFrame,orient=HORIZONTAL, command=self.searchBox.xview)
        scrollBar.grid(column=0, row=1,sticky=(E,W))
        self.searchBox['xscrollcommand']=scrollBar.set
        conn = sqlite3.connect('myHtml.db')
        cur = conn.cursor()
        cur.execute('SELECT title FROM Html')
        for row in cur:
            self.searchBox.insert('end',list(row))
        cur.close()
        self.searchBox.bind("<<ListboxSelect>>",self.on_click_listbox)

    def on_click_listbox(self, event):                          #Retrieve from listbox the row I selected by mouseclick
        index = self.searchBox.curselection()
        self.selectedTxt = self.searchBox.get(index)
        self.selText = str(self.selectedTxt)
        self.selText.replace('(','')
        Label(root,text='Selected: '+self.selText).grid(column=1,row=0)
        self.selText.replace('(','')
        self.selText.replace(')','')
        self.selText.replace(',','')
        self.myHtml=self.selText.replace('(','').replace(',','').replace(')','')    #Replaces all characters with empty space

    def addRec(self):                                                               #Adds new item to database
        Label(self.mFrame, text="",width=12).grid(column=1,row=1,sticky='ew')
        self.AddFlag=1
        self.aFrame=LabelFrame(root, text='Add HTML text', width=400,height='50')
        self.aFrame.grid(column=0,columnspan=4,row=5,sticky='nsew')
        Label(self.aFrame,text='HTML text to be added(Press"Enter": ').grid(column=0,row=0)
        self.descr=''
        self.Entry1=Entry(self.aFrame)
        self.Entry1.insert(0,self.descr)
        self.Entry1.grid(column=0,row=1)
        self.Entry1.focus()
        self.Entry1.bind("<Return>",self.upDateDescr)

    def upDateDescr(self,event):                                            #Update database with new added item
        Label(self.mFrame, text="",width=12).grid(column=1,row=1,sticky='ew')
        descr=self.Entry1.get()
        if self.AddFlag==1:
            self.conn=sqlite3.connect('myHtml.db')
            self.cur=self.conn.cursor()
            self.cur.execute('''INSERT into Html VALUES(?)''',[descr])
            print (descr)
            self.cur.execute('SELECT title FROM Html')
            for row in self.cur:
                print (row)
            self.conn.commit()
            self.conn.close()
        if self.AddFlag==0:
            self.conn=sqlite3.connect('myHtml.db')
            self.cur=self.conn.cursor()
            self.cur.execute('''Update into Html SET DESCRIPTION=?''',[descr])
            self.conn.commit()
            self.conn.close()
        success=self.cur.rowcount
        if success == 1:
            Label(self.mFrame, text="db updated: "+descr, width=40).grid(column=1,row=1,sticky='ew')
        if success == 0:
            Label(self.mFrame, text="db Error", width=12).grid(column=1,row=1,sticky='ew')
    def sendRec(self):                                                  #On Button click sends selected item to webbrowser
        webbrowser.open_new_tab('STAY_TUNED.html')
        webtext=self.myHtml
        f=open("STAY_TUNED.html", 'w')
        f.write('''<html><head></head><body><p>''')
        f.write(webtext)
        f.write('''</p></body></html>''')
        f.close()

if __name__=="__main__":
    root = Tk()
    root.title("GUI for html creating and loading")
    root.geometry("400x200+200+10")  #Width, Height, x location, y location
    a = StringVar()
    e = Entry(root, textvariable = a)
    setup()
    root.mainloop()