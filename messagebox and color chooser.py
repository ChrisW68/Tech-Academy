Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from tkinter import messagebox
>>> messagebox.showinfo
<function showinfo at 0x0000005BFE58F840>
>>> messagebox.showinfo(title = 'A Friendly message', 'Hello Enter')
SyntaxError: positional argument follows keyword argument
>>> messagebox.showinfo(title = 'A Friendly message', message = 'Hello Enter')
'ok'
>>> messagebox.askyesno(title = "Hungry", mesage = "Want something to eat")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    messagebox.askyesno(title = "Hungry", mesage = "Want something to eat")
  File "C:\Users\wise_\AppData\Local\Programs\Python35\lib\tkinter\messagebox.py", line 104, in askyesno
    s = _show(title, message, QUESTION, YESNO, **options)
  File "C:\Users\wise_\AppData\Local\Programs\Python35\lib\tkinter\messagebox.py", line 72, in _show
    res = Message(**options).show()
  File "C:\Users\wise_\AppData\Local\Programs\Python35\lib\tkinter\commondialog.py", line 48, in show
    s = w.tk.call(self.command, *w._options(self.options))
_tkinter.TclError: bad option "-mesage": must be -default, -detail, -icon, -message, -parent, -title, or -type
>>> messagebox.askyesno(title = "Hungry", message = "Want something to eat")
True
>>> from tkinter import filedialog
>>> filedialog.askopenfile()
>>> filename = filedialog.askopenfile()
>>> filename.name()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    filename.name()
TypeError: 'str' object is not callable
>>> filename.name
'C:/Users/wise_/Documents/GitHub/The-Tech_Courses/Tech-Academy/paned window.py'
>>> from tkinter import colorchooser
>>> colorchooser.askcolor(initialcolor = 'Green')
((0.0, 128.5, 192.75), '#0080c0')
>>> 
