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