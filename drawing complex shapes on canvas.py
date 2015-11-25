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
>>> rect = canvas.create_rectangle(50, 120, 200, 300)
>>> canvas.itemconfigure(rect, fill = 'yellow')
>>> oval = canvas.create_oval(50, 120, 200, 300)
>>> arc = canvas.create_arc (160,1, 120,300)
>>> canvas.itemconfigure(arc, start = 0, extent = 180, fill = 'green')
>>> poly = canvas.create_polygon(160, 360, 320, 480, 480, 360)
>>> text = canvas.create_text(320, 240, text = 'Python', font = ('Courier', 32 'bold'))
SyntaxError: invalid syntax
>>> text = canvas.create_text(320, 240, text = 'Python', font = ('Courier', 32, 'bold'))
>>> logo = PhotoImage(file = 'C:\\Users\\wise_\\Pictures\\python_logo.gif')
>>> image = canvas.create_image(320, 340, image = logo)
>>> canvas.lift(text)
>>> canvas.lower(image)
>>> canvas.lower(image, text)
>>> button = Button(canvas, text = 'Click Me')
>>> canvas.create_window(320, 60, window = button)
8
>>> canvas.itemconfigure(rect, tag = ('shape'))
>>> canvas.itemconfigure(oval, tag = ('shape', 'round'))
>>> canvas.itemconfigure('shape', fill = 'grey')
>>> canvas.gettags(oval)
('shape', 'round')
>>> 
