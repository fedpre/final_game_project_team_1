import arcade
from game import constants
from game.views import InstructionView

def main():
        """ Main Function """
        window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
        start_view = InstructionView()
        window.show_view(start_view)
        arcade.run()

if __name__ == "__main__":
    main()



