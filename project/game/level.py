import arcade

class Level:
    def __init__(self):
        self._level = 0
        self.set_text()

    def set_text(self):
        self.text = f"Level: {self._level}"

    def get_text(self):
        return self.text
        
    def increment_level(self):
        self._level += 1
        self.set_text()

    def get_level(self):
        return self._level

    