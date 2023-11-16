def a(**kwargs):
  print(kwargs.keys())


a(a=5, h=5)








# d = dict(
#   name = 'muwaffuq',
#   job = 'software engineer',
#   address = 'aljerif west'
# )

# a = {'end':'ffff'}

# b = "{end}"

# b.format(**a)

# print(b.format(**a))







# def color(*args):
#   a = '#{:x}{:x}{:x}'.format(*args)
#   print(a)
  
# color(255,255,25)


# # print('{{:02x}{:02x}{:02x}}'.format((255,255,255)))

# print('#%02x%02x%02x' % (64, 204, 208))


# from tkinter import *

# master = Tk()

# Label(text="one").pack()

# separator = Frame(height=2, bd=1, relief=SUNKEN)
# separator.pack(fill=X, padx=5, pady=5)

# Label(text="two").pack()

# mainloop()



# import tkinter as tk
# from tkinter import messagebox

# root = tk.Tk()

# def on_closing():
#     if messagebox.askokcancel("Quit", "Do you want to quit?"):
#         root.destroy()

# root.protocol("WM_DELETE_WINDOW", on_closing)
# root.mainloop()


# name = dict(a=0, b=2, c=3)

# a = {5:'f', 4:'t', 08:'t', 1:0}



# # print(list(a.items()))

# print(a.get(1,'h'))

# help(nonlocal)

# from tkinter import *

# root = Tk()
# Button(root, text="Quit", command=root.destroy).pack()
# root.mainloop()