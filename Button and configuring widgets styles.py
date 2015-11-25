Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> from tkinter import *
from tkinter import ttk        
    
root = Tk()
SyntaxError: multiple statements found while compiling a single statement
>>> rom tkinter import *
SyntaxError: invalid syntax
>>> from tkinter import ttk
>>> root = Tk()
>>> button1 = ttk.Button(root, text = 'Button 1')
>>> button2 = ttk.Button(root, text = 'Button 2')
>>> button3 = ttk.Button(root, text = 'Button 3')
>>> button1.pack()
>>> button2.pack()
>>> button3.pack()
>>> style = ttk.Style()
>>> style.theme_names()
('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
>>> style.theme_use()
'vista'
>>> style.theme_use('clam')
>>> style.theme_use('alt')
>>> style.theme_use('xpnative')
>>> style.theme_use('vista')
>>> button1.winfo_class()
'TButton'
>>> style.configure('TButton', foreground = 'blue')
{}
>>> style.configure('Alarm.TButton', foreground = 'orange', font = ('Arial', 24, 'bold'))
{}
>>> button2.config(style = 'Alarm.TButton')
>>> style.map('Alarm.TButton', foreground = [('pressed', 'pink'), ('disabled', 'grey')])
{}
>>> button2.state(['disabled'])
('!disabled',)
>>> style.layout('TButton')
[('Button.button', {'children': [('Button.focus', {'children': [('Button.padding', {'children': [('Button.label', {'sticky': 'nswe'})], 'sticky': 'nswe'})], 'sticky': 'nswe'})], 'sticky': 'nswe'})]
>>> style.element_options('Button.label')
('-compound', '-space', '-text', '-font', '-foreground', '-underline', '-width', '-anchor', '-justify', '-wraplength', '-embossed', '-image', '-stipple', '-background')
>>> style.lookup('TButton', 'foreground')
'blue'
>>> 
