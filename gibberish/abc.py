_list = [i for i in range(1, 8)]

# print(_list)


def gen():
  for i in range(len(_list)-1,-1,-1):
    yield _list[i]

g = gen()

for i in range(len(_list)):
  print(next(g))








# import pygame

# default_Color_bg = (100,100,100)
# blue = (0,0,255)

# sprite = pygame.draw.rect(surface, blue, [200,200,50,50])

# pygame.init()
# surface = pygame.display.set_mode((800,600))
# pygame.display.set_caption('some animation')

# close = False

# while not close:
#   for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#       close = True
    
#     if event.type == pygame.KEYDOWN:
#       if event.key == pygame.K_RIGHT:
#         character.move(1,0) 




# class char:
#   def __init__(self, x, y, sprite):
#     self.x = x
#     self.y = y
#     self.sprite = sprite

#   def draw(self):
#     surface.blit(sprite, (self.x*32, self.y*32))

#   def





# def drawChar():
#   global character
#   surface.fill(default_Color_bg)
#   character = pygame.draw.rect()



#   pygame.quit()
#   exit()