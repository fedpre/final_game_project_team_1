import arcade
from game.player import Player
from game import constants

class TeamGame(arcade.Window):
    """ This will be the main application class """
    
    def __init__(self):
        # call the parent class and setup a window
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)


        # Initialize the Sprites lists
        # These are list to keep track of sprites
        self.platform_list = None
        self.player_list = None

        # Create player Sprite
        self.player_sprite = None


        # Create the physics engine
        self.physics_engine = None
        
        arcade.set_background_color(arcade.csscolor.AQUAMARINE)

    def setup(self): # this looks like it should be separated out into a class

        # this is where we'll start the game?
        self.player_list = arcade.SpriteList()
        self.platform_list = arcade.SpriteList(use_spatial_hash=True)

        # setup the player at specific coordinates
        image_source = ":resources:images/animated_characters/zombie/zombie_idle.png"
        self.player_sprite = Player(image_source, constants.CHARACTER_SCALING)
        self.player_sprite.center_x = 60
        self.player_sprite.center_y = 120
        self.player_list.append(self.player_sprite)

        # create the ground
        # this places multiple sprites horizontally
        for x in range(0, constants.SCREEN_WIDTH, 60):
            platform = arcade.Sprite(":resources:images/tiles/stoneMid.png", constants.TILE_SCALING)
            platform.center_x = x
            platform.center_y = 20
            self.platform_list.append(platform)

        # Put some crates on the ground
        # This shows using a coordinate list to place sprites
        coordinate_list = [[512, 96], [256, 96], [768, 96]]

        for coordinate in coordinate_list:
            # Add a crate on the ground
            platform = arcade.Sprite(
                ":resources:images/tiles/boxCrate_double.png", constants.TILE_SCALING
            )
            platform.position = coordinate
            self.platform_list.append(platform)
        
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.platform_list)

    def on_draw(self):
        arcade.start_render()

        # code for drawing the screen will be placed here
        self.player_list.draw()
        self.platform_list.draw()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = constants.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = -constants.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -constants.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = constants.PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""

        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0
        
    def on_update(self, delta_time):
        """Movement and game logic"""

        # Move the player with the physics engine
        self.physics_engine.update()
    
