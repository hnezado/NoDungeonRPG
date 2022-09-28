import pygame as pg
from pygame_utilities import mouse_down, mouse_up, key_down, key_up


class Controls:
    def __init__(self, menu, main_menu):
        self.menu = menu
        self.count_menu = 0
        self.main_menu = main_menu

    def main(self, event):
        if event.type == pg.QUIT:
            pg.quit()
            quit()

        self.ctrl_menu(event)
        self.ctrl_main_menu(event)

        self.reset_btns(event)

    def set_active(self, win=None):
        self.main_menu.active = False

        if win == 'main_menu':
            self.main_menu.active = True

    def reset_btns(self, event):
        if mouse_up(event, 1):
            self.menu.btn_back.pressed = False

    def ctrl_menu(self, event):
        if self.menu.active:
            # if IOMouseHover.mouse_hover(sett.mouse_pos, self.menu.btn_back.rect):
            #     self.menu.btn_back.hovering = True
            # else:
            #     self.menu.btn_back.hovering = False
            if self.menu.layer in ["load", "new_game", "settings"]:
                if mouse_down(event, 1, self.menu.btn_back):
                    self.menu.btn_back.pressed = True
                if self.menu.btn_back.pressed:
                    if mouse_up(event, 1, self.menu.btn_back):
                        self.menu.layer = ""
                        self.set_active("main_menu")

                if key_down(event, pg.K_ESCAPE):
                    self.menu.layer = ""
                    self.set_active("main_menu")

    def ctrl_main_menu(self, event):
        if self.main_menu.active:
            if mouse_down(event, 1, self.main_menu.btns["continue"].rect):
                self.main_menu.btns["continue"].pressed = True
            if self.main_menu.btns["continue"].pressed:
                if mouse_up(event, 1, self.main_menu.btns["continue"].rect):
                    self.main_menu.btns["continue"].pressed = False
                    self.main_menu.draw_buttons()
                    self.set_active("menu")
                    self.menu.layer = "load"

            if mouse_down(event, 1, self.main_menu.btns["new_game"].rect):
                self.main_menu.btns["new_game"].pressed = True
            if self.main_menu.btns["new_game"].pressed:
                if mouse_up(event, 1, self.main_menu.btns["new_game"].rect):
                    self.main_menu.btns["new_game"].pressed = False
                    self.main_menu.draw_buttons()
                    self.set_active("menu")
                    self.menu.layer = "new_game"

            if mouse_down(event, 1, self.main_menu.btns["settings"].rect):
                self.main_menu.btns["settings"].pressed = True
            if self.main_menu.btns["settings"].pressed:
                if mouse_up(event, 1, self.main_menu.btns["settings"].rect):
                    self.main_menu.btns["settings"].pressed = False
                    self.main_menu.draw_buttons()
                    self.set_active("menu")
                    self.menu.layer = "settings"

            if mouse_down(event, 1, self.main_menu.btns["quit"].rect):
                self.main_menu.btns["quit"].pressed = True
            if self.main_menu.btns["quit"].pressed:
                if mouse_up(event, 1, self.main_menu.btns["quit"].rect):
                    self.main_menu.btns["quit"].pressed = False
                    self.main_menu.draw_buttons()
                    # temporal (needs confirmation)
                    pg.quit()
                    quit()

            if mouse_up(event, 1):
                for btn in self.main_menu.btns.keys():
                    self.main_menu.btns[btn].pressed = False

