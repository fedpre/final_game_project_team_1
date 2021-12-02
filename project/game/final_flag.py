import arcade
from game import constants

class FinalFlag(arcade.Sprite):
    def __init__(self):
        super().__init__(constants.SIGN_RX_IMAGE, constants.TILE_SCALING)
        self.center_x = 2450
        self.center_y = 95
    
