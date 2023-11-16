from song import*
from parameters import*
from tkinter import*


class Window:
  def __init__(self):
    self.root = Tk()
    self.root.title('Flex')
    self.root.geometry('{width}x{height}+{x}+{y}'.format(width=mw_coordinates.height, height=mw_coordinates.width,x=0,y=0))
    # self.root.configure(width=mw_coordinates.height, height=mw_coordinates.width)
    # self.frame = Frame(self.root, width=mw_coordinates.height, height=mw_coordinates.width, bd=2, bg= '#{:x}{:x}{:x}'.format(*color.gray))
    # self.frame.pack()

class Button:
  def __init__(self, root):
    self.root = root
    self.quit = self.root.protocol('WM_DELETE_WINDOW', self.root.quit)


class Song_list:
  def __init__(self, root):
    self.song_list = Listbox(root, width=w_size.width, height=w_size.height)
    self.song_list.pack()
    # self.song_list.grid(row=1, column=2)


if __name__ == '__main__':
  main_window = Window()
  song_list = Song_list(main_window.root)
  button = Button(main_window.root)
  main_window.root.mainloop()