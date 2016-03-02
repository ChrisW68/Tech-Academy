# write-html.py
import webbrowser
from tkinter import*

def add_text():
    global in_html
    in_html = html_text.get()
    print (in_html)
    label1 = Label(root, text="This will be placed in HTML document")
    label1.pack()

def add_page():
    webbrowser.open_new_tab('STAY_TUNED.html')

def loadRecord():
    cont = sqlite3.connect('html_selection.db')
    c = cont.cursor()
    c.execute('SELECT * FROM content')
    mydata = c.fetchall()
    for row in mydata:
        list.get(row)

#Bind listbox selection into entry field
def get_list(event):
    index = listbox1.curselection()[0]
    seltext = listbox1.get(index)
    enter1.delete(0, 50)
    enter1.insert(0, seltext)

#Bind entry text into listbox
def loadRecord():
    cont = sqlite3.connect('test.db')
    c = cont.cursor()
    c.execute('SELECT * FROM content')
    my data = c.fetchall()
    for row in mydata:
        list.get(row)

root = Tk()
root.title("What would you like to enter for HTML text?")
root.geometry("450x165")
html_text_label = Label(root, text="Text to enter:")
html_text_label.pack()

listbox1 = tk.Listbox(root, width=50, height = 15)
listbox1.grid(row=0, column=0)
list_box1.bind('<ButtonRelease-1>', get_list)


enter_button = Button(root, text="Enter", command=add_text)
enter_button.pack()

insert_button = Button(root, text="Webpage insert", command=add_page)
insert_button.pack()
      
root.mainloop()

f = open('STAY_TUNED.html','w')

message = in_html

if __name__ == "__main__":
    f.write('''<html><head></head><body><p>''')
    f.write(message)
    f.write('''</p></body></html>''')
    f.close()




