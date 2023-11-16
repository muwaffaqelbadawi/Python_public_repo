import pygame

d_width = 600
d_height = 800

white = (255,255,255)

clock = pygame.time.Clock()

target = pygame.image.load('./target_pratice.png')
shooter = pygame.image.load('./shooter.png')



block_size = 20

FPS = 30


pygame.init()
gameDisplay = pygame.display.set_mode((d_width,d_height))
pygame.display.set_caption('shooter Zak')



def GameLoop():
  
  x = d_width/2
  y = d_height/2

  move_x = 10
  move_y = 0
  
  GameExit = False

  while not GameExit:
    
    gameDisplay.fill(white)
    gameDisplay.blit(target, (500,100))
    gameDisplay.blit(target, (350,100))
    gameDisplay.blit(target, (200,100))
    gameDisplay.blit(target, (50,100))
    
    gameDisplay.blit(shooter, (300,400))
    pygame.display.update()
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        GameExit = True
        
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          move_x = -block_size
          move_y = 0
          
        
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          move_x = block_size
          move_y = 0

    x += move_x
    y += move_y
        
    clock.tick(FPS)


  pygame.quit()
  raise SystemExit




if __name__ == '__main__':
  GameLoop()