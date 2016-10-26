import pygame as pg
import sys
import time

from Apple import Apple
from Directions import Directions
from Snake import Snake


class Game(object):
    """
    Game class is responsible for Game Logic and Drawing game elements on screen
    """

    def __init__(self, display_resolution, screen, fps, clock, block_size, colors, online):
        self.display_resolution = display_resolution
        self.screen = screen
        self.fps = fps
        self.clock = clock
        self.block_size = block_size
        self.online = online
        self.black = colors["black"]
        self.white = colors["white"]
        self.snake_color = colors["snake_color"]
        self.walls_color = colors["walls_color"]
        self.apple_color = colors["apple_color"]
        self.score = 0

    def game_loop(self):
        # Creating game objects
        snake = Snake(self.display_resolution, self.block_size)
        apple = Apple(self.display_resolution, self.block_size)
        snake.current_direction = Directions.RIGHT
        apple.generate(snake)
        self.score = 0

        game_exit = False

        while not game_exit:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    game_exit = True
                    sys.exit()
                elif event.type == pg.K_ESCAPE:
                    pg.quit()
                    game_exit = True
                    sys.exit()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        snake.move_left()
                    if event.key == pg.K_RIGHT:
                        snake.move_right()
                    if event.key == pg.K_UP:
                        snake.move_up()
                    if event.key == pg.K_DOWN:
                        snake.move_down()

            snake.update(self)

            if snake.head.x == apple.coords.x and snake.head.y == apple.coords.y:
                snake.tail_extend()
                self.score += 1
                apple.generate(snake)
                print(self.score)

            # Filling background with color (default white)
            self.screen.fill(self.white)
            self.show_score(self.screen, self.score)
            self.screen.fill(self.black, (20, 20, self.display_resolution[0], self.display_resolution[1]))

            # Drawing snakes head
            pg.draw.rect(self.screen,
                         self.snake_color,
                         (snake.head.x, snake.head.y, self.block_size, self.block_size))

            # Drawing snakes tail
            for elem in snake.tail_coords:
                pg.draw.rect(self.screen,
                             self.snake_color,
                             (elem.x, elem.y, self.block_size, self.block_size))

            # Drawing walls
            # Upper wall
            pg.draw.rect(self.screen,
                         self.walls_color,
                         (0, 20, self.display_resolution[0], 20))
            # Left wall
            pg.draw.rect(self.screen,
                         self.walls_color,
                         (0, 20, 20, self.display_resolution[1]))
            # Bottom wall
            pg.draw.rect(self.screen,
                         self.walls_color,
                         (0, self.display_resolution[1] - 20, self.display_resolution[0], 20))
            # Right wall
            pg.draw.rect(self.screen,
                         self.walls_color,
                         (self.display_resolution[0] - 20, 20, 20, self.display_resolution[1]))

            # Drawing apple
            pg.draw.rect(self.screen,
                         self.apple_color,
                         (apple.coords.x, apple.coords.y, self.block_size, self.block_size))

            pg.display.update()
            self.clock.tick(self.fps)

    def show_score(self, screen, score):
        font = pg.font.Font(None, 36)
        text = font.render("SCORE: " + str(score), 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = screen.get_rect().centerx
        screen.blit(text, textpos)

    def game_over(self):
        if self.online:
            pass
        else:
            font = pg.font.SysFont(None, 72)

            game_over_text = font.render("GAME OVER", 1, (255, 0, 0))
            game_over_width = game_over_text.get_width()
            game_over_height = game_over_text.get_height()

            score_text = font.render("YOUR SCORE: " + str(self.score), 1, (255, 0, 0))
            score_width = score_text.get_width()
            score_height = score_text.get_height()

            self.screen.blit(game_over_text,
                             (self.display_resolution[0]/2 - game_over_width/2,
                              self.display_resolution[1]/2 - game_over_height/2))
            self.screen.blit(score_text,
                             (self.display_resolution[0]/2 - score_width/2,
                              self.display_resolution[1]/2 - score_height/2 + game_over_height + 20))
            pg.display.update()
            time.sleep(2)
            self.game_loop()

