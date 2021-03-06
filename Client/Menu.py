import pygame as pg
import sys
from RESTClient import RESTClient

class Menu(object):
    """
    This class is responsible for game menu
    """

    def __init__(self, game):
        self.game = game

    def main_menu(self):
        game_title_font = pg.font.SysFont(None, 100)
        menu_options_font = pg.font.SysFont(None, 64)
        connection_font = pg.font.SysFont(None, 32)
        game_title_txt = game_title_font.render("PySnake", 1, (0, 255, 0))
        play_option_txt = menu_options_font.render("Play", 1, self.game.black)
        options_option_txt = menu_options_font.render("Options", 1, self.game.black)
        highscores_option_txt = menu_options_font.render("Highscores", 1, self.game.black)
        quit_option_txt = menu_options_font.render("Quit", 1, self.game.black)
        online_txt = connection_font.render("Online mode", 1, self.game.black)
        offline_txt = connection_font.render("Offline mode", 1, self.game.black)

        game_title_width = game_title_txt.get_width()
        play_option_width = play_option_txt.get_width()
        options_option_width = options_option_txt.get_width()
        highscores_option_width = highscores_option_txt.get_width()
        quit_option_width = quit_option_txt.get_width()
        online_width = online_txt.get_width()
        online_height = online_txt.get_height()
        offline_width = offline_txt.get_width()
        offline_height = offline_txt.get_height()

        menu_options = {0: "Play", 1: "Options", 2: "Highscores", 3: "Quit"}
        current_option = 0

        while True:
            self.game.screen.fill(self.game.white)
            if current_option == 0:
                pg.draw.rect(self.game.screen, (255, 0, 0), (340, 190, 120, 65), 2)
            elif current_option == 1:
                pg.draw.rect(self.game.screen, (255, 0, 0), (300, 260, 200, 65), 2)
            elif current_option == 2:
                pg.draw.rect(self.game.screen, (255, 0, 0), (265, 330, 270, 65), 2)
            elif current_option == 3:
                pg.draw.rect(self.game.screen, (255, 0, 0), (340, 400, 120, 65), 2)

            self.game.screen.blit(game_title_txt,
                                  (self.game.display_resolution[0] / 2 - game_title_width / 2,
                                   50))
            self.game.screen.blit(play_option_txt,
                                  (self.game.display_resolution[0] / 2 - play_option_width / 2,
                                   200))
            self.game.screen.blit(options_option_txt,
                                  (self.game.display_resolution[0]/2 - options_option_width/2,
                                   270))
            self.game.screen.blit(highscores_option_txt,
                                  (self.game.display_resolution[0]/2 - highscores_option_width/2,
                                  340))
            self.game.screen.blit(quit_option_txt,
                                  (self.game.display_resolution[0]/2 - quit_option_width/2,
                                   410))

            if self.game.online:
                self.game.screen.blit(online_txt,
                                      (self.game.display_resolution[0] - online_width,
                                       self.game.display_resolution[1] - online_height))
            else:
                self.game.screen.blit(offline_txt,
                                      (self.game.display_resolution[0] - offline_width,
                                       self.game.display_resolution[1] - offline_height))

            pg.display.update()
            self.game.clock.tick(self.game.fps)
            pg.time.wait(0)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
                if event.type == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        if current_option - 1 < 0:
                            current_option = 3
                        else:
                            current_option -= 1
                        pg.display.update()
                    if event.key == pg.K_DOWN:
                        if current_option + 1 > 3:
                            current_option = 0
                        else:
                            current_option += 1
                        pg.display.update()
                    if event.key == pg.K_RETURN:
                       if current_option == 0:
                           self.game.game_loop()
                       if current_option == 1:
                           self.options_menu()
                       if current_option == 2:
                           self.high_scores_menu()
                       if current_option == 3:
                           sys.exit()

    def options_menu(self):
        color_schemes = self.game.color_schemes

        game_title_font = pg.font.SysFont(None, 100)
        option_font = pg.font.SysFont(None, 48)
        color_scheme_font = pg.font.SysFont(None, 64)

        game_title_txt = game_title_font.render("PySnake", 1, (0, 255, 0))
        option_color_scheme_txt = option_font.render("Color Scheme", 1, self.game.black)
        option_back_txt = option_font.render("Back", 1, self.game.black)

        game_title_width = game_title_txt.get_width()
        option_color_scheme_width = option_color_scheme_txt.get_width()
        option_back_width = option_back_txt.get_width()

        current_option = 0

        while True:
            current_color_scheme_txt = color_scheme_font.render(color_schemes[self.game.current_color_scheme]["name"],
                                                                1, (100, 100, 255))
            current_color_scheme_width = current_color_scheme_txt.get_width()
            self.game.screen.fill(self.game.white)

            if current_option == 0:
                pg.draw.rect(self.game.screen, (255, 0, 0), (40, 180, 720, 280), 2)
                pg.draw.lines(self.game.screen, (255, 0, 0), 0, [[30,300],[5,320],[30,340]], 2)
                pg.draw.lines(self.game.screen, (255, 0, 0), 0, [[770, 340], [795, 320], [770, 300]], 2)
            elif current_option == 1:
                pg.draw.rect(self.game.screen, (255, 0, 0), (325, 485, 150, 65), 2)


            self.game.screen.blit(game_title_txt,
                                  (self.game.display_resolution[0] / 2 - game_title_width / 2,
                                   50))
            self.game.screen.blit(option_color_scheme_txt,
                                  (self.game.display_resolution[0] / 2 - option_color_scheme_width / 2,
                                   200))
            self.game.screen.blit(current_color_scheme_txt,
                                  (self.game.display_resolution[0] / 2 - current_color_scheme_width / 2,
                                   300))
            self.game.screen.blit(option_back_txt,
                                  (self.game.display_resolution[0] / 2 - option_back_width / 2,
                                   500))

            pg.display.update()
            self.game.clock.tick(self.game.fps)
            pg.time.wait(0)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
                if event.type == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        if current_option - 1 < 0:
                            current_option = 1
                        else:
                            current_option -= 1
                        pg.display.update()
                    if event.key == pg.K_DOWN:
                        if current_option + 1 > 1:
                            current_option = 0
                        else:
                            current_option += 1
                        pg.display.update()
                    if event.key == pg.K_LEFT:
                        if current_option == 0:
                            if self.game.current_color_scheme + 1 > len(color_schemes)-1:
                                self.game.current_color_scheme = 0
                            else:
                                self.game.current_color_scheme += 1
                    if event.key == pg.K_RIGHT:
                        if current_option == 0:
                            if self.game.current_color_scheme - 1 < 0:
                                self.game.current_color_scheme = len(color_schemes) - 1
                            else:
                                self.game.current_color_scheme -= 1
                    if event.key == pg.K_RETURN:
                       if current_option == 1:
                           # Changing color scheme and returning back to main menu
                           self.game.snake_color = color_schemes[self.game.current_color_scheme]["snake_color"]
                           self.game.apple_color = color_schemes[self.game.current_color_scheme]["apple_color"]
                           self.game.walls_color = color_schemes[self.game.current_color_scheme]["walls_color"]
                           self.game.background_color = color_schemes[self.game.current_color_scheme]["background_color"]
                           self.main_menu()

    def high_scores_menu(self):
        # Font definitions
        game_title_font = pg.font.SysFont(None, 100)
        score_font = pg.font.SysFont(None, 32)
        back_font = pg.font.SysFont(None, 64)

        # Rendering text with fonts (args: Text, Antyaliasing, Text Color)
        game_title_txt = game_title_font.render("PySnake", 1, (0, 255, 0))
        back_txt = back_font.render("Back", 1, self.game.black)
        offline_text = score_font.render("This option in unavailable in offline mode...", 1, self.game.black)
        no_scores_text = score_font.render("Nothing to show here...", 1, self.game.black)

        # Saving text width
        game_title_width = game_title_txt.get_width()
        back_width = back_txt.get_width()
        offline_width = offline_text.get_width()
        no_scores_width = no_scores_text.get_width()

        rest_client = RESTClient("http://localhost", 8000)
        if rest_client.check_connection() and self.game.online:
            scores = rest_client.get_high_scores()

        while True:
            self.game.screen.fill(self.game.white)

            self.game.screen.blit(game_title_txt,
                                  (self.game.display_resolution[0] / 2 - game_title_width / 2,
                                   50))

            if rest_client.check_connection() and self.game.online:
                if scores:
                    position = 0
                    for enum, score in enumerate(scores, 1):
                        position += 30
                        score_txt = score_font.render('{0}. {1} - {2}'.format(enum, score["score"], score["name"]),
                                                      1, self.game.black)
                        self.game.screen.blit(score_txt,
                                              (100, 150 + position))
                elif not scores:
                    self.game.screen.blit(no_scores_text,
                                          (self.game.display_resolution[0] / 2 - no_scores_width / 2,
                                           self.game.display_resolution[1] / 2))
                    self.game.screen.blit(back_txt,
                                          (self.game.display_resolution[0] / 2 - back_width / 2,
                                           self.game.display_resolution[1] - 100))
                    pg.draw.rect(self.game.screen, (255, 0, 0),
                                 (self.game.display_resolution[0] / 2 - back_width / 2 - 10, 490, 125, 60), 2)
                    pg.display.update()

            else:
                self.game.screen.blit(offline_text,
                                      (self.game.display_resolution[0]/2 - offline_width/2,
                                      self.game.display_resolution[1]/2))
            self.game.screen.blit(back_txt,
                                  (self.game.display_resolution[0]/2 - back_width/2,
                                   self.game.display_resolution[1] - 100))
            pg.draw.rect(self.game.screen, (255, 0, 0),
                         (self.game.display_resolution[0]/2 - back_width/2 - 10, 490, 125, 60), 2)
            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
                if event.type == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        self.main_menu()
            self.game.clock.tick(self.game.fps)
            pg.time.wait(0)

