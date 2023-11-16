import os
import pygame
from tkinter.filedialog import askdirectory, askopenfile


hight = 800
width = 600
black = (0,0,0)
white = (255,255,255)
grey = (100,100,100)


def Draw_surfice(x,y):
    global main_surface
    main_surface.fill(grey)
    main_surface.blit(play_icon, (x,y))

    pygame.display.update()

x = 300
y = 250

cwd = askdirectory()

list_file = os.listdir(cwd)
for file in list_file:
    if file.endswith(".png") == True:
       play_icon = play_icon = pygame.image.load(os.path.join(cwd, file))


def Init():
    pygame.init()
    global main_surface
    main_surface = pygame.display.set_mode((hight,width))

def Main():
    quit = False
    while not quit:
        curser = pygame.event.get()
        for move in curser:
            if move.type == pygame.QUIT:
                quit = True
        Draw_surfice(x,y)
    pygame.quit()
    exit()

Init()
Main()
