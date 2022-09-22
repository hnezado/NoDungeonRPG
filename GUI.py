from atlas import *

opened_windows = []
item_info = {}


class GraphicalUserInterface:
	def __init__(self):

		# Image loadings #
		self.img_menu_bg = pg.image.load('data/images/gui/menu_bg.png').convert_alpha()
		self.img_save_game = Sheet('data/images/gui/save_game.png', (5, 1))
		self.img_delete_game = Sheet('data/images/gui/delete_game.png', (3, 1))
		self.img_gui_bg1 = pg.image.load('data/images/gui/guis/gui_bg1.png').convert_alpha()
		self.img_but_icon_ingame_menu = Sheet('data/images/gui/but_icon_ingame_menu.png', dimensions=(1, 1))
		self.img_but_bg50 = Sheet('data/images/gui/but_bg50.png', dimensions=(1, 3))
		self.img_but_bg50_sh = Sheet('data/images/gui/but_bg50_sh.png', dimensions=(1, 3))
		self.img_but_bg100 = Sheet('data/images/gui/but_bg100.png', dimensions=(2, 1))
		self.img_but_bg150_sh = Sheet('data/images/gui/but_bg150_sh.png', dimensions=(2, 1))
		self.img_but_equ_inv = Sheet('data/images/gui/but_equ_inv.png', dimensions=(2, 3))
		self.img_msg_box = pg.image.load('data/images/gui/msg_box.png').convert_alpha()
		self.img_glass_bar = pg.image.load('data/images/gui/glass_bar.png').convert_alpha()
		self.img_hp_bar = pg.image.load('data/images/gui/hp_bar.png').convert_alpha()
		self.img_mp_bar = pg.image.load('data/images/gui/mp_bar.png').convert_alpha()
		self.img_vigor_bar = pg.image.load('data/images/gui/vigor_bar.png').convert_alpha()
		self.img_spirit_bar = pg.image.load('data/images/gui/spirit_bar.png').convert_alpha()
		self.img_spirit_inner_bar = Sheet('data/images/gui/spirit_inner_bar.png', dimensions=(11, 1))
		self.img_spirit_halo = pg.image.load('data/images/gui/spirit_halo.png').convert_alpha()
		self.img_portrait1 = pg.image.load('data/images/gui/portrait.png').convert_alpha()
		self.img_info_bg = pg.image.load('data/images/info_bg.png').convert()

		# Menu #
		self.ingame_menu_button = Button(screen, bg=self.img_but_bg150_sh, icon=self.img_but_icon_ingame_menu,
		                                 sheet_index=0, pos=(850, 694))
		self.menu_active = False
		self.menu_layer = 'main'
		self.menu_rect = self.img_menu_bg.get_rect()
		self.menu_pos = (disp_w*0.5-self.img_menu_bg.get_width()*.5, disp_h*0.5-self.img_menu_bg.get_height()*0.5)
		self.menu_but_imgs = {'resume': text('Resume', font_style=info_font, font_size=30, color=col_black)[0],
		                      'save': text('Save', font_style=info_font, font_size=30, color=col_black)[0],
		                      'load': text('Load', font_style=info_font, font_size=30, color=col_black)[0],
		                      'settings': text('Settings', font_style=info_font, font_size=30, color=col_black)[0],
		                      'main_menu': text('Main menu', font_style=info_font, font_size=30, color=col_black)[0],
		                      'load_game': text('Load game', font_style=info_font, font_size=30, color=col_black)[0],
		                      'sound_on': text('Sound on', font_style=info_font, font_size=30, color=col_green)[0],
		                      'sound_off': text('Sound off', font_style=info_font, font_size=30, color=col_red)[0],
		                      'back': text('Back', font_style=info_font, font_size=30, color=col_black)[0]
		                      }
		self.menu_but = {
				'resume': Button(
						screen, pos=self.menu_but_imgs['resume'].get_rect(
								center=(self.menu_pos[0]+self.menu_rect.w*0.5, self.menu_pos[1]+self.menu_rect.h*0.1)),
						hover_on=True, img=self.menu_but_imgs['resume'],
						img_hover=text('Resume', font_style=info_font, font_size=30, color=col_white)[0],
						img_pressed=text('Resume', font_style=info_font, font_size=30, color=col_grey)[0]),
				'save': Button(
						screen, pos=self.menu_but_imgs['save'].get_rect(
								center=(self.menu_pos[0]+self.menu_rect.w*0.5, self.menu_pos[1]+self.menu_rect.h*0.3)),
						hover_on=True, img=self.menu_but_imgs['save'],
						img_hover=text('Save', font_style=info_font, font_size=30, color=col_white)[0],
						img_pressed=text('Save', font_style=info_font, font_size=30, color=col_grey)[0]),
				'load': Button(
						screen, pos=self.menu_but_imgs['load'].get_rect(
								center=(self.menu_pos[0]+self.menu_rect.w*0.5, self.menu_pos[1]+self.menu_rect.h*0.5)),
						hover_on=True, img=self.menu_but_imgs['load'],
						img_hover=text('Load', font_style=info_font, font_size=30, color=col_white)[0],
						img_pressed=text('Load', font_style=info_font, font_size=30, color=col_grey)[0]),
				'settings': Button(
						screen, pos=self.menu_but_imgs['settings'].get_rect(
								center=(self.menu_pos[0]+self.menu_rect.w*0.5, self.menu_pos[1]+self.menu_rect.h*0.7)),
						hover_on=True, img=self.menu_but_imgs['settings'],
						img_hover=text('Settings', font_style=info_font, font_size=30, color=col_white)[0],
						img_pressed=text('Settings', font_style=info_font, font_size=30, color=col_grey)[0]),
				'main_menu': Button(
						screen, pos=self.menu_but_imgs['main_menu'].get_rect(
								center=(self.menu_pos[0]+self.menu_rect.w*0.5, self.menu_pos[1]+self.menu_rect.h*0.9)),
						hover_on=True, img=self.menu_but_imgs['main_menu'],
						img_hover=text('Main menu', font_style=info_font, font_size=30, color=col_white)[0],
						img_pressed=text('Main menu', font_style=info_font, font_size=30, color=col_grey)[0]),
				'save_game_buttons': {
						'save_game1': Button(
								screen, pos=(self.menu_pos[0]+self.menu_rect.w*0.5-self.img_save_game.crop_w*0.5,
								             self.menu_pos[1]+self.menu_rect.h*0.15-self.img_save_game.crop_h*0.5),
								img=self.img_save_game.sheet.subsurface(self.img_save_game.crops[0]),
								img_pressed=self.img_save_game.sheet.subsurface(self.img_save_game.crops[1])),
						'save_game2': Button(
								screen, pos=(self.menu_pos[0]+self.menu_rect.w*0.5-self.img_save_game.crop_w*0.5,
								             self.menu_pos[1]+self.menu_rect.h*0.35-self.img_save_game.crop_h*0.5),
								img=self.img_save_game.sheet.subsurface(self.img_save_game.crops[0]),
								img_pressed=self.img_save_game.sheet.subsurface(self.img_save_game.crops[1])),
						'save_game3': Button(
								screen, pos=(self.menu_pos[0]+self.menu_rect.w*0.5-self.img_save_game.crop_w*0.5,
								             self.menu_pos[1]+self.menu_rect.h*0.55-self.img_save_game.crop_h*0.5),
								img=self.img_save_game.sheet.subsurface(self.img_save_game.crops[0]),
								img_pressed=self.img_save_game.sheet.subsurface(self.img_save_game.crops[1])),
						'save_game4': Button(
								screen, pos=(self.menu_pos[0]+self.menu_rect.w*0.5-self.img_save_game.crop_w*0.5,
								             self.menu_pos[1]+self.menu_rect.h*0.75-self.img_save_game.crop_h*0.5),
								img=self.img_save_game.sheet.subsurface(self.img_save_game.crops[0]),
								img_pressed=self.img_save_game.sheet.subsurface(self.img_save_game.crops[1]))},
				'delete_game': {
						'save_game1': Button(
								screen, pos=(self.menu_pos[0]+self.menu_rect.w*0.5+self.img_save_game.crop_w*0.5+2,
								             self.menu_pos[1]+self.menu_rect.h*0.15-self.img_delete_game.crop_h*0.5),
								hover_on=True, img=self.img_delete_game.sheet.subsurface(self.img_delete_game.crops[0]),
								img_hover=self.img_delete_game.sheet.subsurface(self.img_delete_game.crops[1]),
								img_pressed=self.img_delete_game.sheet.subsurface(self.img_delete_game.crops[2])),
						'save_game2': Button(
								screen, pos=(self.menu_pos[0]+self.menu_rect.w*0.5+self.img_save_game.crop_w*0.5+2,
								             self.menu_pos[1]+self.menu_rect.h*0.35-self.img_delete_game.crop_h*0.5),
								hover_on=True, img=self.img_delete_game.sheet.subsurface(self.img_delete_game.crops[0]),
								img_hover=self.img_delete_game.sheet.subsurface(self.img_delete_game.crops[1]),
								img_pressed=self.img_delete_game.sheet.subsurface(self.img_delete_game.crops[2])),
						'save_game3': Button(
								screen, pos=(self.menu_pos[0]+self.menu_rect.w*0.5+self.img_save_game.crop_w*0.5+2,
								             self.menu_pos[1]+self.menu_rect.h*0.55-self.img_delete_game.crop_h*0.5),
								hover_on=True, img=self.img_delete_game.sheet.subsurface(self.img_delete_game.crops[0]),
								img_hover=self.img_delete_game.sheet.subsurface(self.img_delete_game.crops[1]),
								img_pressed=self.img_delete_game.sheet.subsurface(self.img_delete_game.crops[2])),
						'save_game4': Button(
								screen, pos=(self.menu_pos[0]+self.menu_rect.w*0.5+self.img_save_game.crop_w*0.5+2,
								             self.menu_pos[1]+self.menu_rect.h*0.75-self.img_delete_game.crop_h*0.5),
								hover_on=True, img=self.img_delete_game.sheet.subsurface(self.img_delete_game.crops[0]),
								img_hover=self.img_delete_game.sheet.subsurface(self.img_delete_game.crops[1]),
								img_pressed=self.img_delete_game.sheet.subsurface(self.img_delete_game.crops[2]))},
				'load_game_buttons': {
						'save_game1': Button(
								screen, pos=(self.menu_pos[0]+self.menu_rect.w*0.5-self.img_save_game.crop_w*0.5,
								             self.menu_pos[1]+self.menu_rect.h*0.15-self.img_save_game.crop_h*0.5),
								img=self.img_save_game.sheet.subsurface(self.img_save_game.crops[0]),
								img_pressed=self.img_save_game.sheet.subsurface(self.img_save_game.crops[1])),
						'save_game2': Button(
								screen, pos=(self.menu_pos[0]+self.menu_rect.w*0.5-self.img_save_game.crop_w*0.5,
								             self.menu_pos[1]+self.menu_rect.h*0.35-self.img_save_game.crop_h*0.5),
								img=self.img_save_game.sheet.subsurface(self.img_save_game.crops[0]),
								img_pressed=self.img_save_game.sheet.subsurface(self.img_save_game.crops[1])),
						'save_game3': Button(
								screen, pos=(self.menu_pos[0]+self.menu_rect.w*0.5-self.img_save_game.crop_w*0.5,
								             self.menu_pos[1]+self.menu_rect.h*0.55-self.img_save_game.crop_h*0.5),
								img=self.img_save_game.sheet.subsurface(self.img_save_game.crops[0]),
								img_pressed=self.img_save_game.sheet.subsurface(self.img_save_game.crops[1])),
						'save_game4': Button(
								screen, pos=(self.menu_pos[0]+self.menu_rect.w*0.5-self.img_save_game.crop_w*0.5,
								             self.menu_pos[1]+self.menu_rect.h*0.75-self.img_save_game.crop_h*0.5),
								img=self.img_save_game.sheet.subsurface(self.img_save_game.crops[0]),
								img_pressed=self.img_save_game.sheet.subsurface(self.img_save_game.crops[1]))},
				'saved_game_text': {'save_game1': None, 'save_game2': None, 'save_game3': None, 'save_game4': None},
				'sound_on': Button(
						screen, pos=self.menu_but_imgs['sound_on'].get_rect(
								center=(self.menu_pos[0]+self.menu_rect.w*0.5, self.menu_pos[1]+self.menu_rect.h*0.1)),
						hover_on=True, img=self.menu_but_imgs['sound_on'],
						img_hover=text('Sound on', font_style=info_font, font_size=30, color=col_white)[0],
						img_pressed=text('Sound on', font_style=info_font, font_size=30, color=col_grey)[0]),
				'sound_off': Button(
						screen, pos=self.menu_but_imgs['sound_off'].get_rect(
								center=(self.menu_pos[0]+self.menu_rect.w*0.5, self.menu_pos[1]+self.menu_rect.h*0.1)),
						hover_on=True, img=self.menu_but_imgs['sound_off'],
						img_hover=text('Sound off', font_style=info_font, font_size=30, color=col_white)[0],
						img_pressed=text('Sound off', font_style=info_font, font_size=30, color=col_grey)[0]),
				'back': Button(screen, pos=self.menu_but_imgs['back'].get_rect(
						center=(self.menu_pos[0]+self.menu_rect.w*0.5, self.menu_pos[1]+self.menu_rect.h*0.9)),
						hover_on=True, img=self.menu_but_imgs['back'],
						img_hover=text('Back', font_style=info_font, font_size=30, color=col_white)[0],
						img_pressed=text('Back', font_style=info_font, font_size=30, color=col_grey)[0])
		}

		# GUI background #
		if sett.current_game['settings']['gui_bg_option'] == 1:
			self.img_gui_bg_chosen = self.img_gui_bg1
			self.gui_bg_pos = (0, 608)
		self.gui_bg_rect = pg.Rect(self.gui_bg_pos[0], self.gui_bg_pos[1],
		                           self.img_gui_bg_chosen.get_width(), self.img_gui_bg_chosen.get_height())

		# Message box #
		self.messages = []
		self.messages_surfaces = []
		self.text_length = 45

		# Status bars #
		self.glass_bar_rect = pg.Rect(0, 0, self.img_glass_bar.get_width(), self.img_glass_bar.get_height())
		self.inner_bar_rect = self.img_hp_bar.get_rect()
		self.space_between_bars = 10
		self.hp_glass_pos = (202, 645)
		self.mp_glass_pos = (self.hp_glass_pos[0]+self.glass_bar_rect.width+self.space_between_bars,
		                     self.hp_glass_pos[1])
		self.vigor_glass_pos = (self.hp_glass_pos[0]+self.glass_bar_rect.width*2+self.space_between_bars*2,
		                        self.hp_glass_pos[1])
		self.spirit_bar_pos = (718, 655)

		self.stat_rects = {
				'health': pg.Rect(self.hp_glass_pos[0], self.hp_glass_pos[1],
				                  self.glass_bar_rect.width, self.glass_bar_rect.height),
				'mana': pg.Rect(self.mp_glass_pos[0], self.mp_glass_pos[1],
		                             self.glass_bar_rect.width, self.glass_bar_rect.height),
				'vigor': pg.Rect(self.vigor_glass_pos[0], self.vigor_glass_pos[1],
		                                self.glass_bar_rect.width, self.glass_bar_rect.height),
				'spirit': pg.Rect(self.spirit_bar_pos[0], self.spirit_bar_pos[1],
		                               self.img_spirit_bar.get_width(), self.img_spirit_bar.get_height()),
				'meditation': pg.Rect(self.spirit_bar_pos[0]+43, self.spirit_bar_pos[1]+39, 14, 14)}

		# Status states #
		self.hp_pct, self.mp_pct, self.vigor_pct = \
			int(sett.current_game['current_char'].chstats['health']*100/sett.current_game['current_char'].chstats['max_hp']), \
			int(sett.current_game['current_char'].chstats['mana']*100/sett.current_game['current_char'].chstats['max_mp']), \
			int(sett.current_game['current_char'].chstats['vigor']*100/sett.current_game['current_char'].chstats['max_vigor'])
		self.last_hp_pct, self.last_mp_pct, self.last_vigor_pct = self.hp_pct, self.mp_pct, self.vigor_pct
		self.hp_change, self.mp_change, self.vigor_change = False, False, False
		self.blinking_threshold = 25
		self.low_hp_counter = 0
		self.spirit_halo_alpha = 0
		self.spirit_halo_start = True
		self.spirit_halo_alpha_up, self.spirit_halo_alpha_down = True, False

		self.hover_hp, self.hover_mp, self.hover_vigor = False, False, False
		self.stat_txt_surfaces = {}

		# Portrait #
		self.portrait_pos = (self.gui_bg_pos[0]+20, self.gui_bg_pos[1]+18)
		if sett.current_game['current_char'].char_class == 'adventurer':
			self.img_portrait = self.img_portrait1

		self.item_on_cursor = None

	def draw_gui(self):
		"""Centralizes all the GUI displaying"""

		screen.blit(self.img_gui_bg_chosen, self.gui_bg_pos)
		self.msg_box()
		screen.blit(self.img_portrait, self.portrait_pos)
		self.update_stats()
		self.draw_bars()
		self.draw_gui_buttons()

		for win in reversed(opened_windows):
			win.draw_window()

		self.draw_info_panel()

		if sett.current_game['current_container'] is None:
			if IOLootContainer.active_window:
				IOLootContainer.close_win = True
				if sett.current_game['previous_container'] is not None:
					sett.current_game['previous_container'].opened = False

	def draw_menu(self, main_menu=False):
		"""Displays the menu if opened"""

		if main_menu:
			if self.menu_active:
				screen.blit(self.img_menu_bg, self.menu_pos)
				self.draw_menu_buttons()
		else:
			if self.menu_active:
				sett.current_game['current_char'].stop_movement()
				IOAtlas.fade_bg('in')
				IOAtlas.fading['menu'] = 'in'
				if IOAtlas.opacity_counter >= 200:
					IOAtlas.fading['menu'] = 'out'
				screen.blit(self.img_menu_bg, self.menu_pos)
				self.draw_menu_buttons()
			else:
				if IOAtlas.fading['menu'] == 'out':
					IOAtlas.fade_bg('out')
					if IOAtlas.opacity_counter <= 0:
						IOAtlas.fading['menu'] = 'off'

			IOGUI.ingame_menu_button.draw_button()

	def draw_menu_buttons(self):
		"""Displays the menu buttons"""

		if self.menu_layer == 'main':
			self.menu_but['resume'].draw_button()
			self.menu_but['save'].draw_button()
			self.menu_but['load'].draw_button()
			self.menu_but['settings'].draw_button()
			self.menu_but['main_menu'].draw_button()

		elif self.menu_layer == 'save':
			self.check_saved_games()
			for socket in self.menu_but['save_game_buttons'].keys():
				self.menu_but['save_game_buttons'][socket].draw_button()
				if sett.save_sockets[socket] is not None:
					self.menu_but['delete_game'][socket].draw_button()
					pos = [self.menu_but['save_game_buttons'][socket].pos[0]+90, self.menu_but['save_game_buttons'][socket].pos[1]+10]
					for surf in self.menu_but['saved_game_text'][socket]:
						screen.blit(surf, pos)
						pos[1] += surf.get_height()+2
			self.menu_but['back'].draw_button()

		elif self.menu_layer == 'load':
			self.check_saved_games()
			for socket in self.menu_but['load_game_buttons'].keys():
				self.menu_but['load_game_buttons'][socket].draw_button()
				if sett.save_sockets[socket] is not None:
					pos = [self.menu_but['save_game_buttons'][socket].pos[0]+90, self.menu_but['save_game_buttons'][socket].pos[1]+10]
					for surf in self.menu_but['saved_game_text'][socket]:
						screen.blit(surf, pos)
						pos[1] += surf.get_height()+2
			self.menu_but['back'].draw_button()

		elif self.menu_layer == 'settings':
			if sett.current_game['settings']['sound_active']: self.menu_but['sound_on'].draw_button()
			else: self.menu_but['sound_off'].draw_button()
			self.menu_but['back'].draw_button()

	def check_saved_games(self):
		"""Checks the saved games and changes save buttons (green or orange)"""

		for socket in sett.save_sockets.keys():
			if os.path.isfile('saves/'+socket+'.dgn'):
				sett.save_sockets[socket] = loadgame(socket)

				self.menu_but['saved_game_text'][socket] = text(
						f'{sett.save_sockets[socket]["current_char"].char_name} ('
						f'{sett.save_sockets[socket]["current_char"].char_class})$'
						f'{readable_text(sett.save_sockets[socket]["current_map"].name, "_")}$'
						f'{sett.save_sockets[socket]["date_time"]}',
						font_style=info_font, font_size=15, color=col_white)
				self.menu_but['save_game_buttons'][socket].img, self.menu_but['save_game_buttons'][socket].img_pressed =\
					self.img_save_game.sheet.subsurface(self.img_save_game.crops[2]),\
					self.img_save_game.sheet.subsurface(self.img_save_game.crops[3])
				self.menu_but['load_game_buttons'][socket].img, self.menu_but['load_game_buttons'][socket].img_pressed =\
					self.img_save_game.sheet.subsurface(self.img_save_game.crops[0]),\
					self.img_save_game.sheet.subsurface(self.img_save_game.crops[1])
			else:
				self.menu_but['save_game_buttons'][socket].img, self.menu_but['save_game_buttons'][socket].img_pressed =\
					self.img_save_game.sheet.subsurface(self.img_save_game.crops[0]),\
					self.img_save_game.sheet.subsurface(self.img_save_game.crops[1])
				self.menu_but['load_game_buttons'][socket].img, self.menu_but['load_game_buttons'][socket].img_pressed =\
					self.img_save_game.sheet.subsurface(self.img_save_game.crops[4]),\
					self.img_save_game.sheet.subsurface(self.img_save_game.crops[4])

	def menu(self, action, socket=None):
		"""Receives different menu actions"""

		if action == 'open':
			self.menu_active = True
		elif action == 'close':
			self.menu_layer = 'main'
			sett.active_screen = 'game'
			self.menu_active = False
		elif action == 'main_menu':
			sett.active_screen = 'main_menu'
		elif action == 'save_game':
			self.save_game(socket)
			self.message('Game saved')
		elif action == 'load_game':
			sett.current_game['current_char'].stat_modify = True
			self.load_game(socket)
			self.message('Game Loaded')
		elif action == 'sound_on':
			sett.current_game['settings']['sound_active'] = True
		elif action == 'sound_off':
			sett.current_game['settings']['sound_active'] = False
		else:
			self.menu_layer = action

	@staticmethod
	def save_game(socket):
		"""Checks if socket available to save the game"""

		sett.current_game['date_time'] = datetime.datetime.now().strftime("%H:%M  %d/%m/%Y")
		sett.save_sockets[socket] = sett.current_game
		savegame(sett.save_sockets[socket], socket)

	@staticmethod
	def load_game(socket):
		"""Checks if any saved game to load it"""

		# sett.save_sockets[socket] = loadgame(socket)
		sett.current_game = sett.save_sockets[socket]
		IOAtlas.explore_area()

	def msg_box(self):
		"""Displays every messages list element as a line into the message box"""

		msg_box_pos = (self.gui_bg_rect.w*0.5-self.img_msg_box.get_width()*0.5, self.gui_bg_pos[1]+30)
		screen.blit(self.img_msg_box, msg_box_pos)
		if len(self.messages) >= 6:
			blit_alpha(screen, self.messages[-6], (msg_box_pos[0]+80, msg_box_pos[1]+22-3), 120)
			blit_alpha(screen, self.messages[-5], (msg_box_pos[0]+80, msg_box_pos[1]+32-2), 180)
			blit_alpha(screen, self.messages[-4], (msg_box_pos[0]+80, msg_box_pos[1]+42-1), 255)
			blit_alpha(screen, self.messages[-3], (msg_box_pos[0]+80, msg_box_pos[1]+52+0), 255)
			blit_alpha(screen, self.messages[-2], (msg_box_pos[0]+80, msg_box_pos[1]+62+1), 255)
			blit_alpha(screen, self.messages[-1], (msg_box_pos[0]+80, msg_box_pos[1]+72+2), 255)
		elif len(self.messages) >= 5:
			blit_alpha(screen, self.messages[-5], (msg_box_pos[0]+80, msg_box_pos[1]+32-2), 180)
			blit_alpha(screen, self.messages[-4], (msg_box_pos[0]+80, msg_box_pos[1]+42-1), 255)
			blit_alpha(screen, self.messages[-3], (msg_box_pos[0]+80, msg_box_pos[1]+52+0), 255)
			blit_alpha(screen, self.messages[-2], (msg_box_pos[0]+80, msg_box_pos[1]+62+1), 255)
			blit_alpha(screen, self.messages[-1], (msg_box_pos[0]+80, msg_box_pos[1]+72+2), 255)
		elif len(self.messages) >= 4:
			blit_alpha(screen, self.messages[-4], (msg_box_pos[0]+80, msg_box_pos[1]+42-1), 255)
			blit_alpha(screen, self.messages[-3], (msg_box_pos[0]+80, msg_box_pos[1]+52+0), 255)
			blit_alpha(screen, self.messages[-2], (msg_box_pos[0]+80, msg_box_pos[1]+62+1), 255)
			blit_alpha(screen, self.messages[-1], (msg_box_pos[0]+80, msg_box_pos[1]+72+2), 255)
		elif len(self.messages) >= 3:
			blit_alpha(screen, self.messages[-3], (msg_box_pos[0]+80, msg_box_pos[1]+52+0), 255)
			blit_alpha(screen, self.messages[-2], (msg_box_pos[0]+80, msg_box_pos[1]+62+1), 255)
			blit_alpha(screen, self.messages[-1], (msg_box_pos[0]+80, msg_box_pos[1]+72+2), 255)
		elif len(self.messages) >= 2:
			blit_alpha(screen, self.messages[-2], (msg_box_pos[0]+80, msg_box_pos[1]+62+1), 255)
			blit_alpha(screen, self.messages[-1], (msg_box_pos[0]+80, msg_box_pos[1]+72+2), 255)
		elif len(self.messages) >= 1:
			blit_alpha(screen, self.messages[-1], (msg_box_pos[0]+80, msg_box_pos[1]+72+2), 255)

	def update_stats(self):
		"""Updates some stat related variables"""

		if sett.current_game['current_char'].stat_modify:
			IOEqu.update_sub_win()
			self.stat_txt_surfaces = {
					'hp': text(f'{int(sett.current_game["current_char"].chstats["health"])}', sett.info_font, 10, col_green_lime),
					'mp': text(f'{int(sett.current_game["current_char"].chstats["mana"])}', sett.info_font, 10, col_green_lime),
					'vp': text(f'{int(sett.current_game["current_char"].chstats["vigor"])}', sett.info_font, 10, col_green_lime),
					'health': text(
							f'Health:${int(sett.current_game["current_char"].chstats["health"])}/'
							f'{int(sett.current_game["current_char"].chstats["max_hp"])}',
							font_style=sett.info_font, font_size=15, color=col_white),
					'mana': text(
							f'Mana:${int(sett.current_game["current_char"].chstats["mana"])}/'
							f'{int(sett.current_game["current_char"].chstats["max_mp"])}',
							font_style=sett.info_font, font_size=15, color=col_white),
					'vigor': text(
							f'Vigor:${int(sett.current_game["current_char"].chstats["vigor"])}/'
							f'{int(sett.current_game["current_char"].chstats["max_vigor"])}',
							font_style=sett.info_font, font_size=15, color=col_white),
					'spirit': text(
							f'Spirit:${int(sett.current_game["current_char"].chstats["spirit"])}/'
							f'{int(sett.current_game["current_char"].chstats["max_spirit"])}',
							font_style=sett.info_font, font_size=15, color=col_white),
					'meditation': text(f'Ready for meditation', font_style=info_font, font_size=10, color=col_grey)}
			sett.current_game['current_char'].stat_modify = False

		self.hp_pct = int(
				sett.current_game['current_char'].chstats['health']*100/sett.current_game['current_char'].chstats['max_hp'])
		self.mp_pct = int(
				sett.current_game['current_char'].chstats['mana']*100/sett.current_game['current_char'].chstats['max_mp'])
		self.vigor_pct = int(
				sett.current_game['current_char'].chstats['vigor']*100/sett.current_game['current_char'].chstats['max_vigor'])

	def draw_bars(self):
		"""Displays the stat bars (hp, mp, vigor and spirit) on the User Interface background"""

		def show_remaining(stat):
			"""Displays the text of the remaining provided stat over its bar"""

			txt = self.stat_txt_surfaces[stat]
			txt_rect = txt[0].get_rect()

			if stat == 'hp':
				txt_rect.center = (self.hp_glass_pos[0]+self.glass_bar_rect.width*0.5,
				                   self.hp_glass_pos[1]+self.glass_bar_rect.height*0.5)
			elif stat == 'mp':
				txt_rect.center = (self.mp_glass_pos[0]+self.glass_bar_rect.width*0.5,
				                   self.mp_glass_pos[1]+self.glass_bar_rect.height*0.5)
			elif stat == 'vp':
				txt_rect.center = (self.vigor_glass_pos[0]+self.glass_bar_rect.width*0.5,
				                   self.vigor_glass_pos[1]+self.glass_bar_rect.height*0.5)

			screen.blit(txt[0], (txt_rect.x, txt_rect.y))

		# HP bar #
		if self.hp_pct != self.last_hp_pct: self.hp_change = True
		else: self.hp_change = False

		if self.hp_change:
			self.draw_stat_bar(self.img_hp_bar, self.hp_glass_pos, self.hp_pct, self.last_hp_pct, stat_changing='hp')
		else:
			self.draw_stat_bar(self.img_hp_bar, self.hp_glass_pos, self.hp_pct)

		if not self.hover_hp:
			show_remaining('hp')

		# MP bar #
		if self.mp_pct != self.last_mp_pct: self.mp_change = True
		else: self.mp_change = False

		if self.mp_change:
			self.draw_stat_bar(self.img_mp_bar, self.mp_glass_pos, self.mp_pct, self.last_mp_pct, stat_changing='mp')
		else:
			self.draw_stat_bar(self.img_mp_bar, self.mp_glass_pos, self.mp_pct)

		if not self.hover_mp:
			show_remaining('mp')

		# Vigor bar #
		if self.vigor_pct != self.last_vigor_pct: self.vigor_change = True
		else: self.vigor_change = False

		if self.vigor_change:
			self.draw_stat_bar(self.img_vigor_bar, self.vigor_glass_pos, self.vigor_pct, self.last_vigor_pct,
			                   stat_changing='vigor')
		else:
			self.draw_stat_bar(self.img_vigor_bar, self.vigor_glass_pos, self.vigor_pct)

		if not self.hover_vigor:
			show_remaining('vp')

		# Spirit bar #
		screen.blit(self.img_spirit_bar, self.spirit_bar_pos)
		screen.blit(self.img_spirit_inner_bar.sheet, self.spirit_bar_pos,
		            self.img_spirit_inner_bar.crops[sett.current_game['current_char'].chstats['spirit']])

		# Meditation halo setting #
		if sett.current_game['current_char'].meditation_ready:
			if self.spirit_halo_start:
				self.spirit_halo_alpha = 0
				self.spirit_halo_start = False
			else:
				if self.spirit_halo_alpha_up:
					self.spirit_halo_alpha += 5
				elif self.spirit_halo_alpha_down:
					self.spirit_halo_alpha -= 5

				# Alpha limits #
				if self.spirit_halo_alpha >= 150:
					self.spirit_halo_alpha = 150
					self.spirit_halo_alpha_up, self.spirit_halo_alpha_down = False, True
				if self.spirit_halo_alpha <= 0:
					self.spirit_halo_alpha = 0
					self.spirit_halo_alpha_up, self.spirit_halo_alpha_down = True, False

			blit_alpha(screen, self.img_spirit_halo, self.spirit_bar_pos, self.spirit_halo_alpha)

		else: self.spirit_halo_start = True

	def draw_stat_bar(self, img_stat_bar, stat_glass_pos, stat_pct, last_stat_pct=None, stat_changing=None):
		"""Displays the stat bar status and animates it if there is a change"""

		if self.hp_pct <= self.blinking_threshold: low_hp = True
		else: low_hp = False

		if stat_changing is not None:
			change_stat_speed = 1

			screen.blit(img_stat_bar, (
					stat_glass_pos[0]+5, stat_glass_pos[1]+5+(100-last_stat_pct)*self.inner_bar_rect.height/100), (
					0, ((100-last_stat_pct)*self.inner_bar_rect.height/100), self.inner_bar_rect.width,
					self.inner_bar_rect.height-(100-last_stat_pct)*self.inner_bar_rect.height/100))
			screen.blit(self.img_glass_bar, stat_glass_pos)
			if last_stat_pct < stat_pct:
				if stat_changing == 'hp':
					self.last_hp_pct += change_stat_speed
					if self.last_hp_pct > stat_pct: self.last_hp_pct = stat_pct
				elif stat_changing == 'mp':
					self.last_mp_pct += change_stat_speed
					if self.last_mp_pct > stat_pct: self.last_mp_pct = stat_pct
				elif stat_changing == 'vigor':
					self.last_vigor_pct += change_stat_speed
					if self.last_vigor_pct > stat_pct: self.last_vigor_pct = stat_pct

			elif last_stat_pct > stat_pct:
				if stat_changing == 'hp':
					self.last_hp_pct -= change_stat_speed
					if self.last_hp_pct < stat_pct: self.last_hp_pct = stat_pct
				elif stat_changing == 'mp':
					self.last_mp_pct -= change_stat_speed
					if self.last_mp_pct < stat_pct: self.last_mp_pct = stat_pct
				elif stat_changing == 'vigor':
					self.last_vigor_pct -= change_stat_speed
					if self.last_vigor_pct < stat_pct: self.last_vigor_pct = stat_pct

		else:
			# Blinking bar when low HP #
			if img_stat_bar == self.img_hp_bar:
				if low_hp:
					if self.low_hp_counter <= 20:
						screen.blit(img_stat_bar, (
								stat_glass_pos[0]+5, stat_glass_pos[1]+5+(100-stat_pct)*self.inner_bar_rect.height/100), (
								0, ((100-stat_pct)*self.inner_bar_rect.height/100), self.inner_bar_rect.width,
								self.inner_bar_rect.height-(100-stat_pct)*self.inner_bar_rect.height/100))
					self.low_hp_counter += 1
					if self.low_hp_counter > 40: self.low_hp_counter = 0
				else:
					screen.blit(img_stat_bar, (
							stat_glass_pos[0]+5, stat_glass_pos[1]+5+(100-stat_pct)*self.inner_bar_rect.height/100), (
							0, ((100-stat_pct)*self.inner_bar_rect.height/100), self.inner_bar_rect.width,
							self.inner_bar_rect.height-(100-stat_pct)*self.inner_bar_rect.height/100))
			else:
				screen.blit(img_stat_bar, (
						stat_glass_pos[0]+5, stat_glass_pos[1]+5+(100-stat_pct)*self.inner_bar_rect.height/100), (
						0, ((100-stat_pct)*self.inner_bar_rect.height/100), self.inner_bar_rect.width,
						self.inner_bar_rect.height-(100-stat_pct)*self.inner_bar_rect.height/100))

			screen.blit(self.img_glass_bar, stat_glass_pos)

	@staticmethod
	def draw_gui_buttons():
		"""Displays every GUI button"""

		IOEqu.gui_button.draw_button()
		IOInv.gui_button.draw_button()

	def draw_info_panel(self):
		"""Displays the info panel when hovers with cursor"""

		def set_panel_size(surf, panel_sz, borders, interl):
			"""Sets a proper size for every displayed panel"""

			panel_size = panel_sz

			if surf.get_width() > panel_size[0]-borders[0]*2:
				panel_size[0] = surf.get_width()+borders[0]*2
			panel_size[1] += surf.get_height()+interl

			return panel_size

		def set_panel_limits(pos, panel_sz):
			"""Sets limits to the information panel position"""

			position = [pos[0], pos[1]]

			if position[0] > disp_w-panel_sz[0]:
				position[0] = disp_w-panel_sz[0]
			if position[1] > disp_h-self.gui_bg_rect.h-panel_sz[1]:
				position[1] = disp_h-self.gui_bg_rect.h-panel_sz[1]

			return position

		def equ_info_panel(item_type):
			item = sett.current_game['equipped'][item_type]
			border_w, border_h, interline = 8, 4, 3
			panel_pos = (IOEqu.equ_rects[item_type].x+32, IOEqu.equ_rects[item_type].y+32)
			panel_size = [0, border_h*2]

			if item is not None:
				for stat_surf in item_info[item.uuid]:
					panel_size = set_panel_size(surf=stat_surf, panel_sz=panel_size,
					                            borders=(border_w, border_h), interl=interline)

				panel_pos = set_panel_limits(pos=panel_pos, panel_sz=panel_size)
				blit_alpha(screen, self.img_info_bg, panel_pos, 200, (0, 0, panel_size[0], panel_size[1]))

				# Center aligning #
				title = True
				quality = True

				txt_pos = [panel_pos[0]+border_w, panel_pos[1]+border_h]
				for stat_surf in item_info[item.uuid]:
					if title:
						screen.blit(stat_surf, (panel_pos[0]+panel_size[0]*0.5-stat_surf.get_width()*0.5, txt_pos[1]))
						title = False
					elif quality:
						screen.blit(stat_surf, (panel_pos[0]+panel_size[0]*0.5-stat_surf.get_width()*0.5, txt_pos[1]-5))
						quality = False
					else:
						screen.blit(stat_surf, txt_pos)
					txt_pos[1] += stat_surf.get_height()+interline

		def inv_info_panel(cell_coord):
			item = sett.current_game['inv_items'][cell_coord]
			border_w, border_h, interline = 8, 4, 3
			panel_pos = (IOInv.inv_rects[cell_coord].x+32, IOInv.inv_rects[cell_coord].y+32)
			panel_size = [0, border_h*2]

			if sett.current_game['inv_items'][cell_coord] is not None and sett.current_game['inv_items'][cell_coord] != 'locked':
				for stat_surf in item_info[item.uuid]:
					panel_size = set_panel_size(surf=stat_surf, panel_sz=panel_size,
					                            borders=(border_w, border_h), interl=interline)

				panel_pos = set_panel_limits(pos=panel_pos, panel_sz=panel_size)
				blit_alpha(screen, self.img_info_bg, panel_pos, 200, (0, 0, panel_size[0], panel_size[1]))

				title = True
				quality = True

				txt_pos = [panel_pos[0]+border_w, panel_pos[1]+border_h]
				for stat_surf in item_info[item.uuid]:
					if title:
						screen.blit(stat_surf, (panel_pos[0]+panel_size[0]*0.5-stat_surf.get_width()*0.5, txt_pos[1]))
						title = False
					elif quality:
						screen.blit(stat_surf, (panel_pos[0]+panel_size[0]*0.5-stat_surf.get_width()*0.5, txt_pos[1]-5))
						quality = False
					else:
						screen.blit(stat_surf, txt_pos)
					txt_pos[1] += stat_surf.get_height()+interline

		def loot_combat_info_panel(cell_coord):

			item = IOLootCombat.loot_buffer[cell_coord]
			border_w, border_h, interline = 8, 4, 3
			panel_pos = (IOLootCombat.loot_rects[cell_coord].x+32, IOLootCombat.loot_rects[cell_coord].y+32)
			panel_size = [0, border_h*2]

			if item is not None:
				for stat_surf in item_info[item.uuid]:
					panel_size = set_panel_size(surf=stat_surf, panel_sz=panel_size,
					                            borders=(border_w, border_h), interl=interline)

				panel_pos = set_panel_limits(pos=panel_pos, panel_sz=panel_size)
				blit_alpha(screen, self.img_info_bg, panel_pos, 200, (0, 0, panel_size[0], panel_size[1]))

				title = True
				quality = False

				txt_pos = [panel_pos[0]+border_w, panel_pos[1]+border_h]
				for stat_surf in item_info[item.uuid]:
					if title:
						screen.blit(stat_surf, (panel_pos[0]+panel_size[0]*0.5-stat_surf.get_width()*0.5, txt_pos[1]))
						title = False
						quality = True
					elif quality:
						screen.blit(stat_surf, (panel_pos[0]+panel_size[0]*0.5-stat_surf.get_width()*0.5, txt_pos[1]-5))
						quality = False
					else:
						screen.blit(stat_surf, txt_pos)
					txt_pos[1] += stat_surf.get_height()+interline

		def loot_container_info_panel(cell_coord):
			if sett.current_game['current_container'] is not None:
				item = sett.current_game['current_container'].loot_items[cell_coord]
				border_w, border_h, interline = 8, 4, 3
				panel_pos = (IOLootContainer.loot_rects[cell_coord].x+32, IOLootContainer.loot_rects[cell_coord].y+32)
				panel_size = [0, border_h*2]

				if item is not None:
					for stat_surf in item_info[item.uuid]:
						panel_size = set_panel_size(surf=stat_surf, panel_sz=panel_size,
						                            borders=(border_w, border_h), interl=interline)

					panel_pos = set_panel_limits(pos=panel_pos, panel_sz=panel_size)
					blit_alpha(screen, self.img_info_bg, panel_pos, 200, (0, 0, panel_size[0], panel_size[1]))

					title = True
					quality = False

					txt_pos = [panel_pos[0]+border_w, panel_pos[1]+border_h]
					for stat_surf in item_info[item.uuid]:
						if title:
							screen.blit(stat_surf, (panel_pos[0]+panel_size[0]*0.5-stat_surf.get_width()*0.5, txt_pos[1]))
							title = False
							quality = True
						elif quality:
							screen.blit(stat_surf, (panel_pos[0]+panel_size[0]*0.5-stat_surf.get_width()*0.5, txt_pos[1]-5))
							quality = False
						else:
							screen.blit(stat_surf, txt_pos)
						txt_pos[1] += stat_surf.get_height()+interline

		def bar_info_panel(stat):
			border_w, border_h, interline = 2, 0, 0
			panel_size = [0, border_h*2]

			for surf in self.stat_txt_surfaces[stat]:
				panel_size = set_panel_size(surf=surf, panel_sz=panel_size,
				                            borders=(border_w, border_h), interl=interline)

			panel_pos = (self.stat_rects[stat].x+self.stat_rects[stat].width*0.5-panel_size[0]*0.5,
			             self.stat_rects[stat].y-panel_size[1]-4)
			blit_alpha(screen, self.img_info_bg, panel_pos, 150, (0, 0, panel_size[0], panel_size[1]))

			txt_pos = [0, panel_pos[1]+border_h]
			for surf in self.stat_txt_surfaces[stat]:
				txt_pos[0] = panel_pos[0]+panel_size[0]*0.5-surf.get_width()*0.5
				screen.blit(surf, txt_pos)
				txt_pos[1] += surf.get_height()+interline

		def meditation_panel():
			border_w, border_h, interline = 2, 0, 0
			panel_size = [0, border_h*2]
			surf = self.stat_txt_surfaces['meditation'][0]

			panel_size = set_panel_size(surf=surf, panel_sz=panel_size, borders=(border_w, border_h),
			                            interl=interline)

			panel_pos = (self.spirit_bar_pos[0]+self.stat_rects['spirit'].width*0.5-panel_size[0]*0.5,
			             self.spirit_bar_pos[1]+self.stat_rects['spirit'].height-panel_size[1])
			blit_alpha(screen, self.img_info_bg, panel_pos, 150, (0, 0, panel_size[0], panel_size[1]))

			txt_pos = [panel_pos[0]+panel_size[0]*0.5-surf.get_width()*0.5, panel_pos[1]+border_h]
			screen.blit(surf, txt_pos)

		if sett.active_screen == 'game':

			win_collision = []
			if len(opened_windows) > 0:
				for index, win in enumerate(opened_windows):
					if win.rect.collidepoint(sett.mouse_pos): win_collision.append(win)
			if len(win_collision) > 0:
				if win_collision[0] == IOEqu:
					for itype, equ_rect in IOEqu.equ_rects.items():
						if equ_rect.collidepoint(sett.mouse_pos):
							equ_info_panel(itype)
							break

				elif win_collision[0] == IOInv:
					for cell, inv_rect in IOInv.inv_rects.items():
						if inv_rect.collidepoint(sett.mouse_pos):
							inv_info_panel(cell)
							break

				elif win_collision[0] == IOLootCombat:
					for cell, loot_rect in IOLootCombat.loot_rects.items():
						if loot_rect.collidepoint(sett.mouse_pos):
							loot_combat_info_panel(cell)
							break

				elif win_collision[0] == IOLootContainer:
					for cell, loot_rect in IOLootContainer.loot_rects.items():
						if loot_rect.collidepoint(sett.mouse_pos):
							loot_container_info_panel(cell)
							break

			if self.stat_rects['spirit'].collidepoint(sett.mouse_pos):
				bar_info_panel('spirit')
			if self.stat_rects['meditation'].collidepoint(sett.mouse_pos):
				if sett.current_game['current_char'].meditation_ready:
					meditation_panel()

		if sett.active_screen == 'game' or sett.active_screen == 'combat':
			if self.stat_rects['health'].collidepoint(sett.mouse_pos):
				self.hover_hp = True
				bar_info_panel('health')
			elif self.stat_rects['mana'].collidepoint(sett.mouse_pos):
				self.hover_mp = True
				bar_info_panel('mana')
			elif self.stat_rects['vigor'].collidepoint(sett.mouse_pos):
				self.hover_vigor = True
				bar_info_panel('vigor')
			else:
				self.hover_hp, self.hover_mp, self.hover_vigor = False, False, False

	def draw_cursor(self):
		"""Displays the mouse cursor or the item_on_cursor"""

		if self.item_on_cursor is None:
			mouse_visible(surface=screen, image=cursor, mouse_pos=sett.mouse_pos)
		else:
			self.item_on_cursor.draw_single_item(sett.mouse_pos)
			if IOInv.active_window:
				del_text_pos = (IOInv.pos[0]+IOInv.rect.w*0.5, IOInv.pos[1]+IOInv.rect.h*0.9)
				BlinkingText.show_blinking_text(screen, 'Press DEL key to delete the item',
				                                del_text_pos, info_font, 14, col_white, 5)

	def message(self, msg, type=None):
		"""Adds msg to the messages list so it can be displayed into the message box
		If multiple lines are given (separator: '$'), divides them in different list objects"""

		if type == 'thought':
			message = '*'+msg+'*'
			for line in text(message, info_font, 11, col_green, self.text_length):
				self.messages.append(line)
		elif type == 'combat':
			message = '<'+msg+'>'
			for line in text(message, info_font, 11, col_black, self.text_length):
				self.messages.append(line)
		else:
			message = '  '+msg
			for line in text(message, info_font, 11, col_blue_navy, self.text_length):
				self.messages.append(line)


