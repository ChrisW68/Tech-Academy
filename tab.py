Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> from tkinter import ttk
>>> root = Tk()
>>> notebook = ttk.Notebook(root)
>>> notebook.pack()
>>> frame1 = ttk.Frame(notebook)
>>> frame2 = ttk.Frame(notebook)
>>> notebook.add(frame1, text = 'One')
>>> notebook.add(frame2, text = 'Two')
>>> ttk.Button(frame1, text = 'Click Me').pack()
>>> frame3.ttk.Frame(notebook)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    frame3.ttk.Frame(notebook)
NameError: name 'frame3' is not defined
>>> frame3 = ttk.Frame(notebook)
>>> notebook.insert(1, frame3, text = 'Three')
>>> notebook.forget(1)
>>> notebook.add(frame3, text = 'Three')
>>> notebook.select()
'.779599348176.779601727896'
>>> notebook.index(notebook.select())
0
>>> notebook.select(2)
''
>>> notebook.tab(1, state = 'disabled')
{}
>>> notebook.tab(1, state = 'hidden')
{}
>>> notebook.tab(1, state = 'normal')
{}
>>> notebook.tab(1, 'text')
'Two'
>>> notebook.tab(1)
{'padding': [0], 'state': 'normal', 'image': '', 'sticky': 'nsew', 'text': 'Two', 'underline': -1, 'compound': 'none'}
>>> 
