from tkinter import *
from tkinter import ttk

root = Tk()

entry = ttk.Entry(root)
entry.pack()

entry.bind('<<Copy>>', lambda e: print('Copy'))
entry.bind('<<Paste>>', lambda e: print('Paste'))          

root.mainloop()
