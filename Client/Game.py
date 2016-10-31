import pygame as pg
import sys

import external.eztext

from Apple import Apple
from Directions import Directions
from Menu import Menu
from RESTClient import RESTClient
from Snake import Snake


class Game(object):
    """
    Game class is responsible for Game Logic and Drawing game elements on screen
    """

    def __init__(self, display_resolution, screen, fps, clock, block_size, colors, color_schemes, online):
        self.display_resolution = display_resolution
        self.screen = screen
        self.fps = fps
        self.clock = clock
        self.block_size = block_size
        self.online = online
        self.black = colors["black"]
        self.white = colors["white"]
        self.snake_color = color_schemes[0]["snake_color"]
        self.walls_color = color_schemes[0]["walls_color"]
        self.apple_color = color_schemes[0]["apple_color"]
        self.background_color = color_schemes[0]["background_color"]
        self.color_schemes = color_schemes
        self.score = 0
        self.current_color_scheme = 0

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
                if event.type == pg.K_ESCAPE:
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

            # Filling background with color (default white)
            self.screen.fill(self.white)
            self.show_score(self.screen, self.score)
            self.screen.fill(self.background_color, (20, 20, self.display_resolution[0], self.display_resolution[1]))

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
        game_over_font = pg.font.SysFont(None, 100)
        font = pg.font.SysFont(None, 64)
        prompt_font = pg.font.SysFont(None, 40)

        game_over_text = game_over_font.render("GAME OVER", 1, (255, 0, 0))
        game_over_width = game_over_text.get_width()

        self.screen.fill(self.black)
        txt_box = None
        if self.online:
            self.screen.fill(self.black)
            prompt_text = prompt_font.render("Enter your name...", 1, (255, 0, 0), self.black)
            prompt_width = prompt_text.get_width()
            name_saved = False
            txt_box = external.eztext.Input(x=self.display_resolution[0]/2 - 250, y=370, maxlength=22,
                                            color=(255, 0, 0), prompt='')
            while not name_saved:
                self.screen.fill(self.black)
                pg.draw.rect(self.screen, (255, 0, 0), (100, 250, 600, 180), 2)
                pg.draw.rect(self.screen, (100, 100, 100), (130, 360, 530, 40))
                self.screen.blit(game_over_text,
                                 (self.display_resolution[0] / 2 - game_over_width / 2,
                                  100))
                self.screen.blit(prompt_text, (self.display_resolution[0]/2 - prompt_width/2, self.display_resolution[1]/2))
                events = pg.event.get()

                for event in events:
                    if event.type == pg.QUIT:
                        sys.exit()
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_RETURN:
                            rest_client = RESTClient("http://localhost", 8000)
                            name = txt_box.value
                            if name == "":
                                name = "unknown_knight"
                            rest_client.add_high_score(name, self.score)
                            name_saved = True

                txt_box.update(events)
                txt_box.draw(self.screen)
                self.clock.tick(self.fps)
                pg.time.wait(0)
                pg.display.update()

        score_text = font.render("YOUR SCORE: " + str(self.score), 1, (255, 0, 0))
        score_width = score_text.get_width()

        play_again_text = font.render("PLAY AGAIN?", 1, (255, 0, 0))
        play_again_width = play_again_text.get_width()

        yes_no_text = font.render("YES    NO", 1, (255,0 ,0 ))

        play_again = True

        while True:
            self.screen.fill(self.black)
            if play_again:
                pg.draw.rect(self.screen, (255, 0, 0), (295, 445, 100, 50), 2)
            else:
                pg.draw.rect(self.screen, (255, 0, 0), (418, 445, 100, 50), 2)
            self.screen.blit(game_over_text,
                             (self.display_resolution[0] / 2 - game_over_width / 2,
                              100))
            self.screen.blit(score_text,
                             (self.display_resolution[0] / 2 - score_width / 2,
                              200))
            self.screen.blit(play_again_text,
                             (self.display_resolution[0] / 2 - play_again_width / 2,
                              self.display_resolution[1] - 250))
            self.screen.blit(yes_no_text,
                             (300, 450))

            pg.display.update()
            self.clock.tick(self.fps)
            pg.time.wait(0)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    game_exit = True
                    sys.exit()
                if event.type == pg.K_ESCAPE:
                    pg.quit()
                    game_exit = True
                    sys.exit()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        play_again = True
                        pg.display.update()
                    if event.key == pg.K_RIGHT:
                        play_again = False
                        pg.display.update()
                    if event.key == pg.K_RETURN:
                        if play_again:
                            self.game_loop()
                        else:
                            menu = Menu(self)
                            menu.main_menu()