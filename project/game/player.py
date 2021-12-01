import arcade
from game import constants

class Player(arcade.Sprite):

    def __init__(self):
        super().__init__(constants.IMAGE_PLAYER, constants.CHARACTER_SCALING) 
        self.center_x = 64
        self.center_y = 128
    

        

