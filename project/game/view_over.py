import arcade
from game import constants

class Game_overView(arcade.View):

    def on_show(self):
        #this is run once we swithc to this view
        arcade.set_background_color(arcade.csscolor.MIDNIGHT_BLUE)

        #reset the viewport
        arcade.set_viewport(0, constants.SCREEN_WIDTH, 0, constants.SCREEN_HEIGHT)

    def on_draw(self):
        """ Draw this view"""
        arcade.start_render()
        arcade.draw_text("Game Over Screen", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """End Over"""
        