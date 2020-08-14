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
