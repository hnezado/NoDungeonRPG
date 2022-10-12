from pygame_utilities import Sheet, text, merge_surfaces, Button, readable_text
from game import Game
import pygame as pg
import pickle
import general as gral


class Menu:
    def __init__(self):
        self.imgs = {
            "bg": pg.image.load("data/images/menu/bg.png").convert_alpha(),
            "btns": {
                "saved_games": Sheet("data/images/menu/saved_games.png", (5, 1)),
                "delete_game": Sheet("data/images/menu/delete_game.png", (3, 1)),
                "back": text("Back", font_style=gral.font["info"], font_size=30, color=gral.color["black"])[0],
                "sound": {
                    "enabled": text('Sound on', font_style=gral.font["info"], font_size=30, color=gral.color["green"])[0],
                    "disabled": text('Sound off', font_style=gral.font["info"], font_size=30, color=gral.color["red"])[0]
                },
                "resume": text("Resume", font_style=gral.font["info"], font_size=30, color=gral.color["black"])[0],
            },
        }

        self.pos = (gral.scr_dim[0] * .5 - self.imgs["bg"].get_width() * .5,
                    gral.scr_dim[1] * .5 - self.imgs["bg"].get_height() * .5)
        self.rect = self.imgs["bg"].get_rect()

        self._active = False
        self._layer = None

        self.btns = None
        self.update_btns()

        # self.ingame_menu_button = Button(self.screen, bg=self.img_but_bg150_sh, icon=self.img_but_icon_ingame_menu,
        #                                  sheet_index=0, pos=(850, 694))
        # self.menu_layer = 'main'
        # self.menu_rect = self.img_menu_bg.get_rect()
        # self.menu_but_imgs = {'resume': text('Resume', font_style=info_font, font_size=30, color=col_black)[0],
        #                       'save': text('Save', font_style=info_font, font_size=30, color=col_black)[0],
        #                       'load': text('Load', font_style=info_font, font_size=30, color=col_black)[0],
        #                       'settings': text('Settings', font_style=info_font, font_size=30, color=col_black)[0],
        #                       'main_menu': text('Main menu', font_style=info_font, font_size=30, color=col_black)[0],
        #                       'load_game': text('Load game', font_style=info_font, font_size=30, color=col_black)[0],
        #                       'sound_on': text('Sound on', font_style=info_font, font_size=30, color=col_green)[0],
        #                       'sound_off': text('Sound off', font_style=info_font, font_size=30, color=col_red)[0],
        #                       'back': text('Back', font_style=info_font, font_size=30, color=col_black)[0]
        #                       }
        # self.menu_but = {
        #     'resume': Button(
        #         self.screen, pos=self.menu_but_imgs['resume'].get_rect(
        #             center=(self.menu_pos[0] + self.menu_rect.w * 0.5, self.menu_pos[1] + self.menu_rect.h * 0.1)),
        #         hover_on=True, img=self.menu_but_imgs['resume'],
        #         img_hover=text('Resume', font_style=info_font, font_size=30, color=col_white)[0],
        #         img_pressed=text('Resume', font_style=info_font, font_size=30, color=col_grey)[0]),
        #     'save': Button(
        #         self.screen, pos=self.menu_but_imgs['save'].get_rect(
        #             center=(self.menu_pos[0] + self.menu_rect.w * 0.5, self.menu_pos[1] + self.menu_rect.h * 0.3)),
        #         hover_on=True, img=self.menu_but_imgs['save'],
        #         img_hover=text('Save', font_style=info_font, font_size=30, color=col_white)[0],
        #         img_pressed=text('Save', font_style=info_font, font_size=30, color=col_grey)[0]),
        #     'load': Button(
        #         self.screen, pos=self.menu_but_imgs['load'].get_rect(
        #             center=(self.menu_pos[0] + self.menu_rect.w * 0.5, self.menu_pos[1] + self.menu_rect.h * 0.5)),
        #         hover_on=True, img=self.menu_but_imgs['load'],
        #         img_hover=text('Load', font_style=info_font, font_size=30, color=col_white)[0],
        #         img_pressed=text('Load', font_style=info_font, font_size=30, color=col_grey)[0]),
        #     'settings': Button(
        #         self.screen, pos=self.menu_but_imgs['settings'].get_rect(
        #             center=(self.menu_pos[0] + self.menu_rect.w * 0.5, self.menu_pos[1] + self.menu_rect.h * 0.7)),
        #         hover_on=True, img=self.menu_but_imgs['settings'],
        #         img_hover=text('Settings', font_style=info_font, font_size=30, color=col_white)[0],
        #         img_pressed=text('Settings', font_style=info_font, font_size=30, color=col_grey)[0]),
        #     'main_menu': Button(
        #         self.screen, pos=self.menu_but_imgs['main_menu'].get_rect(
        #             center=(self.menu_pos[0] + self.menu_rect.w * 0.5, self.menu_pos[1] + self.menu_rect.h * 0.9)),
        #         hover_on=True, img=self.menu_but_imgs['main_menu'],
        #         img_hover=text('Main menu', font_style=info_font, font_size=30, color=col_white)[0],
        #         img_pressed=text('Main menu', font_style=info_font, font_size=30, color=col_grey)[0]),
        #     'save_game_buttons': {
        #         'save_game1': Button(
        #             self.screen, pos=(self.menu_pos[0] + self.menu_rect.w * 0.5 - self.img_save_game.crop_w * 0.5,
        #                          self.menu_pos[1] + self.menu_rect.h * 0.15 - self.img_save_game.crop_h * 0.5),
        #             img=self.img_save_game.sheet.subsurface(self.img_save_game.crops[0]),
        #             img_pressed=self.img_save_game.sheet.subsurface(self.img_save_game.crops[1])),
        #         'save_game2': Button(
        #             self.screen, pos=(self.menu_pos[0] + self.menu_rect.w * 0.5 - self.img_save_game.crop_w * 0.5,
        #                          self.menu_pos[1] + self.menu_rect.h * 0.35 - self.img_save_game.crop_h * 0.5),
        #             img=self.img_save_game.sheet.subsurface(self.img_save_game.crops[0]),
        #             img_pressed=self.img_save_game.sheet.subsurface(self.img_save_game.crops[1])),
        #         'save_game3': Button(
        #             self.screen, pos=(self.menu_pos[0] + self.menu_rect.w * 0.5 - self.img_save_game.crop_w * 0.5,
        #                          self.menu_pos[1] + self.menu_rect.h * 0.55 - self.img_save_game.crop_h * 0.5),
        #             img=self.img_save_game.sheet.subsurface(self.img_save_game.crops[0]),
        #             img_pressed=self.img_save_game.sheet.subsurface(self.img_save_game.crops[1])),
        #         'save_game4': Button(
        #             self.screen, pos=(self.menu_pos[0] + self.menu_rect.w * 0.5 - self.img_save_game.crop_w * 0.5,
        #                          self.menu_pos[1] + self.menu_rect.h * 0.75 - self.img_save_game.crop_h * 0.5),
        #             img=self.img_save_game.sheet.subsurface(self.img_save_game.crops[0]),
        #             img_pressed=self.img_save_game.sheet.subsurface(self.img_save_game.crops[1]))},
        #     'delete_game': {
        #         'save_game1': Button(
        #             self.screen, pos=(self.menu_pos[0] + self.menu_rect.w * 0.5 + self.img_save_game.crop_w * 0.5 + 2,
        #                          self.menu_pos[1] + self.menu_rect.h * 0.15 - self.img_delete_game.crop_h * 0.5),
        #             hover_on=True, img=self.img_delete_game.sheet.subsurface(self.img_delete_game.crops[0]),
        #             img_hover=self.img_delete_game.sheet.subsurface(self.img_delete_game.crops[1]),
        #             img_pressed=self.img_delete_game.sheet.subsurface(self.img_delete_game.crops[2])),
        #         'save_game2': Button(
        #             self.screen, pos=(self.menu_pos[0] + self.menu_rect.w * 0.5 + self.img_save_game.crop_w * 0.5 + 2,
        #                          self.menu_pos[1] + self.menu_rect.h * 0.35 - self.img_delete_game.crop_h * 0.5),
        #             hover_on=True, img=self.img_delete_game.sheet.subsurface(self.img_delete_game.crops[0]),
        #             img_hover=self.img_delete_game.sheet.subsurface(self.img_delete_game.crops[1]),
        #             img_pressed=self.img_delete_game.sheet.subsurface(self.img_delete_game.crops[2])),
        #         'save_game3': Button(
        #             self.screen, pos=(self.menu_pos[0] + self.menu_rect.w * 0.5 + self.img_save_game.crop_w * 0.5 + 2,
        #                          self.menu_pos[1] + self.menu_rect.h * 0.55 - self.img_delete_game.crop_h * 0.5),
        #             hover_on=True, img=self.img_delete_game.sheet.subsurface(self.img_delete_game.crops[0]),
        #             img_hover=self.img_delete_game.sheet.subsurface(self.img_delete_game.crops[1]),
        #             img_pressed=self.img_delete_game.sheet.subsurface(self.img_delete_game.crops[2])),
        #         'save_game4': Button(
        #             self.screen, pos=(self.menu_pos[0] + self.menu_rect.w * 0.5 + self.img_save_game.crop_w * 0.5 + 2,
        #                          self.menu_pos[1] + self.menu_rect.h * 0.75 - self.img_delete_game.crop_h * 0.5),
        #             hover_on=True, img=self.img_delete_game.sheet.subsurface(self.img_delete_game.crops[0]),
        #             img_hover=self.img_delete_game.sheet.subsurface(self.img_delete_game.crops[1]),
        #             img_pressed=self.img_delete_game.sheet.subsurface(self.img_delete_game.crops[2]))},
        #     'load_game_buttons': {
        #         'save_game1': Button(
        #             self.screen, pos=(self.menu_pos[0] + self.menu_rect.w * 0.5 - self.img_save_game.crop_w * 0.5,
        #                          self.menu_pos[1] + self.menu_rect.h * 0.15 - self.img_save_game.crop_h * 0.5),
        #             img=self.img_save_game.sheet.subsurface(self.img_save_game.crops[0]),
        #             img_pressed=self.img_save_game.sheet.subsurface(self.img_save_game.crops[1])),
        #         'save_game2': Button(
        #             self.screen, pos=(self.menu_pos[0] + self.menu_rect.w * 0.5 - self.img_save_game.crop_w * 0.5,
        #                          self.menu_pos[1] + self.menu_rect.h * 0.35 - self.img_save_game.crop_h * 0.5),
        #             img=self.img_save_game.sheet.subsurface(self.img_save_game.crops[0]),
        #             img_pressed=self.img_save_game.sheet.subsurface(self.img_save_game.crops[1])),
        #         'save_game3': Button(
        #             self.screen, pos=(self.menu_pos[0] + self.menu_rect.w * 0.5 - self.img_save_game.crop_w * 0.5,
        #                          self.menu_pos[1] + self.menu_rect.h * 0.55 - self.img_save_game.crop_h * 0.5),
        #             img=self.img_save_game.sheet.subsurface(self.img_save_game.crops[0]),
        #             img_pressed=self.img_save_game.sheet.subsurface(self.img_save_game.crops[1])),
        #         'save_game4': Button(
        #             self.screen, pos=(self.menu_pos[0] + self.menu_rect.w * 0.5 - self.img_save_game.crop_w * 0.5,
        #                          self.menu_pos[1] + self.menu_rect.h * 0.75 - self.img_save_game.crop_h * 0.5),
        #             img=self.img_save_game.sheet.subsurface(self.img_save_game.crops[0]),
        #             img_pressed=self.img_save_game.sheet.subsurface(self.img_save_game.crops[1]))},
        #     'saved_game_text': {'save_game1': None, 'save_game2': None, 'save_game3': None, 'save_game4': None},
        #     'sound_on': Button(
        #         self.screen, pos=self.menu_but_imgs['sound_on'].get_rect(
        #             center=(self.menu_pos[0] + self.menu_rect.w * 0.5, self.menu_pos[1] + self.menu_rect.h * 0.1)),
        #         hover_on=True, img=self.menu_but_imgs['sound_on'],
        #         img_hover=text('Sound on', font_style=info_font, font_size=30, color=col_white)[0],
        #         img_pressed=text('Sound on', font_style=info_font, font_size=30, color=col_grey)[0]),
        #     'sound_off': Button(
        #         self.screen, pos=self.menu_but_imgs['sound_off'].get_rect(
        #             center=(self.menu_pos[0] + self.menu_rect.w * 0.5, self.menu_pos[1] + self.menu_rect.h * 0.1)),
        #         hover_on=True, img=self.menu_but_imgs['sound_off'],
        #         img_hover=text('Sound off', font_style=info_font, font_size=30, color=col_white)[0],
        #         img_pressed=text('Sound off', font_style=info_font, font_size=30, color=col_grey)[0]),
        #     'back': Button(self.screen, pos=self.menu_but_imgs['back'].get_rect(
        #         center=(self.menu_pos[0] + self.menu_rect.w * 0.5, self.menu_pos[1] + self.menu_rect.h * 0.9)),
        #                    hover_on=True, img=self.menu_but_imgs['back'],
        #                    img_hover=text('Back', font_style=info_font, font_size=30, color=col_white)[0],
        #                    img_pressed=text('Back', font_style=info_font, font_size=30, color=col_grey)[0])
        # }

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, value):
        if type(value) == bool:
            self._active = value
        else:
            raise ValueError('Value must be a boolean')

    @property
    def layer(self):
        return self._layer

    @layer.setter
    def layer(self, value):
        valid_values = ["load", "new_game", "settings"]
        if value in valid_values or value is None:
            self._layer = value
        else:
            raise ValueError(f'Value must be in {valid_values}')

    def update_btns(self):
        self.btns = {
            "load": {
                "bg": {
                    "existent": {
                        socket_num: Button(
                            gral.scr,
                            pos=(self.pos[0] + self.rect.w * 0.5 - self.imgs["btns"]["saved_games"].crop_w * 0.5,
                                 self.pos[1] + self.rect.h * (0.15 + (0.20 * (socket_num - 1)))
                                 - self.imgs["btns"]["saved_games"].crop_h * 0.5),
                            img=self.imgs["btns"]["saved_games"].sheet.subsurface(self.imgs["btns"]["saved_games"].crops[0]),
                            img_pressed=self.imgs["btns"]["saved_games"].sheet.subsurface(self.imgs["btns"]["saved_games"].crops[1]))
                        for socket_num in range(1, 5) if gral.saved_games[socket_num]
                    },
                    "non_existent": {
                        socket_num: Button(
                            gral.scr,
                            pos=(self.pos[0] + self.rect.w * 0.5 - self.imgs["btns"]["saved_games"].crop_w * 0.5,
                                 self.pos[1] + self.rect.h * (0.15 + (0.20 * (socket_num - 1))) - self.imgs["btns"]["saved_games"].crop_h * 0.5),
                            img=self.imgs["btns"]["saved_games"].sheet.subsurface(self.imgs["btns"]["saved_games"].crops[4]))
                        for socket_num in range(1, 5)
                    },
                },
                "text": {
                    "img": {
                        socket_num: merge_surfaces(
                            text(
                                f'{gral.saved_games[socket_num].current_char.name} ('
                                f'{gral.saved_games[socket_num].current_char.char_class})$'
                                f'{readable_text(gral.saved_games[socket_num].current_map.name, "_")}$'
                                f'{gral.saved_games[socket_num].date_time}',
                                font_style=gral.font["info"], font_size=15, color=gral.color["white"]),
                            centered='start'
                        ) for socket_num in range(1, 5) if gral.saved_games[socket_num]
                    },
                    "pos": {
                        socket_num: (
                            (self.pos[0] + self.rect.w * 0.5 - self.imgs["btns"]["saved_games"].crop_w * 0.5) + 90,
                            (self.pos[1] + self.rect.h * (0.15 + (0.20 * (socket_num - 1)))
                             - self.imgs["btns"]["saved_games"].crop_h * 0.5) + 10)
                        for socket_num in range(1, 5) if gral.saved_games[socket_num]
                    }
                }
            },
            "settings": {
                'sound': {
                    "enabled": Button(
                        gral.scr,
                        pos=self.imgs["btns"]["sound"]["enabled"].get_rect(
                            center=(self.pos[0] + self.rect.w * 0.5, self.pos[1] + self.rect.h * 0.1)),
                        hover_on=True,
                        img=self.imgs["btns"]["sound"]["enabled"],
                        img_hover=text('Sound on', font_style=gral.font["info"], font_size=30, color=gral.color["white"])[0],
                        img_pressed=text('Sound on', font_style=gral.font["info"], font_size=30, color=gral.color["grey"])[0]
                    ),
                    "disabled": Button(
                        gral.scr,
                        pos=self.imgs["btns"]["sound"]["disabled"].get_rect(
                            center=(self.pos[0] + self.rect.w * 0.5, self.pos[1] + self.rect.h * 0.1)),
                        hover_on=True,
                        img=self.imgs["btns"]["sound"]["disabled"],
                        img_hover=text('Sound off', font_style=gral.font["info"], font_size=30, color=gral.color["white"])[0],
                        img_pressed=text('Sound off', font_style=gral.font["info"], font_size=30, color=gral.color["grey"])[0]
                    ),
                }
            },
            "back": Button(
                gral.scr,
                pos=self.imgs["btns"]["back"].get_rect(center=(self.pos[0]+self.rect.w*0.5, self.pos[1]+self.rect.h*0.9)),
                hover_on=True, img=self.imgs["btns"]["back"],
                img_hover=text('Back', font_style=gral.font["info"], font_size=30, color=gral.color["white"])[0],
                img_pressed=text('Back', font_style=gral.font["info"], font_size=30, color=gral.color["grey"])[0]),
            "main_menu": {
                "resume": Button(
                    gral.scr, pos=self.imgs["btns"]['resume'].get_rect(
                        center=(self.pos[0] + self.rect.w * 0.5, self.pos[1] + self.rect.h * 0.1)),
                    hover_on=True,
                    img=text('Resume', font_style=gral.font["info"], font_size=30, color=gral.color["black"])[0],
                    img_hover=text('Resume', font_style=gral.font["info"], font_size=30, color=gral.color["white"])[0],
                    img_pressed=text('Resume', font_style=gral.font["info"], font_size=30, color=gral.color["grey"])[0]),
                "save": None,
                "load": None,
                "settings": None,
                "main_menu": None
            }
        }

    def display(self):
        if self.active:
            gral.scr.blit(self.imgs["bg"], self.pos)
            if self.layer == 'main':
                pass
            elif self.layer == 'load':
                for socket_num in range(1, 5):
                    if gral.saved_games[socket_num]:
                        self.btns["load"]["bg"]["existent"][socket_num].draw_button()
                        gral.scr.blit(self.btns["load"]["text"]["img"][socket_num],
                                      self.btns["load"]["text"]["pos"][socket_num])
                    else:
                        self.btns["load"]["bg"]["non_existent"][socket_num].draw_button()
                self.btns["back"].draw_button()
            elif self.layer == 'save':
                pass
            elif self.layer == "settings":
                if gral.settings["sound"] == "enabled":
                    self.btns["settings"]["sound"]["enabled"].draw_button()
                elif gral.settings["sound"] == "disabled":
                    self.btns["settings"]["sound"]["disabled"].draw_button()
                self.btns["back"].draw_button()

    def open(self, layer):
        self.layer = layer
        self.active = True

    def close(self):
        self.layer = None
        self.active = False

    @staticmethod
    def save(socket):
        with open(f"../saves/save_game{socket}.dgn", "wb") as g:
            pickle.dump(gral.current_game, g)

    @staticmethod
    def new_game():
        new_game = Game()

        gral.current_game = new_game

        with open(f"../saves/save_game4.dgn", "wb") as g:
            pickle.dump(new_game, g)

        # sett.current_game['date_time'] = None
        # sett.current_game['current_char'] = None
        # sett.current_game['current_map'] = None
        # sett.current_game['blocking_objs'] = []
        # sett.current_game['current_container'] = None
        # sett.current_game['current_creature'] = None
        # sett.current_game['previous_container'] = None
        # sett.current_game['skills'] = None
        # sett.current_game['equipped'] = {'helm': None, 'weapon': None, 'gloves': None, 'pants': None,
        #                                  'boots': None, 'necklace': None, 'bag':  None, 'shoulder': None,
        #                                  'armor': None, 'ring': None, 'shield': None, 'belt': None},
        # sett.current_game['inv_items'] = generate_grid_status((6, 6), default_value=None)

    @staticmethod
    def switch_sound():
        if gral.settings['sound'] == "enabled":
            gral.settings["sound"] = "disabled"
        elif gral.settings["sound"] == "disabled":
            gral.settings["sound"] = "enabled"
