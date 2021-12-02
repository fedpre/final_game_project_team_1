import os

#Screen Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "TEAM 01 ARCADE GAME"
PLATFORM_LENGTH = 2500

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

# Music files
JUMP_SOUND = ":resources:sounds/phaseJump1.wav"
COIN_SOUND = ":resources:sounds/coin1.wav"
GEM_SOUND = ":resources:sounds/coin1.wav"

# Sprites Images
IMAGE_PLAYER = ":resources:images/animated_characters/female_person/femalePerson_idle.png"
GROUND_IMAGE = ":resources:images/tiles/stoneMid.png"
COINS_IMAGE = ":resources:images/items/gold_1.png"
GEMS_IMAGE = ":resources:images/items/gemGreen.png"
CRATE_IMAGE = ":resources:images/tiles/boxCrate_double.png"

#Sprites Coordinates
COINS_COORDINATES = [[256, 150], [512, 150]]
GEMS_COORDINATES = [[384, 325], [640, 325]]
CRATES_COORDINATES = [[256, 96], [384, 275], [512, 96], [640, 275], [768, 275]]

GAME_TIMER_LENGTH = 20 #SECONDS
