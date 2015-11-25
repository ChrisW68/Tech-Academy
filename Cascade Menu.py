Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> fgrom tkinter import *
SyntaxError: invalid syntax
>>> from tkinter import *
>>> root = Tk()
>>> root.option_add('*tearOff', False)
>>> menubar = Menu(root)
>>> root.config(menu = menubar)
>>> file = Menu(menubar)
>>> edit = Menu(menubar)
>>> help_ = Menuu(menubar)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    help_ = Menuu(menubar)
NameError: name 'Menuu' is not defined
>>> help_ = Menu(menubar)
>>> menubar.add_cascade(menu = file, label = 'file')
>>> menubar.add_cascade(menu = edit, label = 'edit')
>>> menubar.add_cascade(menu = help_, label = 'Help')
>>> file.add_command(label = 'New', command = lambda: print('NewFile'))
>>> file.add_separator()
>>> file.add_command(label = 'Open', command = lambda: print('Open File'))
>>> file.add_command(label = 'Save', command = lambda: print('Save File'))
>>> file.entryconfig('New', accelerator = 'Ctrl + N')
>>> logo = PhotoImage(file = 'C:\\Users\\wise_\\Pictures\\python_logo.gif').subsample(10,10)
>>> file.entryconfig('Open', image = logo, compound = 'left')
>>> file.entryconfig('Open', state = 'disabled')
>>> file.delete('Save')
>>> save = Menu(file)
>>> file.add_cascade(menu = save, label = 'Save')
>>> save.add_command(label = 'Save As', command = lambda: print('Save As'))
>>> save.add_command(label = 'Save All', command = lambda: print('Save All'))
>>> choice = IntVar()
>>> edit.add_radiobutton(label = 'One', variable = choice, value = 1)
>>> edit.add_radiobutton(label = 'Two', variable = choice, value = 2)
>>> edit.add_radiobutton(label = 'Three', variable = choice, value = 3)
>>> file.post(400, 300)
