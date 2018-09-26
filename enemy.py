import arcade
import settings

class Enemy(arcade.Sprite):

    def __init__(self,moveing,shooting,shooting_intervall,moveing_intervall):
        super().__init__()


        # Load a left facing texture and a right facing texture.
        # mirrored=True will mirror the image we load.

        self.shot_texture = arcade.load_texture("images/bullet.png")
        self.texture_left = arcade.load_texture("images/enemy.png", mirrored=True, scale=settings.ENEMY_SCALING)
        self.texture_right = arcade.load_texture("images/enemy.png", scale=settings.ENEMY_SCALING)

        # By default, face right.
        self.texture = self.texture_right
        self.direction = 1
        self.shooting = shooting
        self.moveing = moveing
        self.shooting_intervall = shooting_intervall
        self.moveing_intervall = moveing_intervall



    def update(self):
        if self.moveing:
            self.change_x = settings.ENEMY_SPEED * self.direction
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Figure out if we should face left or right
        if self.change_x < 0:
            self.texture = self.texture_left
        if self.change_x > 0:
            self.texture = self.texture_right

        if self.left < 0:
            self.left = 0
        elif self.right > settings.SCREEN_WIDTH - 1:
            self.right = settings.SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > settings.GAME_HEIGHT - 1:
            self.top = settings.GAME_HEIGHT - 1

    def change_direction(self):
        self.direction = self.direction * -1
        if self.direction == -1:
            self.texture = self.texture_left
