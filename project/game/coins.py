import arcade

class Coins(arcade.Sprite):

    def __init__(self, texture, scale):
        super().__init__(texture, scale) 
        self._value = 1

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value