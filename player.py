import arcade
import settings

player = arcade.AnimatedWalkingSprite()
player.texture = (arcade.load_texture("images/character1.png",
                                                       scale=settings.PLAYER_SCALING))

player.stand_right_textures = []
player.stand_right_textures.append(arcade.load_texture("images/character1.png",
                                                       scale=settings.PLAYER_SCALING))
player.stand_left_textures = []
player.stand_left_textures.append(arcade.load_texture("images/character1.png",
                                                      scale=settings.PLAYER_SCALING, mirrored=True))

player.walk_right_textures = []

player.walk_right_textures.append(arcade.load_texture("images/character1.png",
                                                      scale=settings.PLAYER_SCALING))
player.walk_right_textures.append(arcade.load_texture("images/character2.png",
                                                      scale=settings.PLAYER_SCALING))
player.walk_right_textures.append(arcade.load_texture("images/character3.png",
                                                      scale=settings.PLAYER_SCALING))
player.walk_right_textures.append(arcade.load_texture("images/character4.png",
                                                      scale=settings.PLAYER_SCALING))

player.walk_left_textures = []

player.walk_left_textures.append(arcade.load_texture("images/character1.png",
                                                     scale=settings.PLAYER_SCALING, mirrored=True))
player.walk_left_textures.append(arcade.load_texture("images/character2.png",
                                                     scale=settings.PLAYER_SCALING, mirrored=True))
player.walk_left_textures.append(arcade.load_texture("images/character3.png",
                                                     scale=settings.PLAYER_SCALING, mirrored=True))
player.walk_left_textures.append(arcade.load_texture("images/character4.png",
                                                     scale=settings.PLAYER_SCALING, mirrored=True))

player.texture_change_distance = 30