IOGUI = GraphicalUserInterface()


class GUIWindow:
	def __init__(self, size='default', movable=True):

		self.img_gui_win = pg.image.load('data/images/gui/gui_win.png').convert_alpha()
		self.img_locked_cell = pg.image.load('data/images/gui/locked.png').convert_alpha()

		# General #
		self.surface = screen
		self.size = size
		self.img_gui = None
		if size == 'small':
			self.img_gui_win = pg.image.load('data/images/gui/gui_win_small.png').convert_alpha()
		self.pos_rel = (0, 0)
		self.pos = [0, 0]
		self.rect = self.img_gui_win.get_rect()
		self.movable = movable
		self.active_window = False
		self.focused_window = False

		self.gui_button = None
		self.cell_size = (32, 32)

		# Closing window #
		self.img_button_close = pg.image.load('data/images/gui/button_close.png').convert_alpha()
		self.close_pos_rel = (239, 9)
		if size == 'small':
			self.close_pos_rel = (125, 11)
		self.close_rect = self.img_button_close.get_rect()
		self.close_pressed = False
		self.close_win = False
		self.close_count = 0

		# Move window #
		self.move_win_pos_rel = (68, 9)
		self.move_win_rect = pg.Rect(self.move_win_pos_rel[0], self.move_win_pos_rel[1], 140, 38)
		if size == 'small':
			self.move_win_pos_rel = (30, 8)
			self.move_win_rect = pg.Rect(self.move_win_pos_rel[0], self.move_win_pos_rel[1], 84, 35)
		self.move_win_pressed = False
		self.mouse_pos_rel = (0, 0)

		# Misc #
		self.equ_rects = {}

		self.inv_rects = {}

		self.loot_rects = {}
		self.loot_buffer = {}

		self.stat_slab_rect = None
		self.slab_stats = []
		self.stat_positions = []

	def update_window(self):
		"""Updates some variables after a change in the window position"""

		self.rect[0], self.rect[1] = self.pos[0], self.pos[1]
		self.close_rect[0], self.close_rect[1] = self.pos[0]+self.close_pos_rel[0], self.pos[1]+self.close_pos_rel[1]
		self.move_win_rect[0], self.move_win_rect[1] = \
			self.pos[0]+self.move_win_pos_rel[0], self.pos[1]+self.move_win_pos_rel[1]

		self.update_sub_win()

	def update_sub_win(self):
		"""Default sub window method"""

	def open_window(self):
		"""Opens the 'self' window with its content (sub_window, gui_button...)"""

		if self == IOLootCombat:
			self.loot_buffer = sett.current_game['current_creature'].loot_items
			self.pos = [sett.mouse_pos[0]-self.pos_rel[0], sett.mouse_pos[1]-self.pos_rel[1]]
			self.set_limits()
			self.update_window()
		elif self == IOLootContainer:
			self.pos = [sett.mouse_pos[0]-self.pos_rel[0], sett.mouse_pos[1]-self.pos_rel[1]]
			self.set_limits()
			self.update_window()
		self.active_window = True
		if self.gui_button is not None:
			self.gui_button.active = True
		if self not in opened_windows:
			opened_windows.append(self)
		self.focus_window()

	def set_limits(self):
		"""Sets limits to the window (usually the screen itself)"""

		if self.pos[0] < 0:
			self.pos[0] = 0
		if self.pos[0] > disp_w-self.rect.w:
			self.pos[0] = disp_w-self.rect.w

		if self.pos[1] < 0: self.pos[1] = 0
		if self.pos[1] > disp_h-IOGUI.gui_bg_rect.h-self.rect.h:
			self.pos[1] = disp_h-IOGUI.gui_bg_rect.h-self.rect.h

	def focus_window(self, refresh=False):
		"""Focuses the 'self' window"""

		if not refresh:
			opened_windows.insert(0, opened_windows.pop(opened_windows.index(self)))
		for index, win in enumerate(opened_windows):
			if index == 0:
				win.focused_window = True
			else:
				win.focused_window = False

	def move_window(self, mouse_pos_rel):
		"""Allows the window to move around when holding mouse button"""

		if self.movable:
			self.pos = [sett.mouse_pos[0]-mouse_pos_rel[0], sett.mouse_pos[1]-mouse_pos_rel[1]]
			self.set_limits()
			self.update_window()

	def draw_window(self):
		"""Displays the window and its sub_content"""

		if self.active_window:
			screen.blit(self.img_gui_win, self.pos)
			if self.img_gui is not None:
				screen.blit(self.img_gui, self.pos)
			self.focus_window(refresh=True)
			self.draw_stat_slab()
			self.draw_items()
			self.close_window()

	def draw_stat_slab(self):
		"""Displays the character stats on the stat slab"""

		if self == IOEqu:
			for index, stat in enumerate(self.slab_stats):
				screen.blit(stat, self.stat_positions[index])

	def draw_items(self):
		"""Displays all the items"""

		if self == IOEqu:
			for itype, item in sett.current_game['equipped'].items():
				if item is not None:
					pos = (self.equ_rects[item.itype].x, self.equ_rects[item.itype].y)
					item.draw_single_item(pos)

		elif self == IOInv:
			for cell, item in sett.current_game['inv_items'].items():
				pos = (self.inv_rects[cell].x, self.inv_rects[cell].y)
				if item is not None and item != 'locked':
					item.draw_single_item(pos)
				elif item == 'locked':
					blit_alpha(screen, self.img_locked_cell, pos, 50)

		elif self == IOLootCombat:
			for cell, item in self.loot_buffer.items():
				pos = (self.loot_rects[cell].x, self.loot_rects[cell].y)
				if item is not None:
					item.draw_single_item(pos)

		elif self == IOLootContainer:
			if sett.current_game['previous_container'] is not None:
				for cell, item in sett.current_game['previous_container'].loot_items.items():
					pos = (self.loot_rects[cell].x, self.loot_rects[cell].y)
					if item is not None:
						item.draw_single_item(pos)

	def close_window(self):
		"""Closes the window slightly slower"""

		closed = False
		if self.close_pressed:
			screen.blit(self.img_button_close, (self.pos[0]+self.close_pos_rel[0], self.pos[1]+self.close_pos_rel[1]))
		if self.close_win:
			screen.blit(self.img_button_close, (self.pos[0]+self.close_pos_rel[0], self.pos[1]+self.close_pos_rel[1]))
			self.close_count += 1
			if self.close_count == 5:
				self.close_count = 0
				self.close_pressed = False
				self.close_win = False
				self.active_window = False
				closed = True
				opened_windows.remove(self)
		if closed:
			closed = False
			if self.gui_button is not None:
				self.gui_button.active = False


