import arcade

class Score:
    def __init__(self):
        super().__init__()
        self.score = 0
        self.set_text()

    def set_text(self):
        self.text = f"Score: {self.score}"

    def get_text(self):
        return self.text

    def add_point(self, points):
        self.score += points
        self.set_text()