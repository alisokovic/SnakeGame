import pygame,sys,random
from pygame.math import Vector2


class FRUIT:
    def __init__(self):
        self.color = (12,24,186)
        self.randomize()
        
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.x*cell_size,self.y*cell_size,cell_size,cell_size)
        pygame.draw.rect(screen,self.color,fruit_rect)
        
    def randomize(self):
        self.x = random.randint(0,cell_number-1)
        self.y = random.randint(0,cell_number-1)
        self.pos = Vector2(self.x,self.y)
        
        

class SNAKE:
    def __init__(self):
        self.enlarge = False
        self.color = (192,22,14)
        self.body = [Vector2(7,10),Vector2(6,10),Vector2(5,10)]
        self.direction = Vector2(0,0)
        
    def draw_snake(self):
        for block in self.body:
            block_rect = pygame.Rect(block.x*cell_size,block.y*cell_size,cell_size,cell_size)
            pygame.draw.rect(screen,self.color,block_rect)
            
    def move_snake(self):
        if self.direction != Vector2(0,0):
            if self.enlarge:
                body_copy = self.body
                body_copy.insert(0,body_copy[0]+self.direction)
                self.body = body_copy
                self.enlarge = False
            else:
                body_copy = self.body[:-1]
                body_copy.insert(0,body_copy[0]+self.direction)
                self.body = body_copy
        
    def add_block(self):
        self.enlarge = True
            
            
            
class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
        
    def draw_elements(self):
        self.snake.draw_snake()
        self.fruit.draw_fruit()
        
    def check_collision(self):
        if self.snake.body[0] == self.fruit.pos:
            self.fruit.randomize()
            self.snake.add_block()
            
    def check_fail(self):
        if self.snake.body[0] in self.snake.body[1:]:
            self.game_over()
        
        for block in self.snake.body:
            if block.x == 20:
                self.game_over()
                
            if block.x == -1:
                self.game_over()
                
            if block.y == 20:
                self.game_over()
                
            if block.y == -1:
                self.game_over()
        
    def game_over(self):
        self.snake.body = [Vector2(7,10),Vector2(6,10),Vector2(5,10)]
        self.snake.direction = Vector2(0,0)




pygame.init()

cell_size = 40
cell_number = 20
screen_size = int(cell_number*cell_size)
screen_color = (21,192,23)

screen = pygame.display.set_mode((screen_size,screen_size))
screen_title = pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

main_game = MAIN()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == SCREEN_UPDATE:
            main_game.update()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0,-1)
                
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1)
                
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)
                
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0)
            
    screen.fill(screen_color)
    
    main_game.draw_elements()
            
    pygame.display.update()
    clock.tick(60)