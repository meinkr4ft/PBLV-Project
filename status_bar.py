import arcade
import settings

SCREEN_HEIGHT = settings.SCREEN_HEIGHT
SCREEN_WIDTH = settings.SCREEN_WIDTH
SPRITE_NATIVE_SIZE = settings.SPRITE_NATIVE_SIZE


class StatusBar:
    def __init__(self):
        # status bar values
        self.lives = 3
        self.health = 3
        self.max_health = 3
        self.health_cap = 10
        self.key_cap = 10
        # 3 types of weapons
        self.selected = 2
        self.weapon_count = 3
        self.weapons = [0,0,0]

        self.hearts = []
        self.slot_list = arcade.SpriteList()
        self.setup()

    def setup(self):
        start_index = 0
        health_remaining = self.health
        # hearts
        for i in range(start_index, self.max_health):
            src = "images/heart_full1.png"
            if health_remaining <= 0:
                src = "images/heart_empty1.png"
            health_remaining -= 1
            heart = arcade.Sprite(src)
            heart.top = SCREEN_HEIGHT
            heart.left = i*SPRITE_NATIVE_SIZE
            self.hearts.append(heart)

        start_index += self.max_health +1
        # weapons
        for i in range(start_index, start_index + self.weapon_count):
            index = i - start_index
            src = self.get_weapon_src(index)
            weapon = arcade.Sprite(src)
            weapon.top = SCREEN_HEIGHT
            weapon.left = i*SPRITE_NATIVE_SIZE
            self.slot_list.append(weapon)

            if self.selected == index:
                select_arrow = arcade.Sprite("images/select_arrow.png")
                select_arrow.top = SCREEN_HEIGHT - SPRITE_NATIVE_SIZE
                select_arrow.left = weapon.left
                self.slot_list.append(select_arrow)

    def draw_hearts(self):
        for h in self.hearts:
            h.draw()

    def update_hearts(self):
        for i in range(len(self.hearts)):
            self.hearts[i].kill()

        start_index = 0
        health_remaining = self.health
        # hearts
        for i in range(start_index, self.max_health):
            src = "images/heart_full1.png"
            if health_remaining <= 0:
                src = "images/heart_empty1.png"
            health_remaining -= 1
            heart = arcade.Sprite(src)
            heart.top = SCREEN_HEIGHT
            heart.left = i*SPRITE_NATIVE_SIZE
            self.hearts.append(heart)



    def get_weapon_src(self, slot):
        if self.weapons[slot] == 0:
            return "images/weapon_empty.png"
        elif self.weapons[slot] == 1:
            return "images/Sword1.png"
