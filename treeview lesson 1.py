Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> from tkinter import ttk
>>> root = Tk()
>>> treeview = ttk.Treeview(root)
>>> treeview.pack()
>>> treeview.insert('', '0', 'item1', text = 'First Item')
'item1'
>>> treeview.insert( '', '1', 'item2', text = 'Second Item')
'item2'
>>> treeview.insert( '', 'end', 'item3', text = 'Third Item')
'item3'
>>> logo = PhotoImage(file = 'C:\\Users\\wise_\\Pictures\\python_logo.gif').subsample(10,10)
>>> treeview.insert('item2', 'end', 'python', text = 'Python', image = logo)
'python'
4
>>> treeview.config(height = 5)
>>> treeview.move('item2', 'item1', 'end')
>>> treeview.item('item1', open = True)
{}
>>> treeview.item('item', 'open')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    treeview.item('item', 'open')
  File "C:\Users\wise_\AppData\Local\Programs\Python35\lib\tkinter\ttk.py", line 1351, in item
    return _val_or_dict(self.tk, kw, self._w, "item", item)
  File "C:\Users\wise_\AppData\Local\Programs\Python35\lib\tkinter\ttk.py", line 297, in _val_or_dict
    res = tk.call(*(args + options))
_tkinter.TclError: Item item not found
>>> treeview.item('item1', 'open')
1
>>> treeview.detach('item3')
>>> treeview.move('item3', 'item2', '0')
>>> treeview.delete('item3')
>>> 
