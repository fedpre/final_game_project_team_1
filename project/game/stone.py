import arcade
from game import constants

class Stone(arcade.Sprite):
    def __init__(self, x):
        super().__init__(constants.GROUND_IMAGE, constants.TILE_SCALING)
        self.center_x = x
        self.center_y = 32