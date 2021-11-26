import arcade
from game.player import Player
from game import constants
from game.coins import Coins
from game.gems import Gems
from game.follow_camera import Follow_camera
from game.key_press import UserMovement
from game.drawing import Drawing
from game.do_updates import DoUpdates
from game.score import Score


class TeamGame(arcade.Window):
    """ This will be the main application class """
    def __init__(self):
        # call the parent class and setup a window
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
        # Initialize the Sprites lists
        self.platform_list = None
        self.player_list = None
        self.coin_list = None
        self.gem_list = None
        self.camera = None
        self.gui_camera = None
        self.player_movement = None
        self.drawing = None
        self.do_updates = None
        # Create player Sprite
        self.player_sprite = None
        # Create the physics engine
        self.physics_engine = None
        # Create the variable to store the score
        self.score = None
        # Create the sounds
        self.background_sound = arcade.load_sound(constants.BACKGROUND_MUSIC_PATH)
        self.jump_sound = arcade.load_sound(":resources:sounds/phaseJump1.wav")
        self.collect_coin_sound = arcade.load_sound(":resources:sounds/coin1.wav")
        self.collect_gem_sound = arcade.load_sound(":resources:sounds/coin1.wav")
        # Set the background and play the sound
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
        arcade.play_sound(self.background_sound, 0.1)

    def setup(self): 
        # setup camera
        self.camera = Follow_camera(self.width, self.height)
        self.gui_camera = arcade.Camera(self.width, self.height)
        # this is where we'll start the game?
        self.player_list = arcade.SpriteList()
        self.platform_list = arcade.SpriteList(use_spatial_hash=True)
        # setup the player at specific coordinates
        image_source = ":resources:images/animated_characters/female_person/femalePerson_idle.png"
        self.player_sprite = Player(image_source, constants.CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.score = Score(0)
        self.player_list.append(self.player_sprite)
        # Create the ground
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
        # Create the movement checker
        self.player_movement = UserMovement()
        # Create the update object
        self.do_updates = DoUpdates(self.player_sprite, self.physics_engine, self.camera, self.score)

    def on_draw(self):
        """ Draw all the elements on the screen """
        self.drawing = Drawing()
        self.drawing.use_camera(self.camera)
        self.drawing.draw_objects(self.player_list, self.platform_list, self.coin_list, self.gem_list)
        # Activate the GUI camera before drawing GUI elements
        self.drawing.use_camera(self.gui_camera)
        self.drawing.draw_gui(self.score)


    def on_key_press(self, key, modifiers):
        """Update the player's movement on key press"""
        self.player_movement.movement(key, modifiers, self.player_sprite, self.physics_engine, self.jump_sound)

    def on_key_release(self, key, modifiers):
        """Update the player's movement on key release"""
        self.player_movement.movement_stop(key, modifiers, self.player_sprite)
        
    def on_update(self, delta_time):
        """Movement and game logic"""
        # Update the physics engine and camera
        self.do_updates.do_updates()
        # Process the coin hit
        self.do_updates.check_object_collision(self.coin_list, self.collect_coin_sound)
         # Process the gem hit
        self.do_updates.check_object_collision(self.gem_list, self.collect_gem_sound)



    
