import pygame



class dimensions:
  def __init__(self):
    self.height = 600
    self.width = 1000
    self.forward_button_x = 150
    self.forward_button_y = 550
    
class colors:
  def __init__(self):
    self.white = (255,255,255)
    self. black = (0,0,0)
    
class icons:
  def __init__(self):
    self.forward_button = pygame.image.load('../imagetest/forward_button.png')

dimensions = dimensions()
colors = colors()
icons = icons()