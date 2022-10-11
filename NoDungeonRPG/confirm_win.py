from pygame_utilities import Sheet, Button, text
import pygame as pg
import general as gral


class ConfirmWindow:
	def __init__(self):
		self.imgs = {
			"bg": pg.image.load("data/images/confirm_window/confirm_win_bg.png").convert_alpha(),
			"btn_bg100": Sheet("data/images/gui/but_bg100.png", dimensions=(2, 1)),
			"btn_icons": Sheet("data/images/confirm_window/confirm_win_button_icons.png", (1, 2)),
		}

		self.rect = self.imgs["bg"].get_rect()
		self.pos = (gral.scr_dim[0] * 0.5 - self.rect.w * 0.5, gral.scr_dim[1] * 0.5 - self.rect.h * 0.5,)

		self.btns = {
			"accept": Button(
				gral.scr,
				bg=self.imgs["btn_bg100"],
				icon=self.imgs["btn_icons"],
				sheet_index=0,
				pos=(self.pos[0] + self.rect.w * 0.25 - self.imgs["btn_bg100"].rect.w * 0.5,
					 self.pos[1] + self.rect.h * 0.65)
			),
			"cancel": Button(
				gral.scr,
				bg=self.imgs["btn_bg100"],
				icon=self.imgs["btn_icons"],
				sheet_index=1,
				pos=(self.pos[0] + self.rect.w * 0.75 - self.imgs["btn_bg100"].rect.w * 0.5,
					 self.pos[1] + self.rect.h * 0.65)
			)
		}

		self.msgs = {
			"load": "Load this game?",
			"new_game": "Start a new game?",
			"quit": "Do you want to quit?",
			"save": "Save this game?",
			"main_menu": "Go to the main menu?",
		}
		self.msg = None
		self.msg_pos = []
		self.interline = 20

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

	def display(self):
		"""Displays the confirmation window"""

		if self.active:
			if self.msg:
				gral.scr.blit(self.imgs["bg"], self.pos)
				for btn in self.btns.keys():
					self.btns[btn].draw_button()
				for index, line in enumerate(self.msg):
					gral.scr.blit(self.msg[index], self.msg_pos[index])

	def open(self, mode, **kwargs):
		"""Opens the confirmation window"""

		self.set_mode_msg(mode)
		self.active = True
		self.temp_kwargs = kwargs

	def close(self):
		"""Closes the confirmation window and resets its temporary kwargs"""

		self.set_mode_msg(None)
		self.active = False
		self.temp_kwargs = None

	def set_mode_msg(self, mode):
		"""Sets the confirmation window mode and its message"""

		self.mode = mode

		if self.mode:
			self.msg = text(self.msgs[self.mode], gral.font["info"], 24, gral.color["black"], max_length=24)
			self.msg_pos = [(self.pos[0] + self.rect.w * 0.5 - line.get_width() * 0.5,
							 self.pos[1] + self.interline + index * line.get_height() + 2)
							for index, line in enumerate(self.msg)]