class Equipment(GUIWindow):
	def __init__(self):
		super().__init__()

		self.img_gui = pg.image.load('data/images/gui/gui_equ.png').convert_alpha()
		self.pos = (disp_w*0.25-self.rect.w*0.5, (disp_h-IOGUI.gui_bg_rect.h)*0.5-self.rect.h*0.5)
		self.gui_button = Button(screen, bg=IOGUI.img_but_bg50_sh, icon=IOGUI.img_but_equ_inv,
		                         icon_pressed_custom=True, icon_active_custom=True,
		                         sheet_index=0, pos=(860, 635), activate_on=True)

		self.update_window()

	def update_sub_win(self):
		"""Updates some specific variables"""

		self.equ_rects = {
						'helm': pg.Rect(self.pos[0]+32, self.pos[1]+70, self.cell_size[0], self.cell_size[1]),
						'weapon': pg.Rect(self.pos[0]+32, self.pos[1]+119, self.cell_size[0], self.cell_size[1]),
						'gloves': pg.Rect(self.pos[0]+32, self.pos[1]+168, self.cell_size[0], self.cell_size[1]),
						'pants': pg.Rect(self.pos[0]+32, self.pos[1]+217, self.cell_size[0], self.cell_size[1]),
						'boots': pg.Rect(self.pos[0]+32, self.pos[1]+266, self.cell_size[0], self.cell_size[1]),
						'necklace': pg.Rect(self.pos[0]+80, self.pos[1]+70, self.cell_size[0], self.cell_size[1]),
						'bag': pg.Rect(self.pos[0]+161, self.pos[1]+70, self.cell_size[0], self.cell_size[1]),
						'shoulder': pg.Rect(self.pos[0]+209, self.pos[1]+70, self.cell_size[0], self.cell_size[1]),
						'armor': pg.Rect(self.pos[0]+209, self.pos[1]+119, self.cell_size[0], self.cell_size[1]),
						'ring': pg.Rect(self.pos[0]+209, self.pos[1]+168, self.cell_size[0], self.cell_size[1]),
						'shield': pg.Rect(self.pos[0]+209, self.pos[1]+217, self.cell_size[0], self.cell_size[1]),
						'belt': pg.Rect(self.pos[0]+209, self.pos[1]+266, self.cell_size[0], self.cell_size[1])}

		self.stat_slab_rect = pg.Rect(self.pos[0]+11, self.pos[1]+318, 255, 92)

		if sett.current_game['current_char'].stat_modify:
			self.slab_stats = [
					text(f'Attack: ({int(sett.current_game["current_char"].chstats["min_att"])}, '
					     f'{int(sett.current_game["current_char"].chstats["max_att"])})',
					     font_style=info_font, font_size=12, color=col_dark_red)[0],
					text(f'Defense: {int(sett.current_game["current_char"].chstats["defense"])}',
					     font_style=info_font, font_size=12, color=col_dark_red)[0],
					text(f'Max health: {int(sett.current_game["current_char"].chstats["max_hp"])}', font_style=info_font,
					     font_size=12, color=col_dark_red)[0],
					text(f'Max mana: {int(sett.current_game["current_char"].chstats["max_mp"])}', font_style=info_font,
					     font_size=12, color=col_dark_red)[0],
					text(f'Max vigor: {int(sett.current_game["current_char"].chstats["max_vigor"])}', font_style=info_font,
					     font_size=12, color=col_dark_red)[0],
					text(f'UV level (LOL): {int(sett.current_game["current_char"].chstats["spirit"])}', font_style=info_font,
					     font_size=12, color=col_dark_red)[0],
					text(f'Move speed: {round(sett.current_game["current_char"].chstats["mov_speed"], 3)}', font_style=info_font,
					     font_size=12, color=col_dark_red)[0],
					text(f'Initiative: {int(sett.current_game["current_char"].chstats["initiative"])}', font_style=info_font,
					     font_size=12, color=col_dark_red)[0]]

		self.stat_positions = [
				(self.stat_slab_rect.x+20, self.stat_slab_rect.y+15),
				(self.stat_slab_rect.x+20, self.stat_slab_rect.y+30),
				(self.stat_slab_rect.x+20, self.stat_slab_rect.y+45),
				(self.stat_slab_rect.x+20, self.stat_slab_rect.y+60),
				(self.stat_slab_rect.x+150, self.stat_slab_rect.y+15),
				(self.stat_slab_rect.x+150, self.stat_slab_rect.y+30),
				(self.stat_slab_rect.x+150, self.stat_slab_rect.y+45),
				(self.stat_slab_rect.x+150, self.stat_slab_rect.y+60)
		]


