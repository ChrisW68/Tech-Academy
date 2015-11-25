Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> root = Tk()
>>> text = Text(root, width = 40, height = 10)
>>> text.pack()
>>> text.config(wrap = 'word')
>>> text.get('1.0', end)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    text.get('1.0', end)
NameError: name 'end' is not defined
>>> text.get('1.0', 'end')
'This is a long that is more than 40 loooong\n\n\n\n\n\n\nHellow works .............................................\n'
>>> text.get('1.0', 'l.end')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    text.get('1.0', 'l.end')
  File "C:\Users\wise_\AppData\Local\Programs\Python35\lib\tkinter\__init__.py", line 3091, in get
    return self.tk.call(self._w, 'get', index1, index2)
_tkinter.TclError: bad text index "l.end"
>>> text.get('1.0', 'l.end')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    text.get('1.0', 'l.end')
  File "C:\Users\wise_\AppData\Local\Programs\Python35\lib\tkinter\__init__.py", line 3091, in get
    return self.tk.call(self._w, 'get', index1, index2)
_tkinter.TclError: bad text index "l.end"
>>> text.get('1.0', 'end')
'This is a long that is more than 40 loooong\n\n\n\n\n\n\nHellow works .............................................\n'
>>> text.insert('1.0' + 2 lines', 'Inserted Message')
	    
SyntaxError: invalid syntax
>>> text.insert('1.0 + 2 lines', 'Inserted Message')
>>> text.insert('1.0 + 2 lines lineend', 'and\nmore and\nmore...')
>>> text.delete('1.0')
>>> text.delete('1.0', '1.0 lineend')
>>> text.delete('1.0', '3.0 lineend + 1 chars')
>>> text.replace('1.0', '1.0 lineend', 'This is the first line.')
>>> text.config(state = 'disabled')
>>> text.delete('1.0', 'end')
>>> text.config(state='normal')
>>> 
