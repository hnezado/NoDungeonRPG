from pygame_utilities import MouseHover, mouse_down, mouse_up, key_down
import pygame as pg
import json
import general as gral


class Controls:
    def __init__(self):
        self.hovering_objs = []

        self.settings_upd = False
        self.saved_games_upd = False
        self.set_active("main_menu")

    def is_hovering(self, mouse_pos, hvr_rect, ms=0):
        """Creates MouseHover instance for the rect (if not created) and checks if the rect has a MouseHover instance"""

        if hvr_rect not in [rct for rct, obj in self.hovering_objs]:
            self.hovering_objs.append((hvr_rect, MouseHover()))

        obj = list(filter(lambda x: x[0] == hvr_rect, self.hovering_objs))[0][1]
        return obj.hover(mouse_pos, hvr_rect, ms)

    def check_states(self):
        """Checks event non-related states (hovering)"""

        if gral.menu.active and not gral.confirm_win.active:
            if gral.menu.layer == "load":
                if self.is_hovering(gral.cursor.pos, gral.menu.btns["back"].rect):
                    gral.menu.btns["back"].hovering = True
                else:
                    gral.menu.btns["back"].hovering = False
            elif gral.menu.layer == "save":
                if self.is_hovering(gral.cursor.pos, gral.menu.btns["back"].rect):
                    gral.menu.btns["back"].hovering = True
                else:
                    gral.menu.btns["back"].hovering = False
            elif gral.menu.layer == "settings":
                if gral.settings["sound"] == "enabled":
                    if self.is_hovering(gral.cursor.pos, gral.menu.btns["settings"]["sound"]["enabled"].rect):
                        gral.menu.btns["settings"]["sound"]["enabled"].hovering = True
                    else:
                        gral.menu.btns["settings"]["sound"]["enabled"].hovering = False
                elif gral.settings["sound"] == "disabled":
                    if self.is_hovering(gral.cursor.pos, gral.menu.btns["settings"]["sound"]["disabled"].rect):
                        gral.menu.btns["settings"]["sound"]["disabled"].hovering = True
                    else:
                        gral.menu.btns["settings"]["sound"]["disabled"].hovering = False
                if self.is_hovering(gral.cursor.pos, gral.menu.btns["back"].rect):
                    gral.menu.btns["back"].hovering = True
                else:
                    gral.menu.btns["back"].hovering = False
        #
        # if self.ingame.ingame_upd:

    def check_updates(self):
        """Checks if some global variables should be updated (non-event related)"""

        updates = []
        if self.settings_upd:
            self.settings_upd = False
            updates.append("settings")
        if self.saved_games_upd:
            self.saved_games_upd = False
            updates.append("saved_games")
        return updates

    def main(self, event):
        """Main controls manager"""

        gral.cursor.pos = pg.mouse.get_pos()

        if event.type == pg.QUIT:
            pg.quit()
            quit()

        self.ctrl_confirm_win(event)
        self.ctrl_menu(event)
        self.ctrl_main_menu(event)

        self.reset_btns(event)

    @staticmethod
    def set_active(win=None):
        gral.main_menu.active = False
        gral.ingame.active = False

        if win == 'main_menu':
            gral.main_menu.active = True
        elif win == 'ingame':
            gral.ingame.active = True
            pass

    def set_settings(self, setting):
        if setting == "sound_switch":
            gral.menu.switch_sound()

        with open('config/settings.json', 'w') as j:
            json.dump(gral.settings, j)

        self.settings_upd = True

    @staticmethod
    def reset_btns(event):
        if mouse_up(event, 1):
            for btn in gral.main_menu.btns.values():
                btn.pressed = False
            gral.main_menu.draw_buttons()

            for btn in gral.menu.btns["load"]["bg"]["existent"].values():
                btn.pressed = False
            for btn in gral.menu.btns["settings"]["sound"].values():
                btn.pressed = False
            gral.menu.btns["back"].pressed = False

            for btn in gral.confirm_win.btns.values():
                btn.pressed = False

    def ctrl_confirm_win(self, event):
        if gral.confirm_win.active:
            if gral.confirm_win.mode == 'main_menu':
                if mouse_down(event, 1, gral.confirm_win.btns['accept']):
                    gral.confirm_win.btns['accept'].pressed = True
                if gral.confirm_win.btns['accept'].pressed:
                    if mouse_up(event, 1, gral.confirm_win.btns['accept']):
                        gral.current_game = None
                        self.set_active("main_menu")
            elif gral.confirm_win.mode == 'load':
                if mouse_down(event, 1, gral.confirm_win.btns['accept']):
                    gral.confirm_win.btns['accept'].pressed = True
                if gral.confirm_win.btns['accept'].pressed:
                    if mouse_up(event, 1, gral.confirm_win.btns['accept']):
                        gral.current_game = gral.saved_games[gral.confirm_win.temp_kwargs["socket"]]
                        gral.confirm_win.clear_temp_kwargs()
                        self.set_active("ingame")
            elif gral.confirm_win.mode == "save":
                if mouse_down(event, 1, gral.confirm_win.btns['accept']):
                    gral.confirm_win.btns['accept'].pressed = True
                if gral.confirm_win.btns['accept'].pressed:
                    if mouse_up(event, 1, gral.confirm_win.btns['accept']):
                        gral.saved_games[gral.confirm_win.temp_kwargs["socket"]] = gral.current_game
                        gral.confirm_win.clear_temp_kwargs()
                        self.saved_games_upd = True
            elif gral.confirm_win.mode == 'new_game':
                if mouse_down(event, 1, gral.confirm_win.btns['accept']):
                    gral.confirm_win.btns['accept'].pressed = True
                if gral.confirm_win.btns['accept'].pressed:
                    if mouse_up(event, 1, gral.confirm_win.btns['accept']):
                        gral.menu.new_game()
                        self.saved_games_upd = True
                        gral.confirm_win.close()
            elif gral.confirm_win.mode == 'quit':
                if mouse_down(event, 1, gral.confirm_win.btns['accept']):
                    gral.confirm_win.btns['accept'].pressed = True
                if gral.confirm_win.btns['accept'].pressed:
                    if mouse_up(event, 1, gral.confirm_win.btns['accept']):
                        pg.quit()
                        quit()
            if mouse_down(event, 1, gral.confirm_win.btns['cancel']):
                gral.confirm_win.btns['cancel'].pressed = True
            if gral.confirm_win.btns['cancel'].pressed:
                if mouse_up(event, 1, gral.confirm_win.btns['cancel']):
                    gral.confirm_win.close()

    def ctrl_menu(self, event):
        if gral.menu.active and not gral.confirm_win.active:
            if gral.menu.layer == "main":
                pass
            elif gral.menu.layer == "load":
                for key, socket_btn in gral.menu.btns["load"]["bg"]["existent"].items():
                    if gral.saved_games[key]:
                        if mouse_down(event, 1, socket_btn):
                            socket_btn.pressed = True
                        if socket_btn.pressed:
                            if mouse_up(event, 1, socket_btn):
                                gral.confirm_win.open("load", socket=key)
                if mouse_down(event, 1, gral.menu.btns["back"]):
                    gral.menu.btns["back"].pressed = True
                if gral.menu.btns["back"].pressed:
                    if mouse_up(event, 1, gral.menu.btns["back"]):
                        gral.menu.close()
            elif gral.menu.layer == "save":
                pass
            elif gral.menu.layer == "settings":

                # Sound settings
                if mouse_down(event, 1, gral.menu.btns["settings"]["sound"]["enabled"]):
                    if gral.settings["sound"] == "enabled":
                        gral.menu.btns["settings"]["sound"]["enabled"].pressed = True
                    elif gral.settings["sound"] == "disabled":
                        gral.menu.btns["settings"]["sound"]["disabled"].pressed = True
                if gral.menu.btns["settings"]["sound"]["enabled"].pressed:
                    if mouse_up(event, 1, gral.menu.btns["settings"]["sound"]["enabled"]):
                        self.set_settings("sound_switch")
                if gral.menu.btns["settings"]["sound"]["disabled"].pressed:
                    if mouse_up(event, 1, gral.menu.btns["settings"]["sound"]["disabled"]):
                        self.set_settings("sound_switch")

                if mouse_down(event, 1, gral.menu.btns["back"]):
                    gral.menu.btns["back"].pressed = True
                if gral.menu.btns["back"].pressed:
                    if mouse_up(event, 1, gral.menu.btns["back"]):
                        gral.menu.close()

            if key_down(event, pg.K_ESCAPE):
                gral.menu.layer = None
                gral.menu.active = False

    @staticmethod
    def ctrl_main_menu(event):
        if gral.main_menu.active and not gral.confirm_win.active:
            if mouse_down(event, 1, gral.main_menu.btns["continue"].rect):
                gral.main_menu.btns["continue"].pressed = True
            if gral.main_menu.btns["continue"].pressed:
                if mouse_up(event, 1, gral.main_menu.btns["continue"].rect):
                    gral.menu.open("load")

            if mouse_down(event, 1, gral.main_menu.btns["new_game"].rect):
                gral.main_menu.btns["new_game"].pressed = True
            if gral.main_menu.btns["new_game"].pressed:
                if mouse_up(event, 1, gral.main_menu.btns["new_game"].rect):
                    gral.confirm_win.open("new_game")

            if mouse_down(event, 1, gral.main_menu.btns["settings"].rect):
                gral.main_menu.btns["settings"].pressed = True
            if gral.main_menu.btns["settings"].pressed:
                if mouse_up(event, 1, gral.main_menu.btns["settings"].rect):
                    gral.menu.open("settings")

            if mouse_down(event, 1, gral.main_menu.btns["quit"].rect):
                gral.main_menu.btns["quit"].pressed = True
            if gral.main_menu.btns["quit"].pressed:
                if mouse_up(event, 1, gral.main_menu.btns["quit"].rect):
                    gral.confirm_win.open('quit')
