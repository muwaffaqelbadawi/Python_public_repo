import pygame
import random

x = pygame.init()
wight = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0, 155, 0)

display_width = 800
display_height = 600

block_size = 20
FPS = 15

direction = 'right'

pygame.init()
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Slither')

img = pygame.image.load('snakeHead.png')

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 25)

def snake(block_size, snake_list):
  
  if direction == 'right':
    head = pygame.transform.rotate(img,270)
  
  if direction == 'left':
    head = pygame.transform.rotate(img,90)
    
  if direction == 'up':
    head = img
  if direction == 'down':
    head = pygame.transform.rotate(img,180)
  
  gameDisplay.blit(head, (snake_list[-1][0], snake_list[-1][1]))
  for XnY in snake_list[:-1]:
    pygame.draw.rect(gameDisplay,green,[XnY[0], XnY[1], block_size, block_size])

def text_objects(text, color):
  textSurface = font.render(text, True, color)
  return textSurface, textSurface.get_rect()

def message_to_screen(msg, color):
  textSurf, textRect = text_objects(msg, color)
  # screen_text = font.render(msg, True, color)
  # gameDisplay.blit(screen_text, [display_width/2, display_height/2])
  textRect.center = (display_width/2), (display_height/2)
  gameDisplay.blit(textSurf, textRect)


def game_loop():
  global direction
  gameExit = False
  GameOver = False

  lead_x = display_width/2
  lead_y = display_height/2

  snake_list = []
  snake_length = 1

  lead_x_change = 10
  lead_y_change = 0

  randAppleX = round(random.randrange(0, display_width-block_size))#/10.0)*10.0
  randAppleY = round(random.randrange(0, display_height-block_size))#/10.0)*10.0

  while not gameExit:

    while GameOver == True:
      gameDisplay.fill(wight)
      message_to_screen('Game Over press c to play again or q to quit', red)
      pygame.display.update()

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          GameOver = False
          gameExit = True
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_q:
            gameExit = True
            GameOver = False
          elif event.key == pygame.K_c:
            game_loop()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        gameExit = True
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          direction = 'left'
          lead_x_change = -block_size
          lead_y_change = 0
        elif event.key == pygame.K_RIGHT:
          direction = 'right'
          lead_x_change = block_size
          lead_y_change = 0
        elif event.key == pygame.K_UP:
          direction = 'up'
          lead_y_change = -block_size
          lead_x_change = 0
        elif event.key == pygame.K_DOWN:
          direction = 'down'
          lead_y_change = block_size
          lead_x_change = 0

    if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
      GameOver = True
      
    lead_x += lead_x_change
    lead_y += lead_y_change
    gameDisplay.fill(wight)
    appleThickness = 30
    
    pygame.draw.rect(gameDisplay,red,[randAppleX,randAppleY,appleThickness, appleThickness])
    
    snakeHead = []
    snakeHead.append(lead_x)
    snakeHead.append(lead_y)
    snake_list.append(snakeHead)
    
    if len(snake_list) > snake_length:
      del snake_list[0]
      
    for eachsegment in snake_list[:-1]:
      if eachsegment == snakeHead:
        GameOver = True
      
    
    snake(block_size, snake_list)
    pygame.display.update()
    
    
    # if lead_x >= randAppleX and lead_x <= randAppleX + appleThickness:
    #   if lead_y >= randAppleY and lead_y <= randAppleY + appleThickness:
    #       randAppleX = round(random.randrange(0, display_width-block_size))#/10.0)*10.0
    #       randAppleY = round(random.randrange(0, display_height-block_size))#/10.0)*10.0
    #       snake_length += 1

    if lead_x > randAppleX and lead_x < randAppleX + appleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + appleThickness:
      if lead_y > randAppleY and lead_y < randAppleY + appleThickness:
        randAppleX = round(random.randrange(0, display_width-block_size))#/10.0)*10.0
        randAppleY = round(random.randrange(0, display_height-block_size))#/10.0)*10.0
        snake_length += 1
      elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + appleThickness:
        randAppleX = round(random.randrange(0, display_width-block_size))#/10.0)*10.0
        randAppleY = round(random.randrange(0, display_height-block_size))#/10.0)*10.0
        snake_length += 1

    clock.tick(FPS)
    
  pygame.quit()
  quit()


if __name__ == '__main__':
  game_loop()