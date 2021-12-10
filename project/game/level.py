import arcade

class Level:
    def __init__(self):
        self._level = 0

    def increment_level(self):
        self._level += 1

    def get_level(self):
        return self._level
