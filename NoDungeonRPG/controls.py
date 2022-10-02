import pygame as pg
import json
from pygame_utilities import mouse_down, mouse_up
from pygame_utilities import key_down, key_up
from pygame_utilities import MouseHover


class Controls:
    def __init__(self, cursor, confirm_win, menu, main_menu, settings):
        self._mouse_pos = (0, 0)

        self.cursor = cursor
        self.confirm_win = confirm_win
        self.menu = menu
        self.main_menu = main_menu
        self.settings = settings

        self.hovering_objs = []

        self.settings_change = False
        self.set_active("main_menu")

    @property
    def mouse_pos(self):
        return self._mouse_pos

    @mouse_pos.setter
    def mouse_pos(self, value):
        if type(value) == tuple and len(value) == 2 \
                and len([i for i in value if type(i) == int]) == 2:
            self._mouse_pos = value
        else:
            raise ValueError('Value must be a 2 integers tuple')

    def is_hovering(self, mouse_pos, hvr_rect, ms=0):
        if hvr_rect not in [rct for rct, obj in self.hovering_objs]:
            self.hovering_objs.append((hvr_rect, MouseHover()))

        obj = list(filter(lambda x: x[0] == hvr_rect, self.hovering_objs))[0][1]
        return obj.hover(mouse_pos, hvr_rect, ms)

    def check_states(self):
        """Checks the states even when there are no events (settings, hovering)"""

        if self.menu.active and not self.confirm_win.active:
            if self.menu.layer == "load":
                if self.is_hovering(self.mouse_pos, self.menu.btns["back"].rect):
                    self.menu.btns["back"].hovering = True
                else:
                    self.menu.btns["back"].hovering = False
            elif self.menu.layer == "save":
                if self.is_hovering(self.mouse_pos, self.menu.btns["back"].rect):
                    self.menu.btns["back"].hovering = True
                else:
                    self.menu.btns["back"].hovering = False
            elif self.menu.layer == "settings":
                if self.settings["sound"] == "enabled":
                    if self.is_hovering(self.mouse_pos, self.menu.btns["settings"]["sound"]["enabled"].rect):
                        self.menu.btns["settings"]["sound"]["enabled"].hovering = True
                    else:
                        self.menu.btns["settings"]["sound"]["enabled"].hovering = False
                elif self.settings["sound"] == "disabled":
                    if self.is_hovering(self.mouse_pos, self.menu.btns["settings"]["sound"]["disabled"].rect):
                        self.menu.btns["settings"]["sound"]["disabled"].hovering = True
                    else:
                        self.menu.btns["settings"]["sound"]["disabled"].hovering = False
                if self.is_hovering(self.mouse_pos, self.menu.btns["back"].rect):
                    self.menu.btns["back"].hovering = True
                else:
                    self.menu.btns["back"].hovering = False

        if self.settings_change:
            self.settings_change = False
            return True

    def main(self, event):
        self.mouse_pos = pg.mouse.get_pos()
        self.cursor.pos = self.mouse_pos

        if event.type == pg.QUIT:
            self.confirm_win.open('quit')

        self.ctrl_main_menu(event)
        self.ctrl_menu(event)
        self.ctrl_confirm_win(event)

        self.reset_btns(event)

    def set_active(self, win=None):
        self.main_menu.active = False
        # self.ingame.active = False

        if win == 'main_menu':
            self.main_menu.active = True
        elif win == 'ingame':
            # self.ingame.active = True
            pass

    def set_settings(self, setting):
        if setting == "sound_switch":
            self.menu.switch_sound()

        with open('config/settings.json', 'w') as j:
            json.dump(self.settings, j)

        self.settings_change = True

    def reset_btns(self, event):
        if mouse_up(event, 1):
            for btn in self.main_menu.btns.values():
                btn.pressed = False
            self.main_menu.draw_buttons()

            for btn in self.menu.btns["load"]["bg"].values():
                btn.pressed = False
            for btn in self.menu.btns["settings"]["sound"].values():
                btn.pressed = False
            self.menu.btns["back"].pressed = False

            for btn in self.confirm_win.btns.values():
                btn.pressed = False

    def ctrl_confirm_win(self, event):
        if self.confirm_win.active:
            if self.confirm_win.mode == 'main_menu':
                pass
            elif self.confirm_win.mode == 'new_game':
                if mouse_down(event, 1, self.confirm_win.btns['accept']):
                    self.confirm_win.btns['accept'].pressed = True
                if self.confirm_win.btns['accept'].pressed:
                    if mouse_up(event, 1, self.confirm_win.btns['accept']):
                        self.confirm_win.close()

                if mouse_down(event, 1, self.confirm_win.btns['cancel']):
                    self.confirm_win.btns['cancel'].pressed = True
                if self.confirm_win.btns['cancel'].pressed:
                    if mouse_up(event, 1, self.confirm_win.btns['cancel']):
                        self.confirm_win.close()

            elif self.confirm_win.mode == 'quit':
                if mouse_down(event, 1, self.confirm_win.btns['accept']):
                    self.confirm_win.btns['accept'].pressed = True
                if self.confirm_win.btns['accept'].pressed:
                    if mouse_up(event, 1, self.confirm_win.btns['accept']):
                        pg.quit()
                        quit()

                if mouse_down(event, 1, self.confirm_win.btns['cancel']):
                    self.confirm_win.btns['cancel'].pressed = True
                if self.confirm_win.btns['cancel'].pressed:
                    if mouse_up(event, 1, self.confirm_win.btns['cancel']):
                        self.confirm_win.close()

    def ctrl_menu(self, event):
        if self.menu.active and not self.confirm_win.active:
            if self.menu.layer == "main":
                pass
            elif self.menu.layer == "load":
                for key, socket in self.menu.btns["load"]["bg"].items():
                    if mouse_down(event, 1, socket):
                        socket.pressed = True
                    if socket.pressed:
                        if mouse_up(event, 1, socket):
                            # Añadir aquí la carga del juego correspondiente
                            pass
                if mouse_down(event, 1, self.menu.btns["back"]):
                    self.menu.btns["back"].pressed = True
                if self.menu.btns["back"].pressed:
                    if mouse_up(event, 1, self.menu.btns["back"]):
                        self.menu.close()
            elif self.menu.layer == "save":
                pass
            elif self.menu.layer == "settings":

                # Sound settings
                if mouse_down(event, 1, self.menu.btns["settings"]["sound"]["enabled"]):
                    if self.settings["sound"] == "enabled":
                        self.menu.btns["settings"]["sound"]["enabled"].pressed = True
                    elif self.settings["sound"] == "disabled":
                        self.menu.btns["settings"]["sound"]["disabled"].pressed = True
                if self.menu.btns["settings"]["sound"]["enabled"].pressed:
                    if mouse_up(event, 1, self.menu.btns["settings"]["sound"]["enabled"]):
                        self.set_settings("sound_switch")
                if self.menu.btns["settings"]["sound"]["disabled"].pressed:
                    if mouse_up(event, 1, self.menu.btns["settings"]["sound"]["disabled"]):
                        self.set_settings("sound_switch")

                if mouse_down(event, 1, self.menu.btns["back"]):
                    self.menu.btns["back"].pressed = True
                if self.menu.btns["back"].pressed:
                    if mouse_up(event, 1, self.menu.btns["back"]):
                        self.menu.close()

            if key_down(event, pg.K_ESCAPE):
                self.menu.layer = None
                self.menu.active = False

    def ctrl_main_menu(self, event):
        if self.main_menu.active and not self.confirm_win.active:
            if mouse_down(event, 1, self.main_menu.btns["continue"].rect):
                self.main_menu.btns["continue"].pressed = True
            if self.main_menu.btns["continue"].pressed:
                if mouse_up(event, 1, self.main_menu.btns["continue"].rect):
                    self.menu.open("load")

            if mouse_down(event, 1, self.main_menu.btns["new_game"].rect):
                self.main_menu.btns["new_game"].pressed = True
            if self.main_menu.btns["new_game"].pressed:
                if mouse_up(event, 1, self.main_menu.btns["new_game"].rect):
                    self.confirm_win.open("new_game")

            if mouse_down(event, 1, self.main_menu.btns["settings"].rect):
                self.main_menu.btns["settings"].pressed = True
            if self.main_menu.btns["settings"].pressed:
                if mouse_up(event, 1, self.main_menu.btns["settings"].rect):
                    self.menu.open("settings")

            if mouse_down(event, 1, self.main_menu.btns["quit"].rect):
                self.main_menu.btns["quit"].pressed = True
            if self.main_menu.btns["quit"].pressed:
                if mouse_up(event, 1, self.main_menu.btns["quit"].rect):
                    self.confirm_win.open('quit')
