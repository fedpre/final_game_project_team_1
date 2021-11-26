import arcade

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