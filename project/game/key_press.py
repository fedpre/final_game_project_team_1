import arcade
from game import constants

class UserMovement():      

    def movement(self, key, modifiers, player_sprite, physics_engine, jump_sound):
        """Called whenever a key is pressed."""

        if key == arcade.key.UP or key == arcade.key.SPACE or key == arcade.key.W:
            if physics_engine.can_jump():
                player_sprite.change_y = constants.PLAYER_JUMP_SPEED
                arcade.play_sound(jump_sound)
        elif key == arcade.key.DOWN or key == arcade.key.S:
            player_sprite.change_y = -constants.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            player_sprite.change_x = -constants.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            player_sprite.change_x = constants.PLAYER_MOVEMENT_SPEED

    def movement_stop(self, key, modifiers, player_sprite):
        """Called when the user releases a key."""
        if key == arcade.key.LEFT or key == arcade.key.A:
            player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            player_sprite.change_x = 0

