import random
import sys
import time
import pygame
from pygame.math import Vector2


class FRUIT:
    def __init__(self, width , height):
        self.color = (42, 77, 182)
        self.x = random.randint(0, cell_col_number - 1)
        self.y = random.randint(0, cell_row_number - 1)
        self.pos = Vector2(self.x, self.y)
        self.width = width
        self.height = height

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.x * self.width,
                                 self.y * self.height,
                                 self.width, self.height)
        pygame.draw.rect(screen, self.color, fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_col_number - 1)
        self.y = random.randint(0, cell_row_number - 1)
        self.pos = Vector2(self.x, self.y)


class SNAKE:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.isMoving = False
        self.enlarge = False
        self.color = (155, 35, 57)
        self.body = [Vector2(10, 9), Vector2(9, 9), Vector2(8, 9)]
        self.direction = Vector2(0, 0)

    def draw_snake(self):
        for block in self.body:
            block_rect = pygame.Rect(block.x * self.width,
                                     block.y * self.height,
                                     self.width, self.height)
            pygame.draw.rect(screen, self.color, block_rect)

    def move_snake(self):
        if self.direction != Vector2(0, 0):
            self.isMoving = True
            if self.enlarge:
                body_copy = self.body
                body_copy.insert(0, body_copy[0] + self.direction)
                self.body = body_copy
                self.enlarge = False
            else:
                body_copy = self.body[:-1]
                body_copy.insert(0, body_copy[0] + self.direction)
                self.body = body_copy
        else:
            self.isMoving = False

    def add_block(self):
        self.enlarge = True


class MAIN:
    def __init__(self):
        self.width = screen.get_width() / cell_col_number
        self.height = screen.get_height() / cell_row_number
        self.snake = SNAKE(self.width, self.height)
        self.fruit = FRUIT(self.width, self.height)
        self.restore_booleans()
        self.load_fonts()
        self.score = 0
        self.start_time = 0
        self.current_time = 0

    def update(self):
        self.score = int(len(self.snake.body) - 3)
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def update_40fps(self):
        self.draw_elements()
        self.timer()
        self.set_game_level()
        
    def resize(self):
        self.width = screen.get_width() / cell_col_number
        self.height = screen.get_height() / cell_row_number
        self.snake.width = self.width
        self.snake.height = self.height
        self.fruit.width = self.width
        self.fruit.height = self.height
        self.load_fonts()

    def draw_elements(self):
        self.draw_grass()
        self.snake.draw_snake()
        self.fruit.draw_fruit()
        self.show_time_and_score()
        
    def restore_booleans(self):
        self.new_session = True
        self.lvl1_bool = True
        self.lvl2_bool = True
        self.lvl3_bool = True
        self.lvl4_bool = True

    def check_collision(self):
        if self.snake.body[0] == self.fruit.pos:
            self.fruit.randomize()
            self.snake.add_block()

    def check_fail(self):
        if self.snake.body[0] in self.snake.body[1:]:
            self.game_over()

        if self.snake.body[0].x == -1 or self.snake.body[0].x == cell_col_number:
            self.game_over()

        if self.snake.body[0].y == -1 or self.snake.body[0].y == cell_row_number:
            self.game_over()

    def game_over(self):
        self.snake.body = [Vector2(10, 9), Vector2(9, 9), Vector2(8, 9)]
        self.snake.direction = Vector2(0, 0)
        self.fruit.randomize()
        self.restore_booleans()
        pygame.time.set_timer(SCREEN_UPDATE, 150)

    def draw_grass(self):
        grass_color = (15, 150, 52)
        for col in range(cell_col_number):
            if col % 2 == 0:
                for row in range(cell_row_number):
                    if row % 2 == 0:
                        grass_rect = pygame.Rect(
                            col * self.width,
                            row * self.height,
                            self.width, self.height)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for row in range(cell_row_number):
                    if row % 2 != 0:
                        grass_rect = pygame.Rect(
                            col * self.width,
                            row * self.height,
                            self.width, self.height)
                        pygame.draw.rect(screen, grass_color, grass_rect)

    def timer(self):
        if self.snake.isMoving:
            if self.new_session:
                self.start_time = int(time.time())
                self.new_session = False
            self.current_time = int(time.time()) - self.start_time
        else:
            self.current_time = 0

    def show_time_and_score(self):
        time_text = f"TIME: {self.current_time}"
        time_surface = self.time_font.render(time_text, True, (74, 35, 90))
        time_x = int(self.width // 2.4)
        time_y = int(self.height * 2)
        time_rect = time_surface.get_rect(topleft=(time_x,time_y))
        screen.blit(time_surface, time_rect)

        score_text = f"SCORE: {self.score}"
        score_surface = self.score_font.render(score_text, True, (74, 35, 90))
        score_y = int(self.height // 4)
        score_rect = score_surface.get_rect(topleft=(time_x,-score_y))
        screen.blit(score_surface, score_rect)
        
    def load_fonts(self):
        time_size = int(((self.width + self.height) / 2) * 1.25)
        score_size = int(self.width + self.height)
        self.time_font = pygame.font.Font("./data/fonts/vademecum.otf" , time_size)
        self.score_font = pygame.font.Font("./data/fonts/burnstown dam.otf" , score_size)

    def set_game_level(self):
        if self.lvl1_bool and (self.current_time >= 15):
            pygame.time.set_timer(SCREEN_UPDATE, 120)
            self.lvl1_bool = False

        if self.lvl2_bool and (self.current_time >= 30):
            pygame.time.set_timer(SCREEN_UPDATE, 100)
            self.lvl2_bool = False

        if self.lvl3_bool and (self.current_time >= 45):
            pygame.time.set_timer(SCREEN_UPDATE, 80)
            self.lvl3_bool = False

        if self.lvl4_bool and (self.current_time >= 60):
            pygame.time.set_timer(SCREEN_UPDATE, 60)
            self.lvl4_bool = False


pygame.init()

cell_initial_size = 40
cell_col_number = 32
cell_row_number = 18
screen_inital_size = (int(cell_col_number * cell_initial_size), int(cell_row_number * cell_initial_size))
screen_color = (35, 170, 72)

screen = pygame.display.set_mode(screen_inital_size, pygame.RESIZABLE)
clock = pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)


main_game = MAIN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.VIDEORESIZE:
            main_game.resize()

        if event.type == SCREEN_UPDATE:
            main_game.update()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)

            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)

            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1 and main_game.snake.isMoving:
                    main_game.snake.direction = Vector2(-1, 0)

            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)

    screen.fill(screen_color)

    main_game.update_40fps()

    pygame.display.update()
    clock.tick(40)
