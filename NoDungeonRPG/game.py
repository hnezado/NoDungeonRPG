from pygame_utilities import generate_grid_status


class Game:
    def __init__(self):
        self.socket = 0
        self.date_time = None
        self.current_char = None
        self.current_map = None
        self.blocking_objs = []
        self.current_container = None
        self.current_creature = None
        self.previous_container = None
        self.skills = None
        self.equipped = {
            "helm": None,
            "weapon": None,
            "gloves": None,
            "pants": None,
            "boots": None,
            "necklace": None,
            "bag": None,
            "shoulder": None,
            "armor": None,
            "ring": None,
            "shield": None,
            "belt": None,
        }
        self.inv_items = generate_grid_status((6, 6), default_value=None)

    def save(self):
        pass

    def load(self):
        pass
