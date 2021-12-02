import arcade
from game import constants


class Timer:
    def __init__(self):
        super().__init__()
        self.reset_timer()

    def add_time(self, time_delta):
        self.timer -= time_delta
        self.set_text()
        

    def set_text(self):
        self.text = f"Timer: {self.timer:.0f}"

    def get_text(self):
        return self.text
    
    def reset_timer(self):
        self.timer = constants.GAME_TIMER_LENGTH
        self.set_text()
