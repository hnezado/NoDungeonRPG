from pygame_utilities import *


class Menu:
    def __init__(self):
        self.img_bg = pg.image.load('data/images/gui/menu_bg.png').convert_alpha()
        self.img_save_game = Sheet('data/images/gui/save_game.png', (5, 1))
        self.img_delete_game = Sheet('data/images/gui/delete_game.png', (3, 1))

    def display(self):
        pass

    def load(self):
        pass

    def new_game(self):
        pass

    def settings(self):
        pass

    def quit(self):
        pass
