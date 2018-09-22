import arcade
import settings

SCREEN_HEIGHT = settings.SCREEN_HEIGHT
SCREEN_WIDTH = settings.SCREEN_WIDTH
SPRITE_NATIVE_SIZE = settings.SPRITE_NATIVE_SIZE


class StatusBar:
    def __init__(self):
        # status bar values
        self.lives = 5
        self.health = 5
        self.max_health = 8
        self.health_cap = 10
        self.key_cap = 10
        # 3 types of weapons
        self.selected = 2
        self.weapon_count = 3
        self.weapons = [1,1,1]

        self.sprite_list = arcade.SpriteList()
        self.update_sprites()

    def update_sprites(self):
        self.sprite_list = arcade.SpriteList()
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
            self.sprite_list.append(heart)

        start_index += self.max_health +1
        # weapons
        for i in range(start_index, start_index + self.weapon_count):
            index = i - start_index
            src = self.get_weapon_src(index)
            weapon = arcade.Sprite(src)
            weapon.top = SCREEN_HEIGHT
            weapon.left = i*SPRITE_NATIVE_SIZE
            self.sprite_list.append(weapon)

            if self.selected == index:
                select_arrow = arcade.Sprite("images/select_arrow.png")
                select_arrow.top = SCREEN_HEIGHT - SPRITE_NATIVE_SIZE
                select_arrow.left = weapon.left
                self.sprite_list.append(select_arrow)

    def get_weapon_src(self, slot):
        if self.weapons[slot] == 0:
            return "images/weapon_empty.png"
        elif self.weapons[slot] == 1:
            return "images/Sword1.png"