class Inventory(GUIWindow):
	def __init__(self):
		super().__init__()

		self.img_gui = pg.image.load('data/images/gui/gui_inv.png').convert_alpha()
		self.pos = (disp_w*0.75-self.rect.w*0.5, (disp_h-IOGUI.gui_bg_rect.h)*0.5-self.rect.h*0.5)
		self.gui_button = Button(screen, bg=IOGUI.img_but_bg50_sh, icon=IOGUI.img_but_equ_inv, sheet_index=3,
		                         icon_pressed_custom=True, icon_active_custom=True,
		                         pos=(940, 635), activate_on=True)

		self.default_inv_unlocked = 12
		self.additional_unlocked = 0
		self.full_inv = False

		self.update_window()

	def update_sub_win(self, rects=True, check_inventory=True):
		"""Updates some specific variables"""

		if rects:
			self.inv_rects = generate_grid_rects(pos=self.pos)
		if check_inventory:
			self.update_locked_cells()
			self.check_full_inv()

	def update_locked_cells(self):
		"""Updates the locked cell and item status"""

		self.additional_unlocked = sett.current_game['current_char'].chstats['extra_inv']
		total_unlocked = self.default_inv_unlocked+self.additional_unlocked
		count = 0

		for cell, status in sett.current_game['inv_items'].items():
			if count < int(total_unlocked):
				if status is not None and status != 'locked':
					sett.current_game['inv_items'][cell].item_locked = False
					sett.current_game['inv_items'][cell].update_item_info()
				if status == 'locked':
					sett.current_game['inv_items'][cell] = None
			else:
				if status is not None and status != 'locked':
					sett.current_game['inv_items'][cell].item_locked = True
					sett.current_game['inv_items'][cell].update_item_info()
				elif sett.current_game['inv_items'][cell] is None:
					sett.current_game['inv_items'][cell] = 'locked'
			count += 1

	def check_full_inv(self):
		"""Checks if the inventory is full"""

		free_space = []
		for cell, item in sett.current_game['inv_items'].items():
			if item is None:
				free_space.append(1)

		if any(free_space):
			self.full_inv = False
		else:
			self.full_inv = True


class Loot(GUIWindow):
	def __init__(self):
		super().__init__(size='small')

		self.img_gui = pg.image.load('data/images/gui/gui_loot.png').convert_alpha()
		self.pos_rel = (31, 71)

		self.update_window()

	def update_sub_win(self):
		"""Updates some specific variables"""

		self.loot_rects = generate_grid_rects(dimensions=(3, 3), pos=self.pos, var_x=16, var_y=55)

	def check_loot(self):
		"""Closes the loot window when is empty"""

		loot_items = {}
		if self == IOLootCombat:
			loot_items = self.loot_buffer
		elif self == IOLootContainer:
			loot_items = sett.current_game['current_container'].loot_items

		not_empty = []
		for cell, item in loot_items.items():
			if item is not None:
				not_empty.append(1)
		if not any(not_empty):
			if self == IOLootContainer: sett.current_game['current_container'].opened = False
			self.close_win = True


IOEqu = Equipment()
IOInv = Inventory()
IOLootCombat = Loot()
IOLootContainer = Loot()
IOMouseHover = MouseHover()
