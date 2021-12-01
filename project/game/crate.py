import arcade
from game import constants

class Crate(arcade.Sprite):
    def __init__(self):
        super().__init__(constants.CRATE_IMAGE, constants.TILE_SCALING)
