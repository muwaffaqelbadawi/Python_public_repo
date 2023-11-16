import os
import pygame
import tkinter as tk
from tkinter.filedialog import askdirectory, askopenfile
from pprint import pprint

cwd = askdirectory()

list_file = os.listdir(cwd)
for file in list_file:
    if file.endswith(".png") == True:
       print(file)
