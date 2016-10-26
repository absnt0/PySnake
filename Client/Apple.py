from random import randrange
from Coords import Coords

class Apple(object):
    """
    Apple class is responsible for ... apples
    """

    def __init__(self, display_resolution, block_size):
        self.screen_width = display_resolution[0]
        self.screen_height = display_resolution[1]
        self.block_size = block_size
        self.coords = Coords()


    def generate(self, snake):
        generated = False

        while not generated:
            random_x = randrange(20, self.screen_width - self.block_size - 20, 20)
            random_y = randrange(40, self.screen_height - self.block_size - 20, 20)
            if (random_x != snake.head.x and random_y != snake.head.y) and not (snake.check_tail(random_x, random_y)):
                generated = True
                self.coords.x = random_x
                self.coords.y = random_y





