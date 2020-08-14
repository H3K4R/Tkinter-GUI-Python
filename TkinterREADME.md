# Tkinter-GUI-Python
Python GUI Development with Tkinter, basics and full step by step process
# Tkinter-GUI-Python
Python GUI Development with Tkinter, basics and full step by step process

All are done in IDLE, 
open IDLE |_>

# Now Write:
  >>import tkinter 
  >>import _tkinter
  >>tkinter._test()
  (If all commands run successfully, then your setup is ready)
  
# Let's WRITE YOUR FIRST """HELLO TKINTER""" GUI:::-
{
  from tkinter import *
  root = Tk()
  Label(root, text="Hello, Tkinter ! GUI !!").pack()
  root.mainloop()
}

# WHAT IS TK????
Ans:- Tk is an open source toolkit used to develop Graphical User Interface. It provides a library of interactive widgets which are GUI elements commonly used in Desktop applications. These are things like Buttons, Menus, windows and text entry fields. Tk was developed back in the early '90s as an extension for a scripting language called "Tool Command Language", which is abbreviated as Tcl and often pronounced "tickle". It was designed to be platform independent on most versions of windows, mca, linux. 

# HOW THE WHOLE PROCESS WORKS::--
Ans:- 
{Your Application(Python)}
  |
  {Tkinter(Python module)}
    |
    { _tkinter(C)}
      |
      {Tk widgets(C and Tcl)}
        |
        {Tk(C)}
          |
          {Xlib(C)
          
# CREATING AND CONFIGURE WIDGET:

## Each of the Widget is a "Class" ##
>>from tkinter import *
>>from tkinter import ttk
>>root = Tk()
>>button = ttk.Button(root, text ='Click Me')
>>button.pack()
>>button['text']
>>button['text] = 'Press Me'
>>button.config[text] = 'Push Me')
>>button.config() //it shows the whole Disctionary
>>str(button
>>str(root)
>>ttk.Label(root, text = 'Hello, Tkinter').pack()

# Managing widget:

## Pack Geometry Manager:-

Define edge of parant to pack widget master
Example: widget.pack(side = RIGHT)

## Grid Geometry Manager:-

Define row/column of two-dimentional table in master
Example: widget.grid(row = 0, column = 1)

## Place Geometry Manager:-
Define relative or absolute x/y coordinates in master
Example: widget.place(x = 200, y = 150)

# Display Text and Image using Label:-

## Text ##
>>label.config(text = "hello Swarnava , How are you ???")
>>label.config(wraplength = 150)
>>label.config(justify = CENTER)
>>label.config(foreground = 'blue', background = 'yellow')
>>label.config(font = ('Courier', 18, 'bold'))

## Image ##
>>PhotoImage(file = '--path of the image file--')
>>label.config(image = logo)
Hold the Image logo in a variable:
>>label.img = logo
>>label.config(image = label.img)


#### View Image and Text both at the same time:-
>>label.config(compound = 'text)
>>label.config(compound = 'center')

# Capturing input with buttons
>>> from tkinter import *
>>> from tkinter import ttk
>>> root = Tk()
>>> button = ttk.Button(root, text ="Click Me")
>>> button.pack()
>>> def callback():
	print('Clicked!')

	
>>> button.config(command = callback)
>>> Clicked!
Clicked!
Clicked!
Clicked!
Clicked!
Clicked!
SyntaxError: invalid syntax
>>> 
>>> button.invoke()
Clicked!
'None'
>>> button.state(['disabled'])
('!disabled',)
>>> button.instate(['disabled'])
True
>>> button.state(['disabled'])
()
>>> button.instate(['disabled'])
True




# Presenting Choice with check buttons and Radio Buttons
### Checkbuttons
>>> from tkinter import *
>>> from tkinter import ttk
>>> root = Tk()
>>> checkbutton = ttk.Checkbutton(root, text = 'SPAM')
>>> checkbutton.pack()

### Radio Buttons
>>> radiobutton = ttk.Radiobutton(root, text = 'HOLA')
>>> radiobutton.pack()

# Single-line text with the Entry widget
>>> from tkinter import *
>>> from tkinter import ttk
>>> root = Tk()
>>> entry = ttk.Entry(root, width = 30)
>>> entry.pack()
### Get the Input field message
>>> entry.get()
'Hello Python'
### Delete the indexed 
>>> entry.delete(0, 1)
>>> entry.get()
'ello Python'
### Delete the whole message
>>> entry.delete(0, END)
>>> entry.get()
''
>>> 
### Enter new Message
>>> entry.insert(0, 'Enter your password')
>>> entry.get()
'Enter your password'
>>> 
### Hide Message
entry.config(show = '*')

# Makig selection with the Combobox and Spinbox
### Combobox
>>> from tkinter import *
>>> from tkinter import ttk
>>> root = Tk()
>>> month = StringVar()
>>> combobox = ttk.Combobox(root, textvariable = month)
>>> combobox.pack()
>>> combobox.config(values = ('Jan','Jan','Jan','Jan','Jan','Jan','Jan','Jan',)
		)
>>> month.get()
''
>>> month.get()
'Jan'

### Spinbox
>>> year = StringVar()
>>> Spinbox(root, from_ = 1990, to =2020, textvariable = year).pack() //We can't use ttk.spinbox because it's not ttk module
>>> year.get()
'2009'
>>> 

#Progressbar
>>> from tkinter import *
>>> from tkinter import ttk
>>> root = Tk()
>>> progressbar = ttk.Progressbar(root, orient = HORIZONTAL, length = 200)
>>> progressbar.pack()
>>> progressbar.config(mode = 'indeterminate')
>>> progressbar.start()
>>> progressbar.stop()
>>> progressbar.config(mode = 'determinate', maximun = 11.0, value = 4.2)

### To increase the bar
>>> progressbar.config(mode = 'determinate', maximum = 11.0, value = 4.2)
>>> progressbar.config(value = 8.0)
### Increase by One
>>>progressbar.step()
### Increase by 2 or More
>>>progressbar.step(2)

# Organizing widget with Frames
Type of Frames "relief":-
1.FLAT
2.RAISED
3.SUNKEN
4.SOLID
5.RIDGE
6.GROOVE
### Create frames
>>> from tkinter import *
>>> from tkinter import ttk
>>> root = Tk()
>>> frame = ttk.Frame(root)
>>> frame.pack()
>>> frame.config(height = 100, width = 200) // because by default it is 0 width and height.
>>> 

### different type of frame config
>>> frame.config(relief = RIDGE)
>>> frame.config(relief = SOLID)
>>> frame.config(relief = SUNKEN)
>>> 

# Creating Addintional top-level windows
>>> from tkinter import *
>>> root = Tk()
>>> window = Toplevel(root)
>>> window.title('New Window')
''
>>> window.lower()
>>> window.lift(root)
>>> window.state('zoomed')
''
>>> 
>>> window.state('withdrawn')
''
>>> window.state('iconic')
''
>>> window.state('normal')
''
>>> 

# Paned Window
>>> from tkinter import *
>>> from tkinter import ttk
>>> root = Tk()
>>> panedwindow = ttk.Panedwindow(root, orient = HORIZONTAL)
>>> panedwindow.pack(fill = BOTH, expaned = True)
>>> panedwindow.pack(fill = BOTH, expand = True)
>>> frame1 = ttk.Frame(panedwindow, width = 100, height = 300, relief = SUNKEN)
>>> frame2 = ttk.Frame(panedwindow, width = 400, height = 400, relief = SUNKEN)
>>> panedwindow.add(frame1, weight = 1)
>>> panedwindow.add(frame2, weight = 4)
>>> frame3 = ttk.Frame(panedwindow, width = 50, height = 400, relief = SUNKEN)
>>> panedwindow.insert(1, frame3)
>>> 

# Tabbed Notebook
>>> from tkinter import *
>>> from tkinter import ttk
>>> root = Tk()
>>> notebook = ttk.Notebook(root)
>>> notebook.pack()
>>> frame1 = ttk.Frame(notebook)
>>> frame2 = ttk.Frame(notebook)
>>> notebook.add(frame1, text='One')
>>> notebook.add(frame2, text='Two')
>>> 

# Event Handling

### Configuiring command callbacks

from tkinter import *
from tkinter import ttk

root = Tk()

def callback(number):
    print(number)
ttk.Button(root, text = 'Click Me 1', command = lambda:callback(1)).pack()
ttk.Button(root, text = 'Click Me 2', command = lambda:callback(2)).pack()
ttk.Button(root, text = 'Click Me 3', command = lambda:callback(3)).pack()


root.mainloop()

### Buildig to Keyboard event

from tkinter import *
from tkinter import ttk

root = Tk()

def key_press(event):
    print('type: {}'.format(event.type))
    print('widget: {}'.format(event.widget))
    print('char: {}'.format(event.char))
    print('keysym: {}'.format(event.keysym))
    print('keycode: {}'.format(event.keycode))

root.bind('<KeyPress>', key_press)

root.mainloop()

# Building Mouse Events
from tkinter import *
from tkinter import ttk

root = Tk()

def mouse_press(event):
    global prev
    prev = event
    print('type: {}'.format(event.type))
    print('widget: {}'.format(event.widget))
    print('num: {}'.format(event.num))
    print('x: {}'.format(event.x))
    print('y: {}'.format(event.y))
    print('x_root: {}'.format(event.x_root))
    print('y_root: {}'.format(event.y_root))

canvas = Canvas(root, width=640, height = 480, background = 'white')
canvas.pack()

def draw(event):
    global prev
    canvas.create_line(prev.x, prev.y, event.x, event.y, width = 5)
    prev =event

canvas.bind('<ButtonPress>', mouse_press)
canvas.bind('<B1-Motion>', draw)

root.mainloop()


# Virtual Events
from tkinter import *
from tkinter import ttk

root = Tk()

entry = ttk.Entry(root)
entry.pack()

entry.bind('<<Copy>>', lambda e: print('Copy'))
entry.bind('<<Paste>>', lambda e: print('Paste'))          

root.mainloop()

# Multiple events
from tkinter import *
from tkinter import ttk

root = Tk()


label1 = ttk.Label(root, text = 'Label 1')
label2 = ttk.Label(root, text = 'Label 2')
label1.pack()
label2.pack()

label1.bind('<ButtonPress>', lambda e: print('ButtonPress Label'))
label1.bind('<1>', lambda e: print('<1> Label'))

root.mainloop()





