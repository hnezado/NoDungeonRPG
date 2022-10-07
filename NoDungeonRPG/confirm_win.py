from pygame_utilities import Sheet, Button, text
import pygame as pg
import general as gral


class ConfirmWindow:
	def __init__(self):
		self.scr_w, self.scr_h = gral.scr_dim
		self.img_btn_bg100 = Sheet("data/images/gui/but_bg100.png", dimensions=(2, 1))
		self.imgs = {
			"bg": pg.image.load("data/images/confirm_window/confirm_win_bg.png").convert_alpha(),
			"btn_bg100": Sheet("data/images/gui/but_bg100.png", dimensions=(2, 1)),
			"btn_icons": Sheet("data/images/confirm_window/confirm_win_button_icons.png", (1, 2)),
		}

		self.rect = self.imgs["bg"].get_rect()
		self.pos = (self.scr_w * 0.5 - self.rect.w * 0.5, self.scr_h * 0.5 - self.rect.h * 0.5,)

		self.btn_pos = {
			"accept": (self.pos[0] + self.rect.w * 0.25 - self.imgs["btn_bg100"].rect.w * 0.5,
					   self.pos[1] + self.rect.h * 0.65),
			"cancel": (self.pos[0] + self.rect.w * 0.75 - self.imgs["btn_bg100"].rect.w * 0.5,
					   self.pos[1] + self.rect.h * 0.65,),
		}
		self.btns = {
			"accept": Button(
				gral.scr,
				bg=self.imgs["btn_bg100"],
				icon=self.imgs["btn_icons"],
				sheet_index=0,
				pos=self.btn_pos["accept"],
			),
			"cancel": Button(
				gral.scr,
				bg=self.imgs["btn_bg100"],
				icon=self.imgs["btn_icons"],
				sheet_index=1,
				pos=self.btn_pos["cancel"],
			),
		}

		self.msg_padding = (20, 20)

		self.msgs = {
			"quit": "Do you want to quit?",
			"main_menu": "Go to the main menu?",
			"new_game": "Start a new game?",
			"load": "Load this game?",
			"save": "Save this game?"
		}
		self._confirmation_text = ''

		self.msg = None
		self.msg_pos = []

		self.temp_kwargs = None

		self._mode = None
		self._active = False

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
	def mode(self):
		return self._mode

	@mode.setter
	def mode(self, value):
		if value in self.msgs.keys() or value is None:
			self._mode = value
		else:
			raise ValueError(f'Value must be in {self.msgs.keys()}')

	def clear_temp_kwargs(self):
		self.temp_kwargs = None

	def display(self):
		"""Displays the confirmation window"""

		if self.active:
			if self.msg:
				gral.scr.blit(self.imgs["bg"], self.pos)
				for index, line in enumerate(self.msg):
					gral.scr.blit(self.msg[index], self.msg_pos[index])
				for btn in self.btns.keys():
					self.btns[btn].draw_button()

	def open(self, mode, **kwargs):
		self.set_mode(mode)
		self.active = True
		self.temp_kwargs = kwargs

	def close(self):
		self.set_mode(None)
		self.active = False

	def set_mode(self, mode):
		"""Sets the confirmation window mode and its message"""

		self.mode = mode

		if self.mode:
			self.msg = text(self.msgs[self.mode], gral.font["info"], 24, gral.color["black"], max_length=24)
			self.msg_pos = [(self.pos[0] + self.rect.w * 0.5 - line.get_width() * 0.5,
							 self.pos[1] + self.msg_padding[1] + index * line.get_height() + 2)
							for index, line in enumerate(self.msg)]
