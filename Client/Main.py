import pygame as pg
import requests

from Game import Game
from Menu import Menu
from RESTClient import RESTClient

# Default color definitions
colors = {"black": (0, 0, 0), "white": (255, 255, 255)}

color_schemes = {
        0:
            {
                "name": "default",
                "snake_color": (0, 255, 0),
                "apple_color": (255, 0, 0),
                "walls_color": (50, 50, 200),
                "background_color": (0, 0, 0)
            },
    }

def main():
    online = False
    rest_client = RESTClient(address="http://localhost:8000")
    colors_data = []
    scores_data = []
    if rest_client.check_connection():
        colors_data = rest_client.get_color_schemes()
        scores_data = rest_client.get_high_scores()
        online = True

    pg.init()
    pg.display.set_caption("PySnake")
    display_resolution = width, height = 800, 600
    screen = pg.display.set_mode(display_resolution)
    clock = pg.time.Clock()
    fps = 15
    block_size = 20


    if colors_data:
        for enum, element in enumerate(colors_data, 1):
            color_schemes[enum] = {
                "name": element["name"],
                "snake_color": (element["snake_R"], element["snake_G"], element["snake_B"]),
                "apple_color": (element["apple_R"], element["apple_G"], element["apple_B"]),
                "walls_color": (element["walls_R"], element["walls_G"], element["walls_B"]),
                "background_color": (element["background_R"], element["background_G"], element["background_B"]),
            }
    game = Game(display_resolution, screen, fps, clock, block_size, colors, color_schemes, online)
    menu = Menu(game)
    menu.main_menu()


if __name__ == "__main__":
    main()