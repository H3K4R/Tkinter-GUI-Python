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
