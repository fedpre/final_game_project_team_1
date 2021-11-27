import arcade
from game import constants
from game.director import GameView

class InstructionView(arcade.View):

    def on_show(self):
        #this is run once we swithc to this view
        arcade.set_background_color(arcade.csscolor.MIDNIGHT_BLUE)

        #reset the viewport
        arcade.set_viewport(0, constants.SCREEN_WIDTH, 0, constants.SCREEN_HEIGHT)

    def on_draw(self):
        """ Draw this view"""
        arcade.start_render()
        arcade.draw_text("Instructions Screen", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance",  constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2-75,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
        arcade.draw_text("Press arrow keys or WASD to move around",  constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2-150,
                         arcade.color.YELLOW_ROSE, font_size=20, anchor_x="center")
        arcade.draw_text("(Press space bar to jump too...)",  constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2-180,
                         arcade.color.YELLOW_ROSE, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ if the user presses the mouse, start the game"""
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)
        