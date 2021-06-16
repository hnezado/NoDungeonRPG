from settings import *

title = text(txt='No Dungeon RPG', font_style=info_font, font_size=60, color=col_white)[0]
class MainMenu:
	def __init__(self):
		self.main_menu_bg = pg.image.load('data/images/main_menu/main_menu_bg.png')
		self.main_menu_buttons_bg = pg.image.load('data/images/main_menu/main_menu_buttons_bg.png')
		self.buttons = {
				'continue': Button(screen, )
		}

	def draw_main_menu(self):
		"""Display the main menu"""

		screen.blit(self.main_menu_bg, (0, 0))
		screen.blit(title, (disp_w*0.5-title.get_width()*0.5, disp_h*0.125))
		self.draw_buttons()

	def draw_buttons(self):
		"""Displays the main menu buttons"""

		screen.blit(self.main_menu_buttons_bg, (0, 640))
		# screen.blit(self.buttons['continue'], ())


IOMainMenu = MainMenu()
