Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> from tkinter import ttk
>>> root = Tk()
>>> button = ttk.Button(root, text = "Click Me")
>>> button.pack()
>>> def callback():
	print('Clicked!')

	
>>> button.config(command = callback)
>>> Clicked!
Clicked!

>>> button.invoke()
Clicked!
'None'
>>> button.instate(['disabled'])
False
>>> button.state([!disabled'])
	      
SyntaxError: invalid syntax
>>> button.state(['!disabled'])
()
>>> button.instate(['!disabled'])
True
>>> logo = PhotoImage(file = 'C:\Users\wise_\Pictures\python_logo.gif')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> logo = PhotoImage(file='C:\\Users\\wise_\\Pictures\\python_logo.gif')
>>> button.config(image=logo,compound = LEFT)
>>> small_logo=logo.subsample(5,5)
>>> button.config(image=small_logo)
>>> 
