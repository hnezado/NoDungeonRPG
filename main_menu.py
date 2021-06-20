from combat import *

main_menu_img = {
	'button_icons': Sheet('data/images/main_menu/main_menu_button_icons.png', dimensions=(1, 4)),
}

title = text(txt='No Dungeon RPG', font_style=info_font, font_size=60, color=col_white)[0]


class MainMenu:
	def __init__(self):
		self.main_menu_bg = pg.image.load('data/images/main_menu/main_menu_bg.png')
		self.main_menu_buttons_panel = pg.image.load('data/images/main_menu/main_menu_buttons_bg.png')
		self.panel_pos = (0, self.main_menu_bg.get_height())
		self.panel_rect = pg.Rect(self.main_menu_buttons_panel.get_rect())
		self.but_rect = pg.Rect(0, 0, 158, 58)
		self.button_pos = {
				'continue': (self.panel_pos[0]+self.panel_rect.w*0.125-self.but_rect.w*0.5,
				             self.panel_pos[1]+self.panel_rect.h*0.5-self.but_rect.h*0.5),
				'new_game': (self.panel_pos[0]+self.panel_rect.w*0.125+self.panel_rect.w*0.25-self.but_rect.w*0.5,
				             self.panel_pos[1]+self.panel_rect.h*0.5-self.but_rect.h*0.5),
				'settings': (self.panel_pos[0]+self.panel_rect.w*0.125+self.panel_rect.w*0.5-self.but_rect.w*0.5,
				             self.panel_pos[1]+self.panel_rect.h*0.5-self.but_rect.h*0.5),
				'quit': (self.panel_pos[0]+self.panel_rect.w*0.125+self.panel_rect.w*0.75-self.but_rect.w*0.5,
				             self.panel_pos[1]+self.panel_rect.h*0.5-self.but_rect.h*0.5),
		}
		self.buttons = {
				'continue': Button(screen, bg=IOGUI.img_but_bg150_sh, icon=main_menu_img['button_icons'],
				                   sheet_index=0, pos=self.button_pos['continue']),
				'new_game': Button(screen, bg=IOGUI.img_but_bg150_sh, icon=main_menu_img['button_icons'],
				                   sheet_index=1, pos=self.button_pos['new_game']),
				'settings': Button(screen, bg=IOGUI.img_but_bg150_sh, icon=main_menu_img['button_icons'],
				                   sheet_index=2, pos=self.button_pos['settings']),
				'quit': Button(screen, bg=IOGUI.img_but_bg150_sh, icon=main_menu_img['button_icons'],
				                   sheet_index=3, pos=self.button_pos['quit']),
		}

		# # Menu #
		# self.menu_active = False
		# self.menu_layer = 'main'
		# self.menu_pos = (disp_w*0.5-self.img_menu_bg.get_width()*.5, disp_h*0.5-self.img_menu_bg.get_height()*0.5)
		# self.menu_but_imgs = {
		#                       'settings':  text('Settings', font_style=info_font, font_size=30, color=col_black)[0],
		#                       'load_game': text('Load game', font_style=info_font, font_size=30, color=col_black)[0],
		#                       'sound_on':  text('Sound on', font_style=info_font, font_size=30, color=col_green)[0],
		#                       'sound_off': text('Sound off', font_style=info_font, font_size=30, color=col_red)[0],
		#                       'close':     text('Close', font_style=info_font, font_size=30, color=col_black)[0]}
		# self.menu_but = {'resume':                                                                            Button(
		# 		screen, pos=self.menu_but_imgs['resume'].get_rect(
		# 				center=(self.menu_pos[0]+IOGUI.menu_rect.w*0.5, self.menu_pos[1]+IOGUI.menu_rect.h*0.1)),
		# 		hover_on=True, img=self.menu_but_imgs['resume'],
		# 		img_hover=text('Resume', font_style=info_font, font_size=30, color=col_white)[0],
		# 		img_pressed=text('Resume', font_style=info_font, font_size=30, color=col_grey)[0]), 'save':   Button(
		# 		screen, pos=self.menu_but_imgs['save'].get_rect(
		# 				center=(self.menu_pos[0]+IOGUI.menu_rect.w*0.5, self.menu_pos[1]+IOGUI.menu_rect.h*0.3)),
		# 		hover_on=True, img=self.menu_but_imgs['save'],
		# 		img_hover=text('Save', font_style=info_font, font_size=30, color=col_white)[0],
		# 		img_pressed=text('Save', font_style=info_font, font_size=30, color=col_grey)[0]), 'load':     Button(
		# 		screen, pos=self.menu_but_imgs['load'].get_rect(
		# 				center=(self.menu_pos[0]+IOGUI.menu_rect.w*0.5, self.menu_pos[1]+IOGUI.menu_rect.h*0.5)),
		# 		hover_on=True, img=self.menu_but_imgs['load'],
		# 		img_hover=text('Load', font_style=info_font, font_size=30, color=col_white)[0],
		# 		img_pressed=text('Load', font_style=info_font, font_size=30, color=col_grey)[0]), 'settings': Button(
		# 		screen, pos=self.menu_but_imgs['settings'].get_rect(
		# 				center=(self.menu_pos[0]+IOGUI.menu_rect.w*0.5, self.menu_pos[1]+IOGUI.menu_rect.h*0.7)),
		# 		hover_on=True, img=self.menu_but_imgs['settings'],
		# 		img_hover=text('Settings', font_style=info_font, font_size=30, color=col_white)[0],
		# 		img_pressed=text('Settings', font_style=info_font, font_size=30, color=col_grey)[0]),
		# 		'main_menu':                                                                                  Button(
		# 				screen, pos=self.menu_but_imgs['main_menu'].get_rect(
		# 						center=(self.menu_pos[0]+IOGUI.menu_rect.w*0.5, self.menu_pos[1]+IOGUI.menu_rect.h*0.9)),
		# 				hover_on=True, img=self.menu_but_imgs['main_menu'],
		# 				img_hover=text('Main menu', font_style=info_font, font_size=30, color=col_white)[0],
		# 				img_pressed=text('Main menu', font_style=info_font, font_size=30, color=col_grey)[0]),
		# 		'save_game_buttons':                                                                          {
		# 				'save_game1': Button(screen, pos=(
		# 				self.menu_pos[0]+IOGUI.menu_rect.w*0.5-self.img_save_game.crop_w*0.5,
		# 				self.menu_pos[1]+IOGUI.menu_rect.h*0.15-self.img_save_game.crop_h*0.5),
		# 						img=self.img_save_game.sheet.subsurface(self.img_save_game.crops[0]),
		# 						img_pressed=self.img_save_game.sheet.subsurface(self.img_save_game.crops[1])),
		# 				'save_game2': Button(screen, pos=(
		# 				self.menu_pos[0]+IOGUI.menu_rect.w*0.5-self.img_save_game.crop_w*0.5,
		# 				self.menu_pos[1]+IOGUI.menu_rect.h*0.35-self.img_save_game.crop_h*0.5),
		# 						img=self.img_save_game.sheet.subsurface(self.img_save_game.crops[0]),
		# 						img_pressed=self.img_save_game.sheet.subsurface(self.img_save_game.crops[1])),
		# 				'save_game3': Button(screen, pos=(
		# 				self.menu_pos[0]+IOGUI.menu_rect.w*0.5-self.img_save_game.crop_w*0.5,
		# 				self.menu_pos[1]+IOGUI.menu_rect.h*0.55-self.img_save_game.crop_h*0.5),
		# 						img=self.img_save_game.sheet.subsurface(self.img_save_game.crops[0]),
		# 						img_pressed=self.img_save_game.sheet.subsurface(self.img_save_game.crops[1])),
		# 				'save_game4': Button(screen, pos=(
		# 				self.menu_pos[0]+IOGUI.menu_rect.w*0.5-self.img_save_game.crop_w*0.5,
		# 				self.menu_pos[1]+IOGUI.menu_rect.h*0.75-self.img_save_game.crop_h*0.5),
		# 						img=self.img_save_game.sheet.subsurface(self.img_save_game.crops[0]),
		# 						img_pressed=self.img_save_game.sheet.subsurface(self.img_save_game.crops[1]))},
		# 		'delete_game':                                                                                {
		# 				'save_game1': Button(screen, pos=(
		# 				self.menu_pos[0]+IOGUI.menu_rect.w*0.5+self.img_save_game.crop_w*0.5+2,
		# 				self.menu_pos[1]+IOGUI.menu_rect.h*0.15-self.img_delete_game.crop_h*0.5), hover_on=True,
		# 						img=self.img_delete_game.sheet.subsurface(self.img_delete_game.crops[0]),
		# 						img_hover=self.img_delete_game.sheet.subsurface(self.img_delete_game.crops[1]),
		# 						img_pressed=self.img_delete_game.sheet.subsurface(self.img_delete_game.crops[2])),
		# 				'save_game2': Button(screen, pos=(
		# 				self.menu_pos[0]+IOGUI.menu_rect.w*0.5+self.img_save_game.crop_w*0.5+2,
		# 				self.menu_pos[1]+IOGUI.menu_rect.h*0.35-self.img_delete_game.crop_h*0.5), hover_on=True,
		# 						img=self.img_delete_game.sheet.subsurface(self.img_delete_game.crops[0]),
		# 						img_hover=self.img_delete_game.sheet.subsurface(self.img_delete_game.crops[1]),
		# 						img_pressed=self.img_delete_game.sheet.subsurface(self.img_delete_game.crops[2])),
		# 				'save_game3': Button(screen, pos=(
		# 				self.menu_pos[0]+IOGUI.menu_rect.w*0.5+self.img_save_game.crop_w*0.5+2,
		# 				self.menu_pos[1]+IOGUI.menu_rect.h*0.55-self.img_delete_game.crop_h*0.5), hover_on=True,
		# 						img=self.img_delete_game.sheet.subsurface(self.img_delete_game.crops[0]),
		# 						img_hover=self.img_delete_game.sheet.subsurface(self.img_delete_game.crops[1]),
		# 						img_pressed=self.img_delete_game.sheet.subsurface(self.img_delete_game.crops[2])),
		# 				'save_game4': Button(screen, pos=(
		# 				self.menu_pos[0]+IOGUI.menu_rect.w*0.5+self.img_save_game.crop_w*0.5+2,
		# 				self.menu_pos[1]+IOGUI.menu_rect.h*0.75-self.img_delete_game.crop_h*0.5), hover_on=True,
		# 						img=self.img_delete_game.sheet.subsurface(self.img_delete_game.crops[0]),
		# 						img_hover=self.img_delete_game.sheet.subsurface(self.img_delete_game.crops[1]),
		# 						img_pressed=self.img_delete_game.sheet.subsurface(self.img_delete_game.crops[2]))},
		# 		'load_game_buttons':                                                                          {
		# 				'save_game1': Button(screen, pos=(
		# 				self.menu_pos[0]+IOGUI.menu_rect.w*0.5-self.img_save_game.crop_w*0.5,
		# 				self.menu_pos[1]+IOGUI.menu_rect.h*0.15-self.img_save_game.crop_h*0.5),
		# 						img=self.img_save_game.sheet.subsurface(self.img_save_game.crops[0]),
		# 						img_pressed=self.img_save_game.sheet.subsurface(self.img_save_game.crops[1])),
		# 				'save_game2': Button(screen, pos=(
		# 				self.menu_pos[0]+IOGUI.menu_rect.w*0.5-self.img_save_game.crop_w*0.5,
		# 				self.menu_pos[1]+IOGUI.menu_rect.h*0.35-self.img_save_game.crop_h*0.5),
		# 						img=self.img_save_game.sheet.subsurface(self.img_save_game.crops[0]),
		# 						img_pressed=self.img_save_game.sheet.subsurface(self.img_save_game.crops[1])),
		# 				'save_game3': Button(screen, pos=(
		# 				self.menu_pos[0]+IOGUI.menu_rect.w*0.5-self.img_save_game.crop_w*0.5,
		# 				self.menu_pos[1]+IOGUI.menu_rect.h*0.55-self.img_save_game.crop_h*0.5),
		# 						img=self.img_save_game.sheet.subsurface(self.img_save_game.crops[0]),
		# 						img_pressed=self.img_save_game.sheet.subsurface(self.img_save_game.crops[1])),
		# 				'save_game4': Button(screen, pos=(
		# 				self.menu_pos[0]+IOGUI.menu_rect.w*0.5-self.img_save_game.crop_w*0.5,
		# 				self.menu_pos[1]+IOGUI.menu_rect.h*0.75-self.img_save_game.crop_h*0.5),
		# 						img=self.img_save_game.sheet.subsurface(self.img_save_game.crops[0]),
		# 						img_pressed=self.img_save_game.sheet.subsurface(self.img_save_game.crops[1]))},
		# 		'saved_game_text':                                                                            {
		# 				'save_game1': None, 'save_game2': None, 'save_game3': None, 'save_game4': None},
		# 		'sound_on':                                                                                   Button(
		# 				screen, pos=self.menu_but_imgs['sound_on'].get_rect(
		# 						center=(self.menu_pos[0]+IOGUI.menu_rect.w*0.5, self.menu_pos[1]+IOGUI.menu_rect.h*0.1)),
		# 				hover_on=True, img=self.menu_but_imgs['sound_on'],
		# 				img_hover=text('Sound on', font_style=info_font, font_size=30, color=col_white)[0],
		# 				img_pressed=text('Sound on', font_style=info_font, font_size=30, color=col_grey)[0]),
		# 		'sound_off':                                                                                  Button(
		# 				screen, pos=self.menu_but_imgs['sound_off'].get_rect(
		# 						center=(self.menu_pos[0]+IOGUI.menu_rect.w*0.5, self.menu_pos[1]+IOGUI.menu_rect.h*0.1)),
		# 				hover_on=True, img=self.menu_but_imgs['sound_off'],
		# 				img_hover=text('Sound off', font_style=info_font, font_size=30, color=col_white)[0],
		# 				img_pressed=text('Sound off', font_style=info_font, font_size=30, color=col_grey)[0]),
		# 		'back':                                                                                       Button(
		# 			screen, pos=self.menu_but_imgs['back'].get_rect(
		# 					center=(self.menu_pos[0]+IOGUI.menu_rect.w*0.5, self.menu_pos[1]+IOGUI.menu_rect.h*0.9)),
		# 			hover_on=True, img=self.menu_but_imgs['back'],
		# 			img_hover=text('Back', font_style=info_font, font_size=30, color=col_white)[0],
		# 			img_pressed=text('Back', font_style=info_font, font_size=30, color=col_grey)[0])}

	def draw_main_menu(self):
		"""Display the main menu"""

		screen.blit(self.main_menu_bg, (0, 0))
		screen.blit(title, (disp_w*0.5-title.get_width()*0.5, disp_h*0.125))
		self.draw_buttons()
		IOGUI.draw_menu(main_menu=True)

	def draw_buttons(self):
		"""Displays the main menu buttons"""

		screen.blit(self.main_menu_buttons_panel, (0, 640))
		for but in self.buttons.keys():
			self.buttons[but].draw_button()

	@staticmethod
	def new_game():
		"""Creates a new game instance"""

		pass

		# sett.current_game['date_time'] = None
		# sett.current_game['current_char'] = None
		# sett.current_game['current_map'] = None
		# sett.current_game['blocking_objs'] = []
		# sett.current_game['current_container'] = None
		# sett.current_game['current_creature'] = None
		# sett.current_game['previous_container'] = None
		# sett.current_game['skills'] = None
		# sett.current_game['equipped'] = {'helm': None, 'weapon': None, 'gloves': None, 'pants': None, 'boots': None,
		#                                  'necklace': None, 'bag':  None, 'shoulder': None, 'armor': None, 'ring': None,
		#                                  'shield': None, 'belt': None},
		# sett.current_game['inv_items'] = generate_grid_status((6, 6), default_value=None)


IOMainMenu = MainMenu()
