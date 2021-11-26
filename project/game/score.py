import arcade

class Score:
    def __init__(self, score):
        super().__init__()
        self.score = score
        self.set_text()

    def set_text(self):
        self.text = f"Score: {self.score}"

    def get_text(self):
        return self.text

    def add_point(self):
        self.score += 1
        self.set_text()