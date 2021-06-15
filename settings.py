from pygame_utilities import *
import os
import random as r
import time
import datetime
from uuid import uuid4

pg.init()

os.environ['SDL_VIDEO_CENTERED'] = '1'
pg.display.set_caption('NoDungeonRPG')
disp_w, disp_h = 1024, 768
screen = pg.display.set_mode([disp_w, disp_h])
default_clock = 60
timer = 0
cursor = 'data/images/gui/cursor24.png'
mouse_pos = (0, 0)
tile_w, tile_h = 64, 64

current_game = {
		'date_time': None,
		'settings': {'sound_active': True, 'gui_bg_option': 1},
		'current_char': None,
		'current_map': None,
		'blocking_objs': [],
		'current_container': None,
		'current_creature': None,
		'previous_container': None,
		'skills': None,
		'equipped': {'helm': None, 'weapon': None, 'gloves': None, 'pants': None, 'boots': None, 'necklace': None,
		             'bag':  None, 'shoulder': None, 'armor': None, 'ring': None, 'shield': None, 'belt': None},
		'inv_items': generate_grid_status((6, 6), default_value=None)}

save_sockets = {'save_game1': None, 'save_game2': None, 'save_game3': None, 'save_game4': None}

active_screen = 'game'
focused_gui_win = None

# Colors RGB #
col_black, col_white, col_red, col_green_lime, col_blue, col_purple, col_gold, col_green,\
	col_yellow, col_blue_navy, col_grey, col_dark_red = \
	(0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255), (128, 0, 128), (218, 165, 32), (0, 128, 0),\
	(255, 255, 0), (0, 0, 128), (128, 128, 128), (128, 0, 0)

# Fonts #
info_font = 'data/fonts/germania.ttf'

# Map #
# When creating a map: 'terrain' and 'climate' can be only one element each
# When creating a map_obj: 'terrain' or ''climate' can be more than 1 but always between [], even "['all']"
map_elements = {'terrain': ['sand', 'dirt', 'rock'], 'climate': ['arid', 'template', 'tropical', 'tundra']}

# House 1 => (88, 45)       >>> Block: (64, 104) (200*90)       >>> Base: 267       >>> Size: 271*222
# House 2 => (367, 26)
# House 3 => (345, 45)
# House 4 => (263, 179)
# House 5 => (143, 367)
# House 6 => (699, 179)
# Tower => (575, 414)
# Well => (453, 229)

# Tile => 64*64
