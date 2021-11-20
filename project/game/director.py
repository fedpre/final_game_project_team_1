import arcade
from game.player import Player
from game import constants
from game.coins import Coins
from game.gems import Gems
from game.follow_camera import Follow_camera


class TeamGame(arcade.Window):
    """ This will be the main application class """
    
    def __init__(self):
        # call the parent class and setup a window
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)


        # Initialize the Sprites lists
        # These are list to keep track of sprites
        self.platform_list = None
        self.player_list = None
        self.coin_list = None
        self.gem_list = None
        self.camera = None

        # Create player Sprite
        self.player_sprite = None

        # Create the physics engine
        self.physics_engine = None

        # Create the sounds
        self.background_sound = arcade.load_sound(constants.BACKGROUND_MUSIC_PATH)
        self.jump_sound = arcade.load_sound(":resources:sounds/phaseJump1.wav")
        self.collect_coin_sound = arcade.load_sound(":resources:sounds/coin1.wav")
        self.collect_gem_sound = arcade.load_sound(":resources:sounds/coin1.wav")
        

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
        arcade.play_sound(self.background_sound, 0.1)

    def setup(self): # this looks like it should be separated out into a class

        #setup camera
        self.camera = Follow_camera(self.width, self.height)
        # this is where we'll start the game?
        self.player_list = arcade.SpriteList()
        self.platform_list = arcade.SpriteList(use_spatial_hash=True)

        # setup the player at specific coordinates
        image_source = ":resources:images/animated_characters/female_person/femalePerson_idle.png"
        self.player_sprite = Player(image_source, constants.CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.player_list.append(self.player_sprite)

        # create the ground
        # this places multiple sprites horizontally
        for x in range(0, constants.SCREEN_WIDTH, 60):
            platform = arcade.Sprite(":resources:images/tiles/stoneMid.png", constants.TILE_SCALING)
            platform.center_x = x
            platform.center_y = 32
            self.platform_list.append(platform)

        # Put some crates on the ground
        # This shows using a coordinate list to place sprites
        coordinate_list = [[256, 96], [384, 275], [512, 96], [640, 275], [768, 96]]

        for coordinate in coordinate_list:
            # Add a crate on the ground
            platform = arcade.Sprite(
                ":resources:images/tiles/boxCrate_double.png", constants.TILE_SCALING
            )
            platform.position = coordinate
            self.platform_list.append(platform)
        
        # Create some coins
        coordinate_list_coins = [[256, 150], [512, 150]]
        self.coin_list = arcade.SpriteList()

        for position in coordinate_list_coins:
            coin = Coins(":resources:images/items/gold_1.png", constants.TILE_SCALING)
            coin.position = position
            self.coin_list.append(coin)

        # Create some gems
        coordinate_list_gems = [[384, 325], [640, 325]]
        self.gem_list = arcade.SpriteList()

        for position in coordinate_list_gems:
            gem = Gems(":resources:images/items/gemGreen.png", constants.TILE_SCALING)
            gem.position = position
            self.gem_list.append(gem)

        # Create the 'physics engine'
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, gravity_constant=constants.GRAVITY, walls=self.platform_list
        )

    def on_draw(self):
        arcade.start_render()

        self.camera.use()
        # code for drawing the screen will be placed here
        self.player_list.draw()
        self.platform_list.draw()
        self.coin_list.draw()
        self.gem_list.draw()


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = constants.PLAYER_JUMP_SPEED
                arcade.play_sound(self.jump_sound)
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = -constants.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -constants.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = constants.PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    
        
    def on_update(self, delta_time):
        """Movement and game logic"""

        # Move the player with the physics engine
        self.physics_engine.update()

        self.camera.center_camera_to_player(self.player_sprite)
        # See if we hit any coins
        coin_hit_list = arcade.check_for_collision_with_list(
            self.player_sprite, self.coin_list
        )
        gem_hit_list = arcade.check_for_collision_with_list(
            self.player_sprite, self.gem_list

        )

        # Loop through each coin we hit (if any) and remove it
        for coin in coin_hit_list:
            # Remove the coin
            coin.remove_from_sprite_lists()
            # Play a sound
            arcade.play_sound(self.collect_coin_sound)
        for gem in gem_hit_list:
                # Remove the coin
            gem.remove_from_sprite_lists()
            # Play a sound
            arcade.play_sound(self.collect_gem_sound)
        


    
