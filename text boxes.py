Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> from tkinter import ttk
>>> root = Tk()
>>> entry = ttk.Entry(root, width = 30)
>>> entry.pack()
>>> entry.get()
'Hello, Tkinter!'
>>> entry.delete(0,1)
>>> entry.delete(0,END)
>>> entry.insert(0, 'Enter your password')
>>> entry.config(show = '*')
>>> entry.get()
'Enter your password'
>>> entry.state(['disabled'])
('!disabled',)
>>> entry.state(['!disabled'])
('disabled',)
>>> entry.state(['readonly'])
('!readonly',)
>>> 
