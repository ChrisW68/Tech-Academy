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

def htmlValues=(('This is the first line of html'),('This is a second line of html'),('This is a third line of html'))

    with sqlite3.connect(

root = Tk()
root.title("What would you like to enter for HTML text?")
root.geometry("450x165")
html_text_label = Label(root, text="Text to enter:")
html_text_label.pack()

html_text = Entry(root, bd=1)
html_text.pack()


enter_button = Button(root, text="Enter", command=add_text)
enter_button.pack()

insert_button = Button(root, text="Webpage insert", command=add_page)
insert_button.pack()
      
root.mainloop()

f = open('STAY_TUNED.html','w')

message = in_html

root.mainloop()
f.write('''<html><head></head><body><p>''')
f.write(message)
f.write('''</p></body></html>''')
f.close()




