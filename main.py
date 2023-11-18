import random
import sys
import time
import pygame
from pygame.math import Vector2


class FRUIT:
    def __init__(self):
        self.color = (42, 77, 182)
        self.x = random.randint(0, cell_col_number - 1)
        self.y = random.randint(0, cell_row_number - 1)
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.x * cell_size, self.y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, self.color, fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_col_number - 1)
        self.y = random.randint(0, cell_row_number - 1)
        self.pos = Vector2(self.x, self.y)


class SNAKE:
    def __init__(self):
        self.isMoving = False
        self.enlarge = False
        self.color = (155, 35, 57)
        self.body = [Vector2(10, 9), Vector2(9, 9), Vector2(8, 9)]
        self.direction = Vector2(0, 0)

    def draw_snake(self):
        for block in self.body:
            block_rect = pygame.Rect((block.x * cell_size), (block.y * cell_size), cell_size, cell_size)
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
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.restore_booleans()
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

    def restore_booleans(self):
        self.new_session = True
        self.lvl1_bool = True
        self.lvl2_bool = True
        self.lvl3_bool = True
        self.lvl4_bool = True

    def draw_elements(self):
        self.draw_grass()
        self.snake.draw_snake()
        self.fruit.draw_fruit()
        self.show_time_and_score()

    def check_collision(self):
        if self.snake.body[0] == self.fruit.pos:
            self.fruit.randomize()
            self.snake.add_block()

    def check_fail(self):
        if self.snake.body[0] in self.snake.body[1:]:
            self.game_over()

        if self.snake.body[0].x == -1 or self.snake.body[0].x == 30:
            self.game_over()

        if self.snake.body[0].y == -1 or self.snake.body[0].y == 15:
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
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for row in range(cell_row_number):
                    if row % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
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
        time_surface = game_font.render(time_text, True, (0, 0, 0))
        score_rect = time_surface.get_rect(topright=(screen_size[0] - 30, 30))
        screen.blit(time_surface, score_rect)

        score_text = f"SCORE: {self.score}"
        score_surface = game_font.render(score_text, True, (0, 0, 0))
        score_rect = score_surface.get_rect(topleft=(30, 30))
        screen.blit(score_surface, score_rect)

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

cell_size = 60
cell_col_number = 30
cell_row_number = 15
screen_size = (int(cell_col_number * cell_size), int(cell_row_number * cell_size))
screen_color = (35, 170, 72)

screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
game_font = pygame.font.Font(None, 72)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)


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
                    main_game.snake.direction = Vector2(0, -1)

            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)

            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)

            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)

    screen.fill(screen_color)

    main_game.update_40fps()

    pygame.display.update()
    clock.tick(40)
