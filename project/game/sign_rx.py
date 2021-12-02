import arcade
from game import constants

class SignRx(arcade.Sprite):
    def __init__(self):
        super().__init__(constants.SIGN_RX_IMAGE, constants.TILE_SCALING)
        self.center_x = 120
        self.center_y = 95
