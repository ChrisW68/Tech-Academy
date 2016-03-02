from tkinter import *
from tkinter.ttk import *
import os

class setup:
    def __init__(self):
        self.BT=Style()
        self.BT.theme_use('classic')
        self.BT.configure('TButton')
        self.BT.map('TButton',
                    foreground=[('disabled','yellow'), ('pressed','red'), ('active','blue')],
                    background=[('disabled', 'magenta'),('pressed','cyan'),('active','green')],
                    highlightcolor=[('focus', 'green'),('!focus','red')],
                    relief=[('pressed','groove'),('!pressed','ridge')])
        self.B1 = Button(root, text='Show List Box', width=15,
                         command=self.searchPaths, style='TButton').grid(column=0,row=0)
        self.B2 = Button(root, text='Delete Selected', width=15,
                         command=self.deleteSelected, style='TButton').grid(column=0, row=1)
        self.B3=Button(root, text='Insert to Listbox', width=15,
                       command=self.insertText, style='TButton').grid(column=0, row=2)

    def searchPaths(self):
        searchWin=Toplevel()
        searchWin.geometry("325x200+300+190")                                   #Width, Height, x location, y location
        searchFrame=LabelFrame(searchWin, text="My Current Directory")
        searchFrame.grid(column=0, row=0, sticky = (N,W,E,S))
        self.searchBox=Listbox(searchFrame, selectmode=SINGLE, width=50, height=10)
        self.searchBox.grid(column=0, row=0,sticky=NW)
        scrollBar=Scrollbar(searchFrame, orient=VERTICAL, command=self.searchBox.yview)
        scrollBar.grid(column=1, row=0,sticky=(N,S))
        self.searchBox['yscrollcommand']=scrollBar.set
        scrollBar=Scrollbar(searchFrame,orient=HORIZONTAL, command=self.searchBox.xview)
        scrollBar.grid(column=0, row=1,sticky=(E,W))
        self.searchBox['xscrollcommand']=scrollBar.set
        fileList = os.listdir()                                                 #Gets the current directory files
        for item in fileList:
            self.searchBox.insert('end',item)
        self.searchBox.bind('<ButtonRelease-1>', self.on_click_listbox)

    def on_click_listbox(self, event):
        index = self.searchBox.curselection()                                   #Get selected line index
        self.selectedFile = self.searchBox.get(index)                           #Get the line's text
        Label(root,text='Selected: '+self.selectedFile).grid(column=1,row=0,sticky=(E,W))

    def deleteSelected(self):                                                   #Only deletes from ListBox, that you want to use
        self.searchBox.delete('anchor')                                         #Error trappin in this procedure
        Label(root,text='Deleted: '+self.selectedFile).grid(column=1, row=1)

    def insertText(self):                                                       #Only insert to Listbox what you want
        Label(root, text='Press Return to Add').grid(column=1, row=3, sticky=(E,W))
        self.myInputs=''
        self.Entry1=Entry(root)
        self.Entry1.grid(column=1, row=2)
        self.Entry1.focus()
        self.Entry1.bind("<Return>", self.addListBox)

    def addListBox(self, event):
        self.searchBox.insert(END, self.Entry1.get())                           #Error trapping

if __name__=="__main__":
    root = Tk()
    root.title("RyMax Window on the world")
    root.geometry("200x150+200+10")                                             #Width, Height, x location, y location
    setup()
    root.mainloop()