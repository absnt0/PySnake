import sys

from Coords import Coords
from Directions import Directions


class Snake(object):
    """
    Snake class creates player object
    """

    def __init__(self, display_resolution, block_size):
        self.screen_width = display_resolution[0]
        self.screen_height = display_resolution[1]
        self.block_size = block_size
        self.head = Coords(self.screen_width/2, self.screen_height/2)
        self.tail_coords = [
            Coords(self.head.x - self.block_size, self.head.y),
            Coords(self.head.x - self.block_size * 2, self.head.y),
            Coords(self.head.x - self.block_size * 3, self.head.y),
            Coords(self.head.x - self.block_size * 4, self.head.y)
        ]
        self.move_x = self.block_size
        self.move_y = 0
        self.current_direction = Directions.RIGHT

    def update(self, game):
        if self.check_collision():
            game.game_over()

        self.tail_follow()
        self.head.x += self.move_x
        self.head.y += self.move_y

    def tail_follow(self):
        for i in range(len(self.tail_coords) - 1, 0, -1):
            self.tail_coords[i].x = self.tail_coords[i - 1].x
            self.tail_coords[i].y = self.tail_coords[i - 1].y
        self.tail_coords[0].x = self.head.x
        self.tail_coords[0].y = self.head.y

    def tail_extend(self):
        last_tail_element = len(self.tail_coords) - 1

        self.tail_coords.append(
            Coords(self.tail_coords[last_tail_element].x, self.tail_coords[last_tail_element].y)
        )

    def check_collision(self):
        if self.head.x <= self.block_size-20 or \
                        self.head.x >= self.screen_width - self.block_size or \
                        self.head.y <= self.block_size or \
                        self.head.y >= self.screen_height - self.block_size:
            return True

        for element in self.tail_coords:
            if self.head.x == element.x and self.head.y == element.y:
                return True
        return False

    def check_tail(self, x, y):
        for element in self.tail_coords:
            if element.x == x and element.y == y:
                return True
        return False

    def move_left(self):
        if self.current_direction != Directions.RIGHT:
            self.current_direction = Directions.LEFT
            self.move_x = -self.block_size
            self.move_y = 0

    def move_right(self):
        if self.current_direction != Directions.LEFT:
            self.current_direction = Directions.RIGHT
            self.move_x = self.block_size
            self.move_y = 0

    def move_up(self):
        if self.current_direction != Directions.DOWN:
            self.current_direction = Directions.UP
            self.move_y = -self.block_size
            self.move_x = 0

    def move_down(self):
        if self.current_direction != Directions.UP:
            self.current_direction = Directions.DOWN
            self.move_y = self.block_size
            self.move_x = 0

