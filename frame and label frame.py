Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from Tkinter import *
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    from Tkinter import *
ImportError: No module named 'Tkinter'
>>> from tkinter import*
>>> from tkinter import ttk
>>> root = Tk()
>>> frame = ttk.Frame(root)
>>> frame.pack()
>>> frame.config(height=100, width=200)
>>> frame.config(relief = RIDGE)
>>> ttk.Button(frame, text = 'Click Me!').grid()
4
>>> frame.config(padding = (30, 15))
>>> ttk.LabelFrame(root, height = 100, width = 200, text = 'My Frame').pack()
>>> 
