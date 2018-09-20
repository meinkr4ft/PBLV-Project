import arcade
import random
import os
import shot
import enemy


SPRITE_SCALING = 0.5
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 40
RIGHT_MARGIN = 150

# Physics
MOVEMENT_SPEED = 5
JUMP_SPEED = 14
GRAVITY = 0.5

# These numbers represent "states" that the game can be in.
INSTRUCTIONS_PAGE = 0
GAME_RUNNING = 1
GAME_OVER = 2
MENU_LENGHT = 3


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

        # Set the background color
        arcade.set_background_color(arcade.color.AFRICAN_VIOLET)
        theme = arcade.sound.load_sound("sounds/Theme.wav")
        arcade.sound.play_sound(theme)

        # Start 'state' will be showing the first page of instructions.
        self.current_state = INSTRUCTIONS_PAGE
        self.current_menu = 0

        self.frame_count = 0
        self.player_list = None
        self.coin_list = None
        self.wall_list = None
        self.enemy_list = None
        self.bullet_list = None

        # Set up the player
        self.score = 0
        self.player_sprite = None
        self.physics_engine = None
        self.view_left = 0
        self.view_bottom = 0
        self.game_over = False

        # STEP 1: Put each instruction page in an image. Make sure the image
        # matches the dimensions of the window, or it will stretch and look
        # ugly. You can also do something similar if you want a page between
        # each level.


        self.instructions =  arcade.load_texture("images/background.png")


    def setup(self):
        """
        Set up the game.
        """
        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()


        # Draw the walls on the bottom
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
            wall = arcade.Sprite("images/wall.png", 4*SPRITE_SCALING)

            wall.bottom = 0
            wall.left = x
            self.wall_list.append(wall)


        # Set up the player
        self.score = 0
        self.player_sprite = arcade.Sprite("images/character.png", SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)



        #set up enemy
        en = enemy.Enemy()
        en.center_x = 400
        en.center_y = 50
        self.enemy_list.append(en)
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             self.wall_list,
                                                             gravity_constant=GRAVITY)
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
        """
        Draw all the sprites, along with the score.
        """
        # Draw all the sprites.
        self.frame_count = self.frame_count + 1
        self.bullet_list.draw()
        self.wall_list.draw()
        self.player_list.draw()
        self.enemy_list.draw()

        if self.frame_count%120 == 0:
            for en in self.enemy_list:
                self.bullet_list.append(shot.Shot(en.direction,en.center_x,en.center_y))

        if self.frame_count % 240 == 0:
           for en in self.enemy_list:
            en.change_direction()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    # STEP 5: Update the on_draw function to look like this. Adjust according
    # to the number of instruction pages you have.
    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        if self.current_state == INSTRUCTIONS_PAGE:
            self.draw_instructions_page()



        elif self.current_state == GAME_RUNNING:
            self.draw_game()

        else:
            self.draw_game()
            self.draw_game_over()

    # STEP 6: Do something like adding this to your on_mouse_press to flip
    # between instruction pages.

    # change selected menu point 0 = up 1 = down
    def operate_menu(self,direction):
        sound = arcade.sound.load_sound("sounds/menu.wav")
        arcade.sound.play_sound(sound)
        if direction == 0 and self.current_menu > 0:
            self.current_menu = self.current_menu - 1
        if direction == 1 and self.current_menu < 2:
            self.current_menu = self.current_menu + 1

    def on_key_press(self, key, modifiers):
        if self.current_state == INSTRUCTIONS_PAGE:
            if key == arcade.key.UP or key == arcade.key.W:
                self.operate_menu(0)
            elif key == arcade.key.DOWN or key == arcade.key.S:
                self.operate_menu(1)
            elif key == arcade.key.ENTER:
                if self.current_menu == 0:
                    self.setup()
                    self.current_state = GAME_RUNNING

        elif self.current_state == GAME_RUNNING:
            if key == arcade.key.UP or key == arcade.key.W:
                if self.physics_engine.can_jump():
                    self.player_sprite.change_y = JUMP_SPEED
            elif key == arcade.key.LEFT or key == arcade.key.A:
                self.player_sprite.change_x = - MOVEMENT_SPEED
            elif key == arcade.key.RIGHT or key == arcade.key.D:
                self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        # TODO - Cancel movement only when no key is pressed at all
        if key == arcade.key.LEFT or key == arcade.key.RIGHT\
                or key == arcade.key.A or key == arcade.key.D:
            self.player_sprite.change_x = 0

    # STEP 7: Only update if the game state is GAME_RUNNING like below:
    def update(self, delta_time):
        """ Movement and game logic """
        if self.current_state == INSTRUCTIONS_PAGE:
            self.draw_instructions_page()


        # Only move and do things if the game is running.
        if self.current_state == GAME_RUNNING:
            # Call update on all sprites (The sprites don't do much in this
            # example though.)
            hit_list = arcade.check_for_collision_with_list(self.player_list[0], self.bullet_list)
            self.score = self.score + hit_list.__len__()
            for bullet in hit_list:
                bullet.kill()
            self.player_list.update()
            self.wall_list.update()
            self.bullet_list.update()
            self.enemy_list.update()

            # Generate a list of all sprites that collided with the player.
           # hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

            self.physics_engine.update()
            # Loop through each colliding sprite, remove it, and add to the
            # score.


            # If we've collected all the games, then move to a "GAME_OVER"
            # state.


def main():
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()
