import arcade

class DoUpdates:
    def __init__(self, player, physics_engine, camera, score, timer):
        self._player = player
        self._engine = physics_engine
        self._camera = camera
        self._score = score
        self._timer = timer

        self._engine.update()

    def do_updates(self):
        self._engine.update()
        self._camera.center_camera_to_player(self._player)

    def check_prop_collision(self, object_list, sound):
        object_hit_list = arcade.check_for_collision_with_list(
            self._player, object_list
        )
        for obj in object_hit_list:
            # Remove the object
            obj.remove_from_sprite_lists()
            # Play a sound
            arcade.play_sound(sound)
            points = obj.get_value()
            self._score.add_point(points)

    def check_flag_collision(self, object_list, setup):
        object_hit_list = arcade.check_for_collision_with_list(
            self._player, object_list
        )
        for obj in object_hit_list:
            setup()

    def check_falling(self, player):
        if player.center_y < - 100:
            player.center_x = player.get_x()
            player.center_y = player.get_y()
    
    def update_animation(self, player):
        player.update_animation()

   

    