import os

#Screen Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "TEAM 01 ARCADE GAME"

#Sprite Constants scaled in relation to the original pics
CHARACTER_SCALING = 1
TILE_SCALING = 0.5

# Player Movement
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 1
PLAYER_JUMP_SPEED = 20

# Path
PATH = os.path.dirname(os.path.abspath(__file__))
BACKGROUND_MUSIC_PATH = PATH + "/sounds/background.wav"