import pygame as pg
from pygame_utilities import mouse_down, mouse_up, key_down, key_up


class Controls:
    def __init__(self, confirm_win, menu, main_menu):
        self.confirm_win = confirm_win
        self.menu = menu
        self.count_menu = 0
        self.main_menu = main_menu

        self.set_active("main_menu")

    def main(self, event):
        if event.type == pg.QUIT:
            self.confirm_win.set_mode('quit')
            self.confirm_win.active = True

        self.ctrl_main_menu(event)
        self.ctrl_menu(event)
        self.ctrl_confirm_win(event)

        self.reset_btns(event)

    def set_active(self, win=None):
        self.main_menu.active = False
        # self.ingame.active = False

        if win == 'main_menu':
            self.menu.mode = 'main_menu'
            self.main_menu.active = True
        elif win == 'ingame':
            self.menu.mode = 'ingame'
            # self.ingame.active = True

    def reset_btns(self, event):
        if mouse_up(event, 1):
            for btn in self.main_menu.btns.values():
                btn.pressed = False

            for btn in self.menu.sockets_load["bg"].values():
                btn.pressed = False
            self.menu.btn_back.pressed = False

            for btn in self.confirm_win.btns.values():
                btn.pressed = False

    def ctrl_main_menu(self, event):
        if self.main_menu.active:
            if mouse_down(event, 1, self.main_menu.btns["continue"].rect):
                self.main_menu.btns["continue"].pressed = True
            if self.main_menu.btns["continue"].pressed:
                if mouse_up(event, 1, self.main_menu.btns["continue"].rect):
                    self.main_menu.btns["continue"].pressed = False
                    self.main_menu.draw_buttons()
                    self.menu.layer = "load"
                    self.menu.active = True

            if mouse_down(event, 1, self.main_menu.btns["new_game"].rect):
                self.main_menu.btns["new_game"].pressed = True
            if self.main_menu.btns["new_game"].pressed:
                if mouse_up(event, 1, self.main_menu.btns["new_game"].rect):
                    self.main_menu.btns["new_game"].pressed = False
                    self.main_menu.draw_buttons()
                    self.menu.layer = "new_game"
                    self.menu.active = True

            if mouse_down(event, 1, self.main_menu.btns["settings"].rect):
                self.main_menu.btns["settings"].pressed = True
            if self.main_menu.btns["settings"].pressed:
                if mouse_up(event, 1, self.main_menu.btns["settings"].rect):
                    self.main_menu.btns["settings"].pressed = False
                    self.main_menu.draw_buttons()
                    self.menu.layer = "settings"
                    self.menu.active = True

            if mouse_down(event, 1, self.main_menu.btns["quit"].rect):
                self.main_menu.btns["quit"].pressed = True
            if self.main_menu.btns["quit"].pressed:
                if mouse_up(event, 1, self.main_menu.btns["quit"].rect):
                    self.main_menu.btns["quit"].pressed = False
                    self.main_menu.draw_buttons()
                    self.confirm_win.set_mode('quit')
                    self.confirm_win.active = True

    def ctrl_menu(self, event):
        if self.menu.active:
            if self.menu.mode == 'main_menu':
                # if IOMouseHover.mouse_hover(sett.mouse_pos, self.menu.btn_back.rect):
                #     self.menu.btn_back.hovering = True
                # else:
                #     self.menu.btn_back.hovering = False
                if self.menu.layer == "load":
                    for key, socket in self.menu.sockets_load["bg"].items():
                        if mouse_down(event, 1, socket):
                            socket.pressed = True
                        if socket.pressed:
                            if mouse_up(event, 1, socket):
                                # Añadir aquí la carga del juego correspondiente
                                pass
                    if mouse_down(event, 1, self.menu.btn_back):
                        self.menu.btn_back.pressed = True
                    if self.menu.btn_back.pressed:
                        if mouse_up(event, 1, self.menu.btn_back):
                            self.menu.layer = None
                            self.menu.active = False
                elif self.menu.layer == "new_game":
                    if mouse_down(event, 1, self.menu.btn_back):
                        self.menu.btn_back.pressed = True
                    if self.menu.btn_back.pressed:
                        if mouse_up(event, 1, self.menu.btn_back):
                            self.menu.layer = None
                            self.menu.active = False
                elif self.menu.layer == "settings":
                    if mouse_down(event, 1, self.menu.btn_back):
                        self.menu.btn_back.pressed = True
                    if self.menu.btn_back.pressed:
                        if mouse_up(event, 1, self.menu.btn_back):
                            self.menu.layer = None
                            self.menu.active = False
            elif self.menu.mode == 'ingame':
                pass

            if key_down(event, pg.K_ESCAPE):
                self.menu.layer = None
                self.menu.active = False

    def ctrl_confirm_win(self, event):
        if self.confirm_win.active:
            if self.confirm_win.mode == 'main_menu':
                pass
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
                        self.confirm_win.active = False
