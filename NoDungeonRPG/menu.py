from pygame_utilities import *


class Menu:
    def __init__(self, scr, scr_dim, settings):
        self.scr = scr
        self.scr_w, self.scr_h = scr_dim
        self.settings = settings

        self.img_bg = pg.image.load("data/images/gui/menu_bg.png").convert_alpha()
        self.img_save = Sheet("data/images/gui/save_game.png", (5, 1))
        self.img_delete = Sheet("data/images/gui/delete_game.png", (3, 1))

        self.pos = (self.scr_w * .5 - self.img_bg.get_width() * .5, self.scr_h * .5 - self.img_bg.get_height() * .5)
        self.rect = self.img_bg.get_rect()

        self.txt_btn_back = text('Back', font_style=font["info"], font_size=30, color=color["black"])[0]

        self._active = False
        self._layer = None

        self.btns = {
            "load": {
                "bg": {
                    num: Button(
                        self.scr,
                        pos=(self.pos[0] + self.rect.w * 0.5 - self.img_save.crop_w * 0.5,
                             self.pos[1] + self.rect.h * (0.15 + (0.20 * (num - 1))) - self.img_save.crop_h * 0.5),
                        img=self.img_save.sheet.subsurface(self.img_save.crops[0]),
                        img_pressed=self.img_save.sheet.subsurface(self.img_save.crops[1]))
                    for num in range(1, 5)
                },
                "text": {
                    num: str(num)
                    for num in range(1, 5)
                },
            },
            "settings": {
                'sound': {
                    "enabled": Button(
                        self.scr,
                        pos=text('Sound on', font_style=font["info"], font_size=30, color=color["green"])[0].get_rect(
                            center=(self.pos[0] + self.rect.w * 0.5, self.pos[1] + self.rect.h * 0.1)),
                        hover_on=True,
                        img=text('Sound on', font_style=font["info"], font_size=30, color=color["green"])[0],
                        img_hover=text('Sound on', font_style=font["info"], font_size=30, color=color["white"])[0],
                        img_pressed=text('Sound on', font_style=font["info"], font_size=30, color=color["grey"])[0]
                    ),
                    "disabled": Button(
                        self.scr,
                        pos=text('Sound off', font_style=font["info"], font_size=30, color=color["red"])[0].get_rect(
                            center=(self.pos[0] + self.rect.w * 0.5, self.pos[1] + self.rect.h * 0.1)),
                        hover_on=True,
                        img=text('Sound off', font_style=font["info"], font_size=30, color=color["red"])[0],
                        img_hover=text('Sound off', font_style=font["info"], font_size=30, color=color["white"])[0],
                        img_pressed=text('Sound off', font_style=font["info"], font_size=30, color=color["grey"])[0]
                    ),
                }
            },
            "back": Button(
                self.scr,
                pos=self.txt_btn_back.get_rect(center=(self.pos[0]+self.rect.w*0.5, self.pos[1]+self.rect.h*0.9)),
                hover_on=True, img=self.txt_btn_back,
                img_hover=text('Back', font_style=font["info"], font_size=30, color=color["white"])[0],
                img_pressed=text('Back', font_style=font["info"], font_size=30, color=color["grey"])[0])
        }

        #     "text": {
        #         1: Button(
        #
        #         ),
        #         2: Button(
        #
        #         ),
        #         3: Button(
        #
        #         ),
        #         4: Button(
        #
        #         ),
        #     }

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

    def display(self):
        if self.active:
            self.scr.blit(self.img_bg, self.pos)
            if self.layer == 'main':
                pass
            elif self.layer == 'load':
                for socket, btn_bg in self.btns["load"]["bg"].items():
                    btn_bg.draw_button()
                for socket, txt in self.btns["load"]["text"].items():
                    pass
                self.btns["back"].draw_button()
            elif self.layer == 'save':
                pass
            elif self.layer == "settings":
                if self.settings["sound"] == "enabled":
                    self.btns["settings"]["sound"]["enabled"].draw_button()
                elif self.settings["sound"] == "disabled":
                    self.btns["settings"]["sound"]["disabled"].draw_button()
                self.btns["back"].draw_button()

    def open(self, layer):
        self.layer = layer
        self.active = True

    def close(self):
        self.layer = None
        self.active = False

    def load(self):
        pass

    def new_game(self):
        pass

    def switch_sound(self):
        if self.settings['sound'] == "enabled":
            self.settings["sound"] = "disabled"
        elif self.settings["sound"] == "disabled":
            self.settings["sound"] = "enabled"
