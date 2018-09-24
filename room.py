import enemy
import shot
class Room:
    """
    This class holds all the information about the
    different rooms.
    """

    def __init__(self):
        # You may want many lists. Lists for coins, monsters, etc.
        self.wall_list = None
        self.spikes_list = None
        self.enemy_list = None
        self.item_list = None
        self.bullet_list = None
        self.frame_count = 0

        # This holds the background images. If you don't want changing
        # background images, you can delete this part.
        self.background = None

    def get_lists(self):
        ret = []
        if (self.wall_list is not None):
            ret.append(self.wall_list)
        if (self.spikes_list is not None):
            ret.append(self.spikes_list)
        if (self.enemy_list is not None):
            ret.append(self.enemy_list)
        if (self.item_list is not None):
            ret.append(self.item_list)
        if (self.bullet_list is not None):
            ret.append(self.bullet_list)
        return ret
    def update(self):
        #frame count as timer
        self.frame_count = self.frame_count + 1
        #change  driection of moveing enemies
        for en in self.enemy_list:
            if en.moveing:
                if self.frame_count%en.moveing_intervall == 0:
                    en.change_direction()
        #create bullets
            if en.shooting:
                if self.frame_count%en.shooting_intervall == 0:
                    self.bullet_list.append(shot.Shot(en.direction, en.center_x, en.center_y))
        for l in self.get_lists():
            l.update()