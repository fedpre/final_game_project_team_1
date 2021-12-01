import arcade

from game import constants

class Gems(arcade.Sprite):

    def __init__(self):
        super().__init__(constants.GEMS_IMAGE, constants.TILE_SCALING) 
        self._value = 5

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value