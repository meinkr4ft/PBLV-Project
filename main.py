"""
This program shows how to:
  * Have one or more instruction screens
  * Show a 'Game over' text and halt the game
  * Allow the user to restart the game


If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.instruction_and_game_over_screens
"""

import arcade
import os
import settings
import rooms
from status_bar import StatusBar
from room import Room

import shot
import enemy
import random

def draw_background(background):
    arcade.draw_texture_rectangle(settings.SCREEN_WIDTH // 2, settings.SCREEN_HEIGHT // 2,
                                  settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT, background)


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, screen_width, screen_height):
        """ Constructor """
        # Call the parent constructor. Required and must be the first line.
        super().__init__(screen_width, screen_height)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # start some music


        # Set the background color
        self.background = arcade.load_texture("images/title_screen_background.png")
        main_theme = arcade.sound.load_sound("sounds/Theme.wav")
        arcade.sound.play_sound(main_theme)

        # Start 'state' will be showing the first page of instructions.
        self.current_state = settings.INSTRUCTIONS_PAGE
        self.current_menu = 0

        self.current_room = 0

        # Set up the player
        self.score = 0
        self.player_sprite = None
        self.physics_engine = None
        self.view_left = 0
        self.view_bottom = 0
        self.DOUBLE_JUMP_AVAILABLE = False
        self.LEFT_PRESSED = False
        self.RIGHT_PRESSED = False
        self.game_over = False
        self.rooms = None

        # STEP 1: Put each instruction page in an image. Make sure the image
        # matches the dimensions of the window, or it will stretch and look
        # ugly. You can also do something similar if you want a page between
        # each level.

        self.instructions = arcade.load_texture("images/background.png")

    def setup(self):
        """
        Set up the game.
        """


        # Set up the player
        self.score = 0
        self.player_sprite = arcade.Sprite("images/character.png", settings.PLAYER_SCALING)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.status_bar = StatusBar()
        self.rooms = []


        room = rooms.setup_room_1()
        self.rooms.append(room)
        room = rooms.setup_room_2()
        self.rooms.append(room)

        self.current_room = 0

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list,
                                                             gravity_constant=settings.GRAVITY)

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

    # STEP 2: Add this function.
    def draw_instructions_page(self):
        """
        Draw an instruction page. Load the page as an image.
        """
        page_texture = self.instructions
        if self.current_menu == 0:
            arcade.draw_text("Start", 240, 400, arcade.color.RED, 54)
            arcade.draw_text("Options", 240, 340, arcade.color.WHITE, 54)
            arcade.draw_text("About", 240, 280, arcade.color.WHITE, 54)
        elif self.current_menu == 1:
            arcade.draw_text("Start", 240, 400, arcade.color.WHITE, 54)
            arcade.draw_text("Options", 240, 340, arcade.color.RED, 54)
            arcade.draw_text("About", 240, 280, arcade.color.WHITE, 54)
        elif self.current_menu == 2:
            arcade.draw_text("Start", 240, 400, arcade.color.WHITE, 54)
            arcade.draw_text("Options", 240, 340, arcade.color.WHITE, 54)
            arcade.draw_text("About", 240, 280, arcade.color.RED, 54)

    # STEP 3: Add this function
    def draw_game_over(self):
        """
        Draw "Game over" across the screen.
        """
        output = "Game Over"
        arcade.draw_text(output, 240, 400, arcade.color.WHITE, 54)

        output = "Click to restart"
        arcade.draw_text(output, 310, 300, arcade.color.WHITE, 24)

    # STEP 4: Take the drawing code you currently have in your
    # on_draw method AFTER the start_render call and MOVE to a new
    # method called draw_game.
    def draw_game(self):
        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def draw_lives(self):
        pass
    # STEP 5: Update the on_draw function to look like this. Adjust according
    # to the number of instruction pages you have.
    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        if self.current_state == settings.INSTRUCTIONS_PAGE:
            draw_background(self.background)
            self.draw_instructions_page()

        elif self.current_state == settings.GAME_RUNNING:
            draw_background(self.rooms[self.current_room].background)
            self.status_bar.sprite_list.draw()
            self.rooms[self.current_room].wall_list.draw()
            self.draw_game()
            self.player_sprite.draw()
            self.draw_lives()

        elif self.current_state == settings.GAME_OVER:
            self.draw_game()
            self.draw_game_over()

    # change selected menu point 0 = up 1 = down
    def operate_menu(self, direction):
        sound = arcade.sound.load_sound("sounds/menu.wav")
        arcade.sound.play_sound(sound)
        if direction == 0 and self.current_menu > 0:
            self.current_menu = self.current_menu - 1
        if direction == 1 and self.current_menu < 2:
            self.current_menu = self.current_menu + 1

    def on_mouse_motion(self, x, y, dx, dy):
        pass

    def on_key_press(self, key, modifiers):
        if self.current_state == settings.INSTRUCTIONS_PAGE:
            if key == arcade.key.UP or key == arcade.key.W:
                self.operate_menu(0)
            elif key == arcade.key.DOWN or key == arcade.key.S:
                self.operate_menu(1)
            elif key == arcade.key.ENTER:
                self.background = None
                self.setup()
                self.current_state = settings.GAME_RUNNING

        elif self.current_state == settings.GAME_RUNNING:
            if key == arcade.key.UP or key == arcade.key.W:
                if self.physics_engine.can_jump():
                    self.DOUBLE_JUMP_AVAILABLE = True
                    self.player_sprite.change_y = settings.JUMP_SPEED
                elif self.DOUBLE_JUMP_AVAILABLE:
                    self.DOUBLE_JUMP_AVAILABLE = False
                    self.player_sprite.change_y = settings.SECOND_JUMP_SPEED
            elif key == arcade.key.LEFT or key == arcade.key.A:
                self.LEFT_PRESSED = True
                self.player_sprite.change_x = - settings.MOVEMENT_SPEED
            elif key == arcade.key.RIGHT or key == arcade.key.D:
                self.RIGHT_PRESSED = True
                self.player_sprite.change_x = settings.MOVEMENT_SPEED
            elif key == settings.WEAPON_SWAP_KEY:
                self.status_bar.selected +=1
                self.status_bar.selected %=3
                self.status_bar.update_sprites()

    def on_key_release(self, key, modifiers):
        # TODO - Cancel movement only when no key is pressed at all
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.LEFT_PRESSED = False
            if not self.RIGHT_PRESSED:
                self.player_sprite.change_x = 0
            else:
                self.player_sprite.change_x = settings.MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.RIGHT_PRESSED = False
            if not self.LEFT_PRESSED:
                self.player_sprite.change_x = 0
            else:
                self.player_sprite.change_x = - settings.MOVEMENT_SPEED

    # STEP 7: Only update if the game state is GAME_RUNNING like below:
    def update(self, delta_time):
        """ Movement and game logic """
        if self.current_state == settings.INSTRUCTIONS_PAGE:
            self.draw_instructions_page()

        # Only move and do things if the game is running.
        if self.current_state == settings.GAME_RUNNING:

            self.physics_engine.update()
            if self.physics_engine.can_jump():
                self.DOUBLE_JUMP_AVAILABLE = True

            # Do some logic here to figure out what room we are in, and if we need to go
            # to a different room.
            if self.player_sprite.center_x > settings.SCREEN_WIDTH and self.current_room == 0:
                self.current_room = 1
                self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                                     self.rooms[self.current_room].wall_list,
                                                                     gravity_constant=settings.GRAVITY)
                self.player_sprite.center_x = 0
            elif self.player_sprite.center_x < 0 and self.current_room == 1:
                self.current_room = 0
                self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                                     self.rooms[self.current_room].wall_list,
                                                                     gravity_constant=settings.GRAVITY)
                self.player_sprite.center_x = settings.SCREEN_WIDTH


def main():
    MyGame(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()
