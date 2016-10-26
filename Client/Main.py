import pygame as pg

from Game import Game

# Basic color definitions
colors = {"black": (0, 0, 0),
          "white": (255, 255, 255),
          "snake_color": (0, 255, 0),
          "apple_color": (255, 0, 0),
          "walls_color": (50, 50, 200)}

def main():
    pg.init()
    pg.display.set_caption("PySnake")
    display_resolution = width, height = 800, 600
    screen = pg.display.set_mode(display_resolution)
    clock = pg.time.Clock()
    fps = 15
    block_size = 20
    online = False

    game = Game(display_resolution, screen, fps, clock, block_size, colors, online)
    game.game_loop()

if __name__ == "__main__":
    main()