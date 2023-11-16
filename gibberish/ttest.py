import tkinter as tk
from tkinter import Label


root = tk.Tk()
# root.withdraw()

l  = Label(root, width=5, height=5, bg='red')
l.grid(row=1, column=1)

root.mainloop()