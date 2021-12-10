import arcade
class DoUpdates:
    def __init__(self, player, physics_engine, camera, score, timer, enemies):
        self._player = player
        self._engine = physics_engine
        self._camera = camera
        self._score = score
        self._timer = timer
        self._enemies = enemies
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
    def check_flag_collision(self, object_list, setup, gameover, level_counter):
        object_hit_list = arcade.check_for_collision_with_list(
            self._player, object_list
        )
        for obj in object_hit_list:
            if (level_counter == 3):
                gameover()
            else:
                setup()
        


    def check_falling(self):
        if self._player.center_y < - 100:
            self._player.center_x = self._player.get_x()
            self._player.center_y = self._player.get_y()
                    
    def update_animation(self, enemy_list):
        for enemy in enemy_list:
            enemy.center_x -= 3
        self._player.update_animation()
        for enemy in self._enemies:
            enemy.update_animation()
        
    def check_collision_enemies(self, en_li, game_over):
        hit_list = arcade.check_for_collision_with_list(
            self._player, en_li
        )
        for enemy in hit_list:
            game_over()