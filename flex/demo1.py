import tkinter as tk
from tkinter import*


HEIGHT = 600
WIDTH = 800

root = tk.Tk()
main_canvas = Canvas(root, height=HEIGHT, width=WIDTH, bg='white')

header_frame = Frame(root, background='#{:x}{:x}{:x}'.format(100, 100, 100))
category_frame = Frame(root, bg='#80c1ff')


All_Songs = Label(header_frame, text='All Songs', height=2, width=9, bg='#{:x}{:x}{:x}'.format(100, 100, 100), font='Times 15', justify=CENTER)
songs = Button(category_frame, text="Songs", height=2, width=27, padx=2, bg='#80c1ff')
artists = Button(category_frame, text="Artists", height=2, width=27, padx=2, bg='#80c1ff')
albums = Button(category_frame, text="Albums", height=2, width=27, padx=2, bg='#80c1ff')
folders = Button(category_frame, text="Folders", height=2, width=27, padx=2 , bg='#80c1ff')
# song_list = Listbox(_frame, 3height=20, width=25)

# l = Label(root, text="Songs")

main_canvas.pack()
header_frame.place(relx=0, rely=0, relwidth=1, relheight=0.08)
# l.grid(row=0, column=0)
category_frame.place(relx=0, rely=0.08, relwidth=1, relheight=0.07)
All_Songs.pack()
songs.grid(row=1, column=0)
artists.grid(row=1, column=1)
albums.grid(row=1, column=2)
folders.grid(row=1, column=3)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
# song_list.grid(row=0, column=4)




root.mainloop()