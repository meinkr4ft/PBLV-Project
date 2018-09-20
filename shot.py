import arcade
BULLET_SPEED = 5
class Shot(arcade.Sprite):
    def __init__(self,direction,x,y):
        super().__init__()
        self.direction =  direction
        self.texture = arcade.load_texture("images/bullet.png")
        self.center_x = x
        self.center_y = y

    def update(self):
        self.center_x += BULLET_SPEED*self.direction
