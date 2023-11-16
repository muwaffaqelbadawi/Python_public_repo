import os
import tkinter as tk
from tkinter.filedialog import askdirectory as localdir



class Infofolder:
     currentdir = localdir()
     def __init__(self):
         self.a = Infofolder.currentdir # Info folder
         self.b = os.listdir(Infofolder.currentdir)[0] # Song file


     @staticmethod
     def Info():
         return ""

Info_folder = Infofolder()
print(Info_folder.a)
print(Info_folder.b)
