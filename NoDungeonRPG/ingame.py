import pygame as pg
import general as gral


class InGame:
    def __init__(self):
        self.img_gui_bg = pg.image.load('data/images/gui/guis/gui_bg1.png').convert_alpha()

    def display(self):
        # gral.scr.blit(self.img_gui_bg, (0, 0))
        gral.map.display()
