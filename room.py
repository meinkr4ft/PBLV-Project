class Room:
    """
    This class holds all the information about the
    different rooms.
    """

    def __init__(self):
        # You may want many lists. Lists for coins, monsters, etc.
        self.wall_list = None
        self.hazard_list = None
        self.enemy_list = None

        # This holds the background images. If you don't want changing
        # background images, you can delete this part.
        self.background = None