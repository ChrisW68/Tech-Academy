Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> root = Tk()
>>> canvas = Canvas(root)
>>> canvas.pack()
>>> canvas.config(width = 640, height= 480)
>>> line = canvas.create_line(160, 360, 480, 120, fill = 'blue', width = 5)
>>> canvas.itemconfigure(line, fill = 'green')
>>> canvas.coords(line)
[160.0, 360.0, 480.0, 120.0]
>>> canvas.coords(line, 0, 0, 112, 198, 640,0)
[]
>>> canvas.itemconfigure(line, smooth =True)
>>> canvas.itemconfigure(line, splinesteps=5)
>>> canvas.itemconfigure(line, splinesteps=100)
>>> canvas.delete(line)
>>> 
