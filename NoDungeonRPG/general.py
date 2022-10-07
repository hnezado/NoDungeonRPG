import pygame as pg
import os

font = {
    "info": "data/fonts/germania.ttf"
        }
color = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "red": (255, 0, 0),
    "green_lime": (0, 255, 0),
    "blue": (0, 0, 255),
    "purple": (128, 0, 128),
    "gold": (218, 165, 32),
    "green": (0, 128, 0),
    "yellow": (255, 255, 0),
    "blue_navy": (0, 0, 128),
    "grey": (128, 128, 128),
    "dark_red": (128, 0, 0),
}

pg.init()

os.environ["SLD_VIDEO_CENTERED"] = "1"
pg.display.set_caption("NoDungeonRPG")
scr_dim = [1024, 768]
scr = pg.display.set_mode(scr_dim)

default_clock = 60
timer = 0  # Necesario?

cursor = None
settings = None
saved_games = None
current_game = None

confirm_win = None
menu = None
main_menu = None
ingame = None
controls = None
