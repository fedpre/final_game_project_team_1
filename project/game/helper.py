import arcade
from game import constants
from game.coins import Coins
from game.gems import Gems
from game.stone import Stone
from game.crate import Crate
from game.small_platforms import SmallPlatforms

class Helper():
    def create_ground(self, list):
        counter = 0
        for x in range(0, constants.PLATFORM_LENGTH, 60):
            if counter < 31 and counter > 27:
                counter += 1
                continue
            self.stone = Stone(x)
            list.append(self.stone)
            counter += 1

    def create_coins(self, coordinates, list):
        for position in coordinates:
            coin = Coins()
            coin.position = position
            list.append(coin)

    def create_gems(self, coordinates, list):
        for position in coordinates:
            gem = Gems()
            gem.position = position
            list.append(gem)

    def create_crates(self, coordinates, list):
        for position in coordinates:
            crate = Crate()
            crate.position = position
            list.append(crate)

    def create_small_platforms(self, coordinates, list):
        for position in coordinates:
            small_platforms = SmallPlatforms()
            small_platforms.position = position
            list.append(small_platforms)