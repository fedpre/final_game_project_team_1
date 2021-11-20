import arcade

class Gems(arcade.Sprite):

    def __init__(self, texture, scale):
        super().__init__(texture, scale) 
        self._value = 5

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value