import arcade
from game import constants

class Player(arcade.Sprite):

    def __init__(self):
        super().__init__(constants.IMAGE_PLAYER, constants.CHARACTER_SCALING) 
        self._center_x = 64
        self._center_y = 128
    
    def get_x(self):
        return self._center_x

    def get_y(self):
        return self._center_y
    

        

