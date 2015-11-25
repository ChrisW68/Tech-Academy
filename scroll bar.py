Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> from tkinter import ttk
>>> root = Tk()
>>> text = Text(root, width = 40, height = 10, wrap = 'word')
>>> text.grid(row=0, column = 0)
>>> text.grid(row = 0, column = 0)
>>> scrollbar = tkk.Scrollbar(root, orient = VERTICAL, command = text.yview)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    scrollbar = tkk.Scrollbar(root, orient = VERTICAL, command = text.yview)
NameError: name 'tkk' is not defined
>>> scrollbar = ttk.Scrollbar(root, orient = VERTICAL, command = text.yview)
>>> scrollbar.grid(row = 0, column = 1, sticky = 'ns')
>>> text.config(yscrollcommand = scrollbar.set)
>>> 
