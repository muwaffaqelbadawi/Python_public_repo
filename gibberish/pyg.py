import pygame
from parameters import dimensions, colors, icons

class Window:
  def __init__(self):
    self.init = pygame.init()
    self.surface = pygame.display.set_mode((dimensions.width, dimensions.height))
    self.app_name = pygame.display.set_caption('Flex')
    self.forward_button = icons.forward_button

class Buttons:
  def __init__(self):
    pass




def Apploop():
  w = Window()
  b = Buttons()
  quitApp = False
  while not quitApp:
    w.surface.fill(colors.white)
    w.surface.blit(w.forward_button, (dimensions.forward_button_x, dimensions.forward_button_y))
    pygame.display.update()
    
    for event in pygame.event.get():
      print(event.dict.get('pos'))
      print((dimensions.forward_button_x, dimensions.forward_button_y))
      if event.type == pygame.QUIT:
        quitApp = True
      # elif event.dict.get('pos') == (dimensions.forward_button_x, dimensions.forward_button_y):
      #   print('forward button has been hover over it')
  pygame.quit()
  raise SystemExit

if __name__ == "__main__":
  Apploop()