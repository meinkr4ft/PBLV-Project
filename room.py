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
        return ret
