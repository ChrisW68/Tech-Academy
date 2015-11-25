Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from tkinter import
SyntaxError: invalid syntax
>>> from tkinter import *
>>> from tkinter import ttk
>>> root = Tk()
>>> progressbar = ttk.Progressbar(root, orient = HORIZONTAL, length = 200)
>>> progressbar.pack()
>>> progressbar.config(mode = 'indeterminate')
>>> progressbar.start()
>>> progressbar.stop()
>>> progressbar.config(mode = 'determinate', maximum = 11.0, value = 4.2)
>>> progressbar.config(value = 8.0)
>>> progressbar.step()
>>> progressbar.step(5)
>>> value = DoubleVar()
>>> progressbar.config(variable = value)
>>> scale = ttk.Scale(root, orient = HORIZONTAL, length = 400, variable = value, from_= 0.0, to = 11.0)
>>> scale.pack()
>>> scale.set(4.2)
>>> scale.get()
4.2
>>> 
