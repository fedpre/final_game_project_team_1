import arcade
from game import constants

class Drawing():
    def __init__(self):
        arcade.start_render()

    def draw_objects(self, *argv):
        for arg in argv:
            arg.draw()

    def use_camera(self, *argv):
        for arg in argv:
            arg.use()

    def draw_gui(self, score):
        # Draw our score on the screen, scrolling it with the viewport
        score_text = score.get_text()

        arcade.draw_text(
            score_text,
            10,
            10,
            arcade.csscolor.WHITE,
            18,
        )
    def draw_gui_timer(self, timer):
        # Draw our timer on the screen, scrolling it with the viewport
        timer_text = timer.get_text()
        arcade.draw_text(
            timer_text,
            constants.SCREEN_WIDTH-120,
            constants.SCREEN_HEIGHT-25,
            arcade.csscolor.WHITE,
            18,
        )

    def draw_gui_level(self, level):
        # Draw the level on the screen, scrolling it with the viewport
        level_text = level.get_text()
        arcade.draw_text(
            level_text,
            constants.SCREEN_WIDTH-250,
            constants.SCREEN_HEIGHT-25,
            arcade.csscolor.WHITE,
            18,
        )