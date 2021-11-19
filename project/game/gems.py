import arcade

class Player(arcade.Sprite):

    def __init__(self, path, scale):
        super().__init__(path, scale) 