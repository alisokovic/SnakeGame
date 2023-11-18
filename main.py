import random
import sys
import pygame
from pygame.math import Vector2


class FRUIT:
    def __init__(self):
        self.color = (42,77,182)
        self.x = random.randint(0,cell_col_number - 1)
        self.y = random.randint(0,cell_row_number - 1)
        self.pos = Vector2(self.x , self.y)
        
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.x*cell_size,self.y*cell_size,cell_size,cell_size)
        pygame.draw.rect(screen,self.color,fruit_rect)




pygame.init()

cell_size = 60
cell_col_number = 30
cell_row_number = 15
screen_size = (int(cell_col_number*cell_size) , int(cell_row_number*cell_size))
screen_color = (35,188,72)

screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()


fruit = FRUIT()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    screen.fill(screen_color)
    
    fruit.draw_fruit()
            
    pygame.display.update()
    clock.tick(60)