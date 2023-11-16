import os
import tkinter as tk
from tkinter.filedialog import askdirectory as askdir
from mutagen.mp3 import MP3
# # from pygame import mixer

folder_dir = None

list_of_dirs = []

categories = dict(
  Songs = [],
  Artists = [],
  Albums = [],
  Genres = []
)

class Main(object):
  def __init__(self):
    self.root = tk.Tk()
    self.root.withdraw()

class Root(object):
  def __init__(self, _dir, file_name):
    self.dir = _dir
    self.file_name = file_name

class Object(object):
  def __init__(self, root):
    self.obj = MP3('{0}/{1}'.format(root.dir, root.file_name))
    self.file_name = os.path.basename(self.obj.filename)
    self.full_path = self.obj.filename

# iformation

  def Extract_tags(self):
    try:
      self.title = self.obj['TIT2'].text[0]
    except KeyError:
      self.title = 'UNKNOWN'
      
    try:
      self.artist = self.obj['TPE1'].text[0]
    except KeyError:
      self.artist = 'UNKNOWN'
      
    try:
      self.album = self.obj['TALB'].text[0]
    except KeyError:
      self.album = 'UNKNOWN'
      
    try:
      self.genre = self.obj['TCON'].text[0]
    except KeyError:
      self.genre = 'UNKNOWN'

  def Length_Format(self):
    mins, secs = divmod(self.obj.info.length, 60)
    self.length = '{:.0f}:{:.0f}'.format(round(mins), round(secs))
    
  def Bitrate(self):
    self.bitrate = '{:.0f}'.format(round(self.obj.info.bitrate/1000))

class Categories(object):
  def __init__(self, obj):
    self.obj = obj

  def classify(self):
    categories['Songs'].append(self.obj.title)
    categories['Artists'].append(self.obj.artist)
    categories['Albums'].append(self.obj.album)
    categories['Genres'].append(self.obj.genre)

def folder_selection(_dir):
    list_of_dirs.append(_dir)

def extract_info(dirs):
  for _dir in dirs:
    for file_name in os.listdir(_dir):
      root = Root(_dir, file_name)
      obj = Object(root)
      obj.Extract_tags()
      obj.Length_Format()
      obj.Bitrate()
      category = Categories(obj)
      category.classify()

main = Main()
# extract_info(list_of_dirs)

# for i in range(3):
#   folder_selection(askdir())

folder_selection(askdir())

print(list_of_dirs)
