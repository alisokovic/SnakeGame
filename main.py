import random
import sys
import pygame
from pygame.math import Vector2



pygame.init()


cell_size = 60
cell_col_number = 30
cell_row_number = 15
screen_size = (int(cell_col_number*cell_size) , int(cell_row_number*cell_size))

screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()
    clock.tick(60)