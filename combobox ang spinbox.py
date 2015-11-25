Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from tkinter import*
>>> from tkinter import ttk
>>> root = Tk()
>>> month = StringVar()
>>> combobox = ttk.Combobox(root, textvariable = month)
>>> combobox.pack()
>>> combobox.config(values=('January','February'))
>>> month.get()
''
>>> mont.set('January')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    mont.set('January')
NameError: name 'mont' is not defined
>>> month.set('January')
>>> month.set('Not a month')
>>> month.get()
'Not a month'
>>> year = StringVar()
>>> Spinbox(root, from_ = 1990, to = 2015, textvariable = year).pack()
>>> year.get()
'1990'
>>> year.set('2015')
>>> year.get()
'2015'
>>> 
