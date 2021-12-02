import arcade
from game import constants

class SmallPlatforms(arcade.Sprite):
    def __init__(self):
        super().__init__(constants.SMALL_PLATFORMS_IMAGE, constants.TILE_SCALING)