Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> root = Tk()
>>> window = Toplevel(root)
>>> window.title('New Window')
''
>>> window.lower()
>>> window.lift(root)
>>> window.state('zoomed')
''
>>> window.state('withdrawn')
''
>>> window.state('iconic')
''
>>> window.state('normal')
''
>>> window.state()
'zoomed'
>>> window.state('normal')
''
>>> window.iconify()
''
>>> window.deiconify()
''
>>> window.geometry('640X480+50+00)
		
SyntaxError: EOL while scanning string literal
>>> window.geometry('640X480+50+00')
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    window.geometry('640X480+50+00')
  File "C:\Users\wise_\AppData\Local\Programs\Python35\lib\tkinter\__init__.py", line 1685, in wm_geometry
    return self.tk.call('wm', 'geometry', self._w, newGeometry)
_tkinter.TclError: bad geometry specifier "640X480+50+00"
>>> window.geometry('640x480+50+100')
''
>>> window.resizable(False, False)
''
>>> window.maxsize(640, 480)
>>> window.minsize(200,200)
>>> window.resizable(True, True)
''
>>> root.destroy()
>>> 
