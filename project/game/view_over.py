import arcade
from game import constants
import arcade.gui
from arcade.gui import UIManager
import game.views

class Game_overView(arcade.View):

    def __init__(self):
        super().__init__()
        self.ui_manager = UIManager()
        self.ui_manager.enable()
        self.v_box = arcade.gui.UIBoxLayout()
        self.ui_manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )
    def on_show(self):
        arcade.set_viewport(0, constants.SCREEN_WIDTH, 0, constants.SCREEN_HEIGHT)
        message_box = arcade.gui.UIMessageBox(
            width=300,
            height=200,
            message_text=(
                "GAME OVER \n"
                "Restart Game?"
            ),
            callback=self.on_message_box_close,
            buttons=["Restart", "Quit"]
        )
        self.ui_manager.add(message_box)

    def on_draw(self):
        self.ui_manager.draw()
       
    def on_message_box_close(self, button_text):
        if button_text == "Quit":
            arcade.exit()
        else:
            game_view = game.views.InstructionView()
            self.window.show_view(game_view)