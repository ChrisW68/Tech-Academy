Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> from ktinter import ttk
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    from ktinter import ttk
ImportError: No module named 'ktinter'
>>> from tkinter import ttk
>>> root = Tk()
>>> panedwindow.ttk.Panedwindow(root, orient = HORIZONTAL)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    panedwindow.ttk.Panedwindow(root, orient = HORIZONTAL)
NameError: name 'panedwindow' is not defined
>>> panedwindow = ttk.Panedwindow(root, orient = HORIZONTAL)
>>> panedwindow.pack(fill = BOTH, expand = True)
>>> frame1 = ttk.Frame(panedwindow, width = 100, height = 300, relief = sunken)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    frame1 = ttk.Frame(panedwindow, width = 100, height = 300, relief = sunken)
NameError: name 'sunken' is not defined
>>> frame1 = ttk.Frame(panedwindow, width = 100, height = 300, relief = SUNKEN)
>>> frame1 = ttk.Frame(panedwindow, width = 400, height = 400, relief = SUNKEN)
>>> panedwindow.add(frame1, weight = 1)
>>> panedwindow.add(frame2, weight = 4)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    panedwindow.add(frame2, weight = 4)
NameError: name 'frame2' is not defined
>>> frame2 = ttk.Frame(panedwindow, width = 400, height = 400, relief = SUNKEN)
>>> frame1 = ttk.Frame(panedwindow, width = 100, height = 300, relief = SUNKEN)

>>> panedwindow.add(frame1, weight = 1)
>>> panedwindow.add(frame2, weight = 4)
>>> frame3 = ttk.Frame(panedwindow, width = 50, height = 400, relief = SUNKEN)
>>> panedwindow.insert(1, frame3)
>>> panedwindow.forget(0)
>>> panedwindow.
