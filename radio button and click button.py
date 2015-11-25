Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> from tkinter import ttk
>>> root = Tk()
>>> checkbutton = ttk.Checkbutton(root, text = 'Spam?')
>>> checkbutton.pack()
>>> spam = StringVar()
>>> spam.set('Spam!')
>>> spam.get()
'Spam!'
>>> checkbutton.confg(variable = spam, onvalue = 'Spam please!', offvalue = 'No')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    checkbutton.confg(variable = spam, onvalue = 'Spam please!', offvalue = 'No')
AttributeError: 'Checkbutton' object has no attribute 'confg'
>>> checkbutton.config(variable = spam, onvalue = 'Spam please!', offvalue = 'No')
>>> spam.get()
'Spam!'
>>> spam.get()
'Spam!'
>>> breakfast = StringVar()
>>> ttk.Radiobutton(root, text = 'Spam', variable = breakfast, value = 'Spa,').pack()
>>> ttk.Radiobutton(root, text = 'Eggs', variable = breakfast, value = 'Egss').pack()
>>> ttk.Radiobutton(root, text = 'Ham', variable = breakfast, value = 'Ham').pack()
>>> ttk.Radiobutton(root, text = 'Spam', variable = breakfast, value = 'Spa,').pack()
>>> breakfast.get()
'Spa,'
>>> checkbutton.config(textvariable = breakfast)
>>> 
