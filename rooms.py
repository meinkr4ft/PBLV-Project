import arcade
import settings
from room import Room

# only up and right
def from_to(list, src, a, x, y, dir):
    if dir == arcade.key.UP:
        for i in range(a):
            sprite = arcade.Sprite(src, settings.SPRITE_SCALING)
            sprite.bottom = (y + i)*settings.SPRITE_SIZE
            sprite.left = x*settings.SPRITE_SIZE
            list.append(sprite)

    elif dir == arcade.key.RIGHT:
        for i in range(a):
            sprite = arcade.Sprite(src, settings.SPRITE_SCALING)
            sprite.bottom = y * settings.SPRITE_SIZE
            sprite.left  = (x + i)*settings.SPRITE_SIZE
            list.append(sprite)
    else:
        raise Exception("bad input")


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
    room.spikes_list = arcade.SpriteList()
    room.item_list = arcade.SpriteList()

    # -- Set up the walls
    # Create bottom and top row of boxes
    # This y loops a list of two, the coordinate 0, and just under the top of window
    for y in (0, settings.GAME_HEIGHT - settings.SPRITE_SIZE):
        # Loop for each box going across
        for x in range(0, settings.SCREEN_WIDTH, settings.SPRITE_SIZE):
            if not (y==0 and x>=7*settings.SPRITE_SIZE and x<=9*settings.SPRITE_SIZE):
                wall = arcade.Sprite("images/wall.png", settings.SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)
            else:
                spikes = arcade.Sprite("images/spikes.png", settings.SPRITE_SCALING)
                spikes.left = x
                spikes.bottom = y
                room.spikes_list.append(spikes)

    # Create left and right column of boxes
    for x in (0, settings.SCREEN_WIDTH - settings.SPRITE_SIZE):
        # Loop for each box going across
        for y in range(settings.SPRITE_SIZE, settings.GAME_HEIGHT - settings.SPRITE_SIZE, settings.SPRITE_SIZE):
            # Skip making a block 4 and 5 blocks up on the right side
            if (y != settings.SPRITE_SIZE * 1 and y != settings.SPRITE_SIZE * 2) or x == 0:
                wall = arcade.Sprite("images/wall.png", settings.SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    heart = arcade.Sprite("images/heart_full1.png", settings.SPRITE_SCALING)
    heart.center_x = 12 * settings.SPRITE_SIZE
    heart.bottom = 1 * settings.SPRITE_SIZE
    room.item_list.append(heart)

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
    room.item_list = arcade.SpriteList()
    room.spikes_list = arcade.SpriteList()

    src = "images/wall.png"
    from_to(room.wall_list, src, 15, 0, 0, arcade.key.RIGHT)
    from_to(room.wall_list, src, 15, 0, 9, arcade.key.RIGHT)
    from_to(room.wall_list, src, 6, 0, 3, arcade.key.UP)
    from_to(room.wall_list, src, 5, 14, 1, arcade.key.UP)
    from_to(room.wall_list, src, 1, 14, 8, arcade.key.UP)

    from_to(room.wall_list, src, 3, 1, 4, arcade.key.RIGHT)
    from_to(room.wall_list, src, 1, 4, 2, arcade.key.RIGHT)
    from_to(room.wall_list, src, 4, 5, 1, arcade.key.UP)
    from_to(room.wall_list, src, 1, 6, 4, arcade.key.RIGHT)
    from_to(room.wall_list, src, 5, 7, 3, arcade.key.RIGHT)
    from_to(room.wall_list, src, 1, 12, 4, arcade.key.RIGHT)
    from_to(room.wall_list, src, 1, 13, 2, arcade.key.RIGHT)
    from_to(room.wall_list, src, 3, 1, 4, arcade.key.RIGHT)

    src = "images/spikes.png"
    from_to(room.spikes_list, src, 5, 7, 4, arcade.key.RIGHT)

    room.background = arcade.load_texture("images/background.png")

    return room

def setup_room_3():
    """
    Create and return room 2.
    """
    room = Room()

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.item_list = arcade.SpriteList()
    room.spikes_list = arcade.SpriteList()

    src = "images/wall.png"
    from_to(room.wall_list, src, 6, 0, 0, arcade.key.UP)
    from_to(room.wall_list, src, 2, 0, 8, arcade.key.UP)
    from_to(room.wall_list, src, 9, 3, 0, arcade.key.UP)
    from_to(room.wall_list, src, 1, 4, 3, arcade.key.UP)
    from_to(room.wall_list, src, 1, 4, 6, arcade.key.UP)

    from_to(room.wall_list, src, 2, 0, 8, arcade.key.UP)
    from_to(room.wall_list, src, 14, 1, 9, arcade.key.RIGHT)
    from_to(room.wall_list, src, 9, 6, 0, arcade.key.RIGHT)
    from_to(room.wall_list, src, 8, 14, 2, arcade.key.UP)

    room.background = arcade.load_texture("images/background.png")

    return room

def setup_room_4():
    """
    Create and return room 2.
    """
    room = Room()

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.item_list = arcade.SpriteList()
    room.spikes_list = arcade.SpriteList()

    src = "images/wall.png"
    from_to(room.wall_list, src, 10, 0, 0, arcade.key.UP)
    from_to(room.wall_list, src, 14, 1, 0, arcade.key.RIGHT)
    from_to(room.wall_list, src, 9, 14, 1, arcade.key.UP)
    from_to(room.wall_list, src, 2, 3, 8, arcade.key.UP)
    from_to(room.wall_list, src, 9, 4, 7, arcade.key.RIGHT)
    from_to(room.wall_list, src, 8, 6, 9, arcade.key.RIGHT)

    from_to(room.wall_list, src, 1, 3, 3, arcade.key.RIGHT)
    from_to(room.wall_list, src, 1, 7, 4, arcade.key.RIGHT)
    from_to(room.wall_list, src, 1, 10, 4, arcade.key.RIGHT)
    from_to(room.wall_list, src, 1, 13, 4, arcade.key.RIGHT)

    room.background = arcade.load_texture("images/background.png")

    return room
