import os
import tkinter as tk
from tkinter import filedialog



real_path = os.path.relpath()


root = tk.Tk()

root.minsize(300,500)

filedialog.askdirectory()

first_label = tk.Label(root, text="This is my first tkinter label")
first_label.pack()

first_box = tk.Listbox(root)
first_box.pack()

firs_button = tk.Button(root, text="my_first_button")
firs_button.pack()


root.mainloop()
