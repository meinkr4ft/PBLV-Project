import arcade
import settings
from room import Room

def setup_room_1():
    """
    Create and return room 1.
    If your program gets large, you may want to separate this into different
    files.
    """
    room = Room()

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()

    # -- Set up the walls
    # Create bottom and top row of boxes
    # This y loops a list of two, the coordinate 0, and just under the top of window
    for y in (0, settings.GAME_HEIGHT - settings.SPRITE_SIZE):
        # Loop for each box going across
        for x in range(0, settings.SCREEN_WIDTH, settings.SPRITE_SIZE):
            wall = arcade.Sprite("images/wall.png", settings.SPRITE_SCALING)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    # Create left and right column of boxes
    for x in (0, settings.SCREEN_WIDTH - settings.SPRITE_SIZE):
        # Loop for each box going across
        for y in range(settings.SPRITE_SIZE, settings.GAME_HEIGHT - settings.SPRITE_SIZE, settings.SPRITE_SIZE):
            # Skip making a block 4 and 5 blocks up on the right side
            if (y != settings.SPRITE_SIZE * 4 and y != settings.SPRITE_SIZE * 5) or x == 0:
                wall = arcade.Sprite("images/wall.png", settings.SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    wall = arcade.Sprite("images/wall.png", settings.SPRITE_SCALING)
    wall.left = 23 * settings.SPRITE_SIZE
    wall.bottom = 2 * settings.SPRITE_SIZE
    room.wall_list.append(wall)

    # If you want coins or monsters in a level, then add that code here.

    # Load the background image for this level.
    room.background = arcade.load_texture("images/background.png")

    return room


def setup_room_2():
    """
    Create and return room 2.
    """
    room = Room()

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()

    # -- Set up the walls
    # Create bottom and top row of boxes
    # This y loops a list of two, the coordinate 0, and just under the top of window
    for y in (0, settings.GAME_HEIGHT - settings.SPRITE_SIZE):
        # Loop for each box going across
        for x in range(0, settings.SCREEN_WIDTH, settings.SPRITE_SIZE):
            wall = arcade.Sprite("images/wall.png", settings.SPRITE_SCALING)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    # Create left and right column of boxes
    for x in (0, settings.SCREEN_WIDTH - settings.SPRITE_SIZE):
        # Loop for each box going across
        for y in range(settings.SPRITE_SIZE, settings.GAME_HEIGHT - settings.SPRITE_SIZE, settings.SPRITE_SIZE):
            # Skip making a block 4 and 5 blocks up
            if (y != settings.SPRITE_SIZE * 4 and y != settings.SPRITE_SIZE * 5) or x != 0:
                wall = arcade.Sprite("images/wall.png", settings.SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    wall = arcade.Sprite("images/wall.png", settings.SPRITE_SCALING)
    wall.left = 2 * settings.SPRITE_SIZE
    wall.bottom = 2 * settings.SPRITE_SIZE
    room.wall_list.append(wall)
    room.background = arcade.load_texture("images/background.png")

    return room