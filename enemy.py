import arcade
SPRITE_SCALING = 0.5
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

ENEMY_SPEED = 2

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 40
RIGHT_MARGIN = 150

class Enemy(arcade.Sprite):

    def __init__(self):
        super().__init__()


        # Load a left facing texture and a right facing texture.
        # mirrored=True will mirror the image we load.
        self.texture_left = arcade.load_texture("images/enemy.png", mirrored=True, scale=SPRITE_SCALING)
        self.texture_right = arcade.load_texture("images/enemy.png", scale=SPRITE_SCALING)

        # By default, face right.
        self.texture = self.texture_right
        self.direction = 1


    def update(self):
        self.change_x = ENEMY_SPEED * self.direction
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Figure out if we should face left or right
        if self.change_x < 0:
            self.texture = self.texture_left
        if self.change_x > 0:
            self.texture = self.texture_right

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1

    def change_direction(self):
        self.direction = self.direction * -1
