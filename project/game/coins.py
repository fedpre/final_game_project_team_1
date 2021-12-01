import arcade

from game import constants

class Coins(arcade.Sprite):

    def __init__(self):
        super().__init__(constants.COINS_IMAGE, constants.TILE_SCALING) 
        self._value = 1

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value