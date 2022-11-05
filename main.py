import pygame,sys,random
from pygame.math import Vector2


class FRUIT:
    def __init__(self):
        self.color = (12,24,186)
        self.x = random.randint(0,cell_number-1)
        self.y = random.randint(0,cell_number-1)
        self.pos = Vector2(self.x,self.y)
        
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.x*cell_size,self.y*cell_size,cell_size,cell_size)
        pygame.draw.rect(screen,self.color,fruit_rect)
        
        

class SNAKE:
    def __init__(self):
        self.color = (192,22,14)
        self.body = [Vector2(7,10),Vector2(6,10),Vector2(5,10)]
        self.direction = Vector2(1,0)
        
    def draw_snake(self):
        for block in self.body:
            block_rect = pygame.Rect(block.x*cell_size,block.y*cell_size,cell_size,cell_size)
            pygame.draw.rect(screen,self.color,block_rect)
            
            
            
class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        
    def draw_elements(self):
        self.snake.draw_snake()
        self.fruit.draw_fruit()




pygame.init()

cell_size = 40
cell_number = 20
screen_size = int(cell_number*cell_size)
screen_color = (21,192,23)

screen = pygame.display.set_mode((screen_size,screen_size))
screen_title = pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

main_game = MAIN()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    screen.fill(screen_color)
    
    main_game.draw_elements()
            
    pygame.display.update()
    clock.tick(60)