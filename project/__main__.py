import arcade
from game.director import TeamGame

def main():
        """ Main Function """
        newGame = TeamGame()
        newGame.setup()
        arcade.run()

if __name__ == "__main__":
    main()



