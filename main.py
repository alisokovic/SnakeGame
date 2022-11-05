import pygame,sys,random
from pygame.math import Vector2


pygame.init()

cell_size = 40
cell_number = 20
screen_size = int(cell_number*cell_size)

screen = pygame.display.set_mode((screen_size,screen_size))
screen_title = pygame.display.set_caption("Snake")
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()
    clock.tick(60)