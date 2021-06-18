from settings import *
import settings as sett


class ConfirmWindow:
	def __init__(self):
		self.img_but_bg100 = Sheet('data/images/gui/but_bg100.png', dimensions=(2, 1))
		self.images = {
				'bg': pg.image.load('data/images/confirm_window/confirm_win_bg.png').convert_alpha(),
				'button_icons': Sheet('data/images/confirm_window/confirm_win_button_icons.png', (1, 2))
		}

		self.win_rect = self.images['bg'].get_rect()
		self.win_pos = (disp_w*0.5-self.win_rect.w*0.5, disp_h*0.5-self.win_rect.h*0.5)

		self.button_pos = {
				'accept': (self.win_pos[0]+self.win_rect.w*0.25-self.img_but_bg100.rect.w*0.5,
				           self.win_pos[1]+self.win_rect.h*0.65),
				'cancel': (self.win_pos[0]+self.win_rect.w*0.75-self.img_but_bg100.rect.w*0.5,
				           self.win_pos[1]+self.win_rect.h*0.65),
		}
		self.buttons = {
				'accept': Button(screen, bg=self.img_but_bg100, icon=self.images['button_icons'],
				                   sheet_index=0, pos=self.button_pos['accept']),
				'cancel': Button(screen, bg=self.img_but_bg100, icon=self.images['button_icons'],
				                   sheet_index=1, pos=self.button_pos['cancel']),
		}

		self.padding = (20, 20)

		self.confirmation_text = ''

		self.msg = None
		self.msg_pos = []

		self.active_win = False
		self.type = ''

	def draw_win(self):
		"""Displays the confirm window if active"""

		if self.active_win:
			screen.blit(self.images['bg'], self.win_pos)
			for index, line in enumerate(self.msg):
				screen.blit(self.msg[index], self.msg_pos[index])
			for but in self.buttons.keys():
				self.buttons[but].draw_button()

	def set_msg(self, msg):
		"""Sets the message to display on the confirmation window"""

		if msg == 'main_menu':
			self.confirmation_text = 'Do you want to go to the main menu?'
			self.type = 'main_menu'
		elif msg == 'quit':
			self.confirmation_text = 'Do you want to quit?'
			self.type = 'quit'
		else: raise Exception('The confirmation text is not valid!')

		self.msg = text(self.confirmation_text, info_font, 24, col_black, max_length=24)
		self.msg_pos = [(self.win_pos[0]+self.win_rect.w*0.5-line.get_width()*0.5,
		                 self.win_pos[1]+self.padding[1]+index*line.get_height()+2) for index, line in enumerate(self.msg)]


IOConfirmWindow = ConfirmWindow()
