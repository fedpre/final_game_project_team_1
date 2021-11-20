import arcade
from game.player import Player
from game import constants
from game.coins import Coins
from game.gems import Gems

class Follow_camera(arcade.Camera):
    def __init__(self, width, height):
        super().__init__(width, height)

    def center_camera_to_player(self, player):
        screen_center_x = player.center_x - (self.viewport_width / 2)
        screen_center_y = player.center_y - (
            self.viewport_height / 2
        )

        # Don't let camera travel past 0
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = screen_center_x, screen_center_y

        self.move_to(player_centered)
        