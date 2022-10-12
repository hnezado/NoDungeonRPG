# TODO bugs to fix:

# Fix loot generation based on creature or container modifiers
# Add friendly attitude
# Separate Title from main menu bg image (?)

### IDEAS ###

# Spirit bar can be filled killing creatures or completing actions/requests
# There is a slight chance to learn or improve a magic_skill or ability during meditation

# Vigor is used in every action: (crafting, mining, gathering, fishing, reading...(not combat))

# Food can be found around: fishing, gathering plants or meat (better quality if you cook it)
# Food regenerates hp, mp, and maybe vigor (all with time) and boosts the comfort*

## ADVANCED ##
# Comfort is affected by some factors like campfire creation, well feeding, bad weather...
# A high level of comfort enhances the meditating/sleeping results

# Trees, mining veins, writings (ancient runes), fishing spots, artifacts studying require learn abilities (non-magic)
# and there is a chance to improve known abilities when those actions finish successfully

# There is not a fixed currency to trade with. If any, trades are based on logrolling (favors) and bartering.
# Crux (essence) can be obtained from almost everything you find, and this can be used to craft or enhance objects.
# Crux can be reduced/divided to the most elemental or combined to get a more complex one.
# A special device (Cruxer) is required to divide or combine crux, and knowledge is required to do that.
# Cruxer parts are found along the story. They can be combined to obtain the full device (It may require some knowledge)
# The Cruxer can be upgraded somehow to divide or combine more complex crux.

# from controls import MainMenu

# gen_item(iclass='ragged_bandana', iqual='unique').pick_item()
# gen_item(iclass='fist_knife', iqual='rare').equip()


# def refresh_controls():
#     """Detects if any action takes place"""
#
#     if IOAtlas.fading["transition"] != "in":
#         if not any(pg.key.get_pressed()):
#             sett.current_game["current_char"].stop_movement()
#
#     if not any(pg.mouse.get_pressed()):
#         IOEqu.gui_button.pressed = False
#         IOEqu.close_pressed = False
#         IOEqu.move_win_pressed = False
#         IOInv.gui_button.pressed = False
#         IOInv.close_pressed = False
#         IOInv.move_win_pressed = False
#         IOLootCombat.close_pressed = False
#         IOLootCombat.move_win_pressed = False
#         IOLootContainer.close_pressed = False
#         IOLootContainer.move_win_pressed = False
#         IOGUI.ingame_menu_button.pressed = False
#         IOGUI.menu_but["resume"].pressed = False
#         IOGUI.menu_but["save"].pressed = False
#         IOGUI.menu_but["load"].pressed = False
#         IOGUI.menu_but["settings"].pressed = False
#         IOGUI.menu_but["main_menu"].pressed = False
#         if IOGUI.menu_active:
#             for socket in IOGUI.menu_but["save_game_buttons"].keys():
#                 IOGUI.menu_but["save_game_buttons"][socket].pressed = False
#                 IOGUI.menu_but["delete_game"][socket].pressed = False
#             for socket in IOGUI.menu_but["load_game_buttons"].keys():
#                 IOGUI.menu_but["load_game_buttons"][socket].pressed = False
#         IOGUI.menu_but["sound_on"].pressed = False
#         IOGUI.menu_but["sound_off"].pressed = False
#         IOGUI.menu_but["back"].pressed = False
#         IOItem.item_drag = False
#         IOCombat.button_attack.pressed = False
#         IOCombat.button_cast.pressed = False
#         IOCombat.button_item.pressed = False
#         IOCombat.button_retreat.pressed = False
#         IOCombat.button_back.pressed = False
#
#
# def game():
#     """Displays every ingame element on the screen"""

#     if sett.active_screen == "game":
#         sett.current_game["current_map"].draw_map()
#         IOGUI.draw_gui()
#         IOCombat.draw_combat()
#         IOGUI.draw_menu()
#         IOAtlas.check_transition()

from pygame_utilities import clock
from cursor import *
from confirm_win import ConfirmWindow
from menu import Menu
from main_menu import MainMenu
from ingame import InGame
from controls import Controls
import pygame as pg
import json
import os
import pickle
import general as gral


def update(files=None, mode='r'):
    """Maintains updated some global variables"""

    if mode == "r" or mode == "read":
        if files:
            if 'settings' in files:
                gral.settings = load_settings()
            if 'games' in files:
                gral.saved_games = load_games()
        else:
            gral.controls.check_states()
    elif mode == "w" or mode == "write":
        if files:
            if 'settings' in files:
                with open('config/settings.json', 'w') as j:
                    json.dump(gral.settings, j)
            if 'games' in files:
                with open('../saves/', 'w') as j:
                    json.dump(gral.settings, j)
    else:
        raise ValueError("Value must be either read or write modes ('r' or 'w')")


def load_settings():
    """Loads the settings file content"""

    with open('config/settings.json') as j:
        return json.load(j)


def load_games():
    """Loads the saved game files content"""

    games = {num: None for num in range(1, 5)}
    for game_save in os.listdir("../saves"):
        try:
            with open(f"../saves/{game_save}", "rb") as g:
                games[int(game_save.split(".dgn")[0][-1])] = pickle.load(g)
        except PermissionError:
            pass

    return games


if __name__ == "__main__":

    update(files=['settings', 'games'])

    gral.cursor = Cursor()
    gral.cursor.set_img("data/images/gui/cursor24.png")
    gral.confirm_win = ConfirmWindow()
    gral.menu = Menu()
    gral.main_menu = MainMenu()
    gral.ingame = InGame()
    gral.controls = Controls(update)

    gral.menu.update_btns()

    from pygame_utilities import text, merge_surfaces

    print('saved_games:', gral.saved_games)

    while True:

        for event in pg.event.get():
            gral.controls.main(event)
        update()

        # gral.ingame.display()
        gral.main_menu.display()
        gral.menu.display()
        gral.confirm_win.display()

        gral.cursor.display()

        pg.display.update()
        clock(gral.default_clock)

        # sett.timer = pg.time.get_ticks()

        # refresh_controls()
