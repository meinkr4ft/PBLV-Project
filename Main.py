"""
This program shows how to:
  * Have one or more instruction screens
  * Show a 'Game over' text and halt the game
  * Allow the user to restart the game


If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.instruction_and_game_over_screens
"""

import arcade
import random
import os

BLOCK_SIZE = 30
SPRITE_SCALING = 1
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)

SCREEN_WIDTH = 30*BLOCK_SIZE
SCREEN_HEIGHT = 20*BLOCK_SIZE

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 40
RIGHT_MARGIN = 150

# Physics
MOVEMENT_SPEED = 2.5
JUMP_SPEED = 5
GRAVITY = 0.25

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
        arcade.set_background_color(arcade.color.AMAZON)

        # Start 'state' will be showing the first page of instructions.
        self.current_state = INSTRUCTIONS_PAGE
        self.current_menu = 0

        self.player_list = None
        self.coin_list = None
        self.wall_list = None

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
        self.coin_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        # Draw the walls on the bottom and top
        for y in(0, SCREEN_HEIGHT - BLOCK_SIZE):
            for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
                wall = arcade.Sprite("images/wall.png")

                wall.left = x
                wall.bottom = y
                self.wall_list.append(wall)

        # Draw the walls on the side
        for x in (0, SCREEN_WIDTH - BLOCK_SIZE):
            for y in range(BLOCK_SIZE, SCREEN_HEIGHT - BLOCK_SIZE, BLOCK_SIZE):
                if (y != 4*BLOCK_SIZE and y != 5*BLOCK_SIZE) or x==0:
                    wall = arcade.Sprite("images/wall.png")
                    wall.left = x;
                    wall.bottom = y
                    self.wall_list.append(wall)
        wall = arcade.Sprite("images/coin_01.png")
        wall.center_x = 300
        wall.bottom = BLOCK_SIZE
        self.wall_list.append(wall)

        # Set up the player
        self.score = 0
        self.player_sprite = arcade.Sprite("images/character.png")
        self.player_sprite.center_x = 2*BLOCK_SIZE
        self.player_sprite.center_y = 2*BLOCK_SIZE
        self.player_list.append(self.player_sprite)

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             self.wall_list,
                                                             gravity_constant=GRAVITY)

        for i in range(50):

            # Create the coin instance
            coin = arcade.Sprite("images/coin_01.png", SPRITE_SCALING / 3)

            # Position the coin
            coin.center_x = random.randrange(BLOCK_SIZE, SCREEN_WIDTH - BLOCK_SIZE)
            coin.center_y = random.randrange(BLOCK_SIZE, SCREEN_HEIGHT - BLOCK_SIZE)

            # Add the coin to the lists
            self.coin_list.append(coin)

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
        self.wall_list.draw()
        self.player_list.draw()
        self.coin_list.draw()

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


    # change selected menu point 0 = up 1 = down
    def operate_menu(self,direction):
        if direction == 0 and self.current_menu > 0:
            self.current_menu = self.current_menu - 1
        if direction == 1 and self.current_menu < 2:
            self.current_menu = self.current_menu + 1



    def on_mouse_motion(self, x, y, dx, dy):
        pass

    def on_key_press(self, key, modifiers):
        if self.current_state == INSTRUCTIONS_PAGE:
            if key == arcade.key.UP or key == arcade.key.W:
                self.operate_menu(0)
            elif key == arcade.key.DOWN or key == arcade.key.S:
                self.operate_menu(1)
            elif key == arcade.key.ENTER:
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
            self.coin_list.update()
            self.player_list.update()
            self.wall_list.update()

            # Generate a list of all sprites that collided with the player.
            hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

            self.physics_engine.update()
            # Loop through each colliding sprite, remove it, and add to the
            # score.
            for coin in hit_list:
                coin.kill()
                self.score += 1

            # If we've collected all the games, then move to a "GAME_OVER"
            # state.
            if len(self.coin_list) == 0:
                self.current_state = GAME_OVER
                self.set_mouse_visible(True)


def main():
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()
