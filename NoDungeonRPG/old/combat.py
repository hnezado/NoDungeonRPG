from loot import *


# TODO implement dirt and rock combat backgrounds depending on the current map
combat_img = {
		'portrait_damaged': pg.image.load('data/images/gui/portrait_damaged.png'),
		'combat_bg': None,
		'combat_bg_sand': pg.image.load('data/images/combat/combat_bg_sand.png').convert_alpha(),
		'combat_bg_dirt': pg.image.load('data/images/combat/combat_bg_dirt.png').convert_alpha(),
		'combat_bg_rock': pg.image.load('data/images/combat/combat_bg_rock.png').convert_alpha(),
		'combat_but_bg': pg.image.load('data/images/combat/combat_but_bg.png').convert_alpha(),
		'action_icons': Sheet('data/images/combat/combat_action_icons.png', dimensions=(1, 4)),
		'combat_cr_bar_glass': pg.image.load('data/images/combat/combat_cr_glass_bar.png').convert_alpha(),
		'combat_cr_bar_hp': pg.image.load('data/images/combat/combat_cr_hp_bar.png').convert_alpha(),
}


class Combat:
	def __init__(self):
		self.win_pos = (256, 96)
		self.bar_cr_hp_pos = (self.win_pos[0]+20, self.win_pos[1]+20)
		self.cr_pos = (self.win_pos[0]+170, self.win_pos[1]+90)
		self.panel_pos = (self.win_pos[0], self.win_pos[1]+combat_img['combat_bg_sand'].get_height())
		self.but_rect = pg.Rect(0, 0, 100, 50)
		self.but_att_pos, self.but_cast_pos, self.but_item_pos, self.but_retreat_pos = \
			(self.panel_pos[0]+combat_img['combat_but_bg'].get_width()*0.125-self.but_rect.w*0.5+10,
			 self.panel_pos[1]+combat_img['combat_but_bg'].get_height()*0.5-self.but_rect.h*0.5), \
			(self.panel_pos[0]+combat_img['combat_but_bg'].get_width()*0.375-self.but_rect.w*0.5+5,
			 self.panel_pos[1]+combat_img['combat_but_bg'].get_height()*0.5-self.but_rect.h*0.5), \
			(self.panel_pos[0]+combat_img['combat_but_bg'].get_width()*0.625-self.but_rect.w*0.5-5,
			 self.panel_pos[1]+combat_img['combat_but_bg'].get_height()*0.5-self.but_rect.h*0.5), \
			(self.panel_pos[0]+combat_img['combat_but_bg'].get_width()*0.875-self.but_rect.w*0.5-10,
			 self.panel_pos[1]+combat_img['combat_but_bg'].get_height()*0.5-self.but_rect.h*0.5)

		self.button_attack = Button(screen, bg=IOGUI.img_but_bg100, icon=combat_img['action_icons'],
		                            sheet_index=0, pos=self.but_att_pos)
		self.button_cast = Button(screen, bg=IOGUI.img_but_bg100, icon=combat_img['action_icons'],
		                          sheet_index=1, pos=self.but_cast_pos)
		self.button_item = Button(screen, bg=IOGUI.img_but_bg100, icon=combat_img['action_icons'],
		                          sheet_index=2, pos=self.but_item_pos)
		self.button_retreat = Button(screen, bg=IOGUI.img_but_bg100, icon=combat_img['action_icons'],
		                             sheet_index=3, pos=self.but_retreat_pos)

		self.but_back_pos = (self.panel_pos[0]+440+10, self.panel_pos[1]+12+25)
		self.button_back = Button(screen, bg=IOGUI.img_but_bg50, icon=img_sk_icons,
		                          sheet_index=0, pos=self.but_back_pos)

		self.cr_flee = False
		self.combat_active = False
		self.combat_ready = False
		self.turn = ''
		self.check_turn = True
		self.combat_menu = 'actions'
		self.max_sk_per_row = 8
		self.animation = False
		self.cr_hp_pct, self.last_cr_hp, self.last_cr_hp_pct = 0, 0, 0
		self.counter_between_actions, self.counter_end = 0, 0
		self.char_damage, self.cr_damage = 0, 0
		self.x_variation = 40
		self.random_pos_x = r.randint(-self.x_variation, self.x_variation)

	def draw_combat(self):
		"""Displays the combat screen"""

		if sett.active_screen == 'game':
			self.check_cr_attitude()

		if self.combat_active:
			screen.blit(combat_img['combat_bg'], self.win_pos)
			screen.blit(cr_imgs_big[sett.current_game["current_creature"].name], self.cr_pos)
			self.draw_cr_stat_bars()
			self.show_stat_effects()
			screen.blit(combat_img['combat_but_bg'], self.panel_pos)
			self.draw_combat_buttons()

			self.check_turns()
			self.check_end_combat()

	def check_cr_attitude(self):
		"""Checks the attitude of the collided creature"""

		if sett.current_game["current_creature"] is not None:
			if sett.current_game["current_creature"].attitude == 'aggressive':
				self.start_combat()
			elif sett.current_game["current_creature"].attitude == 'neutral':
				self.combat_ready = True
			elif sett.current_game["current_creature"].attitude == 'elusive':
				chance = r.randint(1, 100)
				if chance < 0:
					self.end_combat('flee')
				else:
					self.start_combat()

		elif sett.current_game["current_creature"] is None:
			self.combat_ready = False

	def check_animation(self):
		"""Checks if there is an animation in process"""

		if self.last_cr_hp_pct != self.cr_hp_pct:
			self.animation = True
		elif IOGUI.last_hp_pct != IOGUI.hp_pct or IOGUI.last_mp_pct != IOGUI.mp_pct:
			self.animation = True
		elif self.char_damage != 0 or self.cr_damage != 0:
			self.animation = True
		else: self.animation = False

	def check_turns(self):
		"""Checks whose turn is it"""

		if self.check_turn:
			self.check_animation()
			if not self.animation:
				self.set_turn()
				self.check_turn = False
		if self.turn == 'creature':
			self.creature_action('attack')

	def check_actions_ready(self, who):
		"""Checks if actions are enabled (when there are no animations)"""

		if not self.animation:
			if self.turn == who:
				if who == 'creature':
					if self.counter_end == 0:
						self.counter_between_actions += 1
						if self.counter_between_actions >= 10:
							self.counter_between_actions = 0
							return True
				else:
					return True

	def draw_cr_stat_bars(self):
		"""Compiles every creature stat bar displaying"""

		def draw_cr_stat(stat):
			"""Displays the specified creature stat bar (while animation -> blocks actions)"""

			change_stat_speed = 1
			self.cr_hp_pct = int(sett.current_game["current_creature"].crstats['health']/sett.current_game["current_creature"].crstats['max_hp']*100)

			if self.last_cr_hp_pct > self.cr_hp_pct:
				self.last_cr_hp_pct -= change_stat_speed
				if self.last_cr_hp_pct < self.cr_hp_pct:
					self.last_cr_hp_pct = self.cr_hp_pct
			elif self.last_cr_hp_pct < self.cr_hp_pct:
				self.last_cr_hp_pct += change_stat_speed
				if self.last_cr_hp_pct > self.cr_hp_pct:
					self.last_cr_hp_pct = self.cr_hp_pct

			if stat == 'hp':
				screen.blit(combat_img['combat_cr_bar_hp'], self.bar_cr_hp_pos,
				            (0, 0, int(self.last_cr_hp_pct/100*combat_img['combat_cr_bar_hp'].get_width()),
				             combat_img['combat_cr_bar_hp'].get_height()))
				screen.blit(combat_img['combat_cr_bar_glass'], self.bar_cr_hp_pos)

				# Text (stat info) #
				txt_hp_cr = text(f'{sett.current_game["current_creature"].crstats["health"]}/{sett.current_game["current_creature"].crstats["max_hp"]}',
				                 info_font, 11)
				txt_pos_cr = (self.bar_cr_hp_pos[0]+combat_img['combat_cr_bar_hp'].get_width()*0.5-txt_hp_cr[0].get_width()*0.5,
				              self.bar_cr_hp_pos[1]+combat_img['combat_cr_bar_hp'].get_height()*0.5-txt_hp_cr[0].get_height()*0.5)
				screen.blit(txt_hp_cr[0], txt_pos_cr)

		draw_cr_stat('hp')

	def show_stat_effects(self):
		"""Animates some actions (like attacking, healing, boosting points...)"""
		"""Shows stat variation animations"""

		# Damage #
		if self.char_damage != 0:
			pos = (self.cr_pos[0]+cr_imgs_big[sett.current_game["current_creature"].name].get_width()*0.5+self.random_pos_x,
			       self.cr_pos[1]+cr_imgs_big[sett.current_game["current_creature"].name].get_height()*0.5)
			loop = Damage.draw_damage(str(self.char_damage), pos, screen, info_font, col_dark_red)

			if loop == 'end_anim':
				self.random_pos_x = r.randint(-self.x_variation, self.x_variation)
				self.char_damage = 0

		elif self.cr_damage != 0:
			img = combat_img['portrait_damaged']
			pos1 = (IOGUI.portrait_pos[0]+IOGUI.img_portrait.get_width()*0.5+self.random_pos_x,
			        IOGUI.portrait_pos[1]+IOGUI.img_portrait.get_height()*0.5+20)
			pos2 = IOGUI.portrait_pos
			loop = Damage.draw_damage(str(self.cr_damage), pos1, screen, info_font, col_dark_red, img, pos2)

			if loop == 'end_anim':
				self.random_pos_x = r.randint(-self.x_variation, self.x_variation)
				self.cr_damage = 0

		# TODO add healing and boosting effects
		# Healing #
		# Boosting #

	def draw_combat_buttons(self):
		"""Displays the combat buttons"""

		if self.combat_menu == 'actions':
			self.button_attack.draw_button()
			self.button_cast.draw_button()
			self.button_item.draw_button()
			self.button_retreat.draw_button()
		elif self.combat_menu == 'cast':
			self.button_back.draw_button()
			pos = [self.panel_pos[0]+16, self.panel_pos[1]+14]
			count = 0
			for sk in sett.current_game['skills']:
				sk_button[sk.name].pos, sk_button[sk.name].pos_pressed = pos, pos
				sk_button[sk.name].rect.x, sk_button[sk.name].rect.y = pos[0], pos[1]
				sk_button[sk.name].draw_button()
				count += 1
				if count < self.max_sk_per_row:
					pos[0] += sk_button[sk.name].rect.w+1
				else:
					pos[1] += sk_button[sk.name].rect.h+1
					pos[0] = self.panel_pos[0]+16
					count = 0

	def check_end_combat(self):
		"""Checks if the combat is over"""

		if sett.current_game["current_creature"].crstats['health'] == 0:
			self.counter_end += 1
			if self.counter_end >= 20:
				self.counter_end = 0
				if not self.animation:
					self.end_combat('win')

		elif sett.current_game['current_char'].chstats['health'] == 0:
			self.counter_end += 1
			if self.counter_end >= 80:
				self.counter_end = 0
				self.end_combat('lose')

	def start_combat(self):
		"""Starts the combat"""

		if not self.combat_active:
			self.combat_active = True
			sett.current_game['current_char'].stop_movement()
			if not self.check_flee(based_on='first_encounter'):
				self.cr_hp_pct = int(sett.current_game["current_creature"].crstats['health']/sett.current_game["current_creature"].crstats['max_hp']*100)
				self.last_cr_hp = sett.current_game["current_creature"].crstats['health']
				self.last_cr_hp_pct = int(self.last_cr_hp/sett.current_game["current_creature"].crstats['max_hp']*100)
				IOGUI.message(f'{sett.current_game["current_creature"].name} attacks!', 'combat')
				self.set_combat_bg()
			else:
				self.end_combat('flee')

	@staticmethod
	def set_combat_bg():
		"""Checks the elements of the current map and picks the proper background"""

		for type in sett.current_game['current_map'].map_elements['terrain']:
			if type == 'sand':
				combat_img['combat_bg'] = combat_img['combat_bg_sand']
			elif type == 'dirt':
				combat_img['combat_bg'] = combat_img['combat_bg_dirt']
			elif type == 'rock':
				combat_img['combat_bg'] = combat_img['combat_bg_rock']

	def end_combat(self, reason=None):
		"""Ends the combat"""

		if reason == 'win':
			IOGUI.message(f'{sett.current_game["current_char"].char_name} has killed {sett.current_game["current_creature"].name}', 'combat')
			loot(stats=True)
		elif reason == 'lose':
			IOGUI.message(f'{sett.current_game["current_char"].char_name} has been defeated', 'combat')

		elif reason == 'retreat':
			IOGUI.message(f'{sett.current_game["current_char"].char_name} has retreated successfully', 'combat')
		elif reason == 'flee':
			IOGUI.message(f'{sett.current_game["current_creature"].name.title()} has fled', 'combat')

		sett.current_game['current_map'].remove_from_map(sett.current_game["current_creature"])
		self.turn, self.check_turn = '', True
		self.combat_active = False

	def char_action(self, action):
		"""Defines the character action"""

		if self.check_actions_ready('char'):
			if action == 'attack':
				self.attack()
				self.check_turn = True
			elif action == 'cast':
				self.show_cast_menu(enabled=True)
			elif action == 'use_item':
				self.use_item()
			elif action == 'retreat':
				self.retreat()

	def creature_action(self, action):
		"""Defines the character action"""

		if self.check_actions_ready('creature'):
			if self.check_flee(based_on='hp_left'):
				self.end_combat('flee')
			else:
				if action == 'attack':
					self.attack()
					self.check_turn = True
				elif action == 'cast':
					self.show_cast_menu()
				elif action == 'use_item':
					self.use_item()
				elif action == 'retreat':
					self.retreat()

	@staticmethod
	def check_flee(based_on):
		"""Checks if the creature flees"""

		flee_modifier = 0
		if sett.current_game["current_creature"].attitude == 'aggressive':
			flee_modifier = 0.02
		elif sett.current_game["current_creature"].attitude == 'neutral':
			flee_modifier = 0.04
		elif sett.current_game["current_creature"].attitude == 'elusive':
			flee_modifier = 0.08

		flee_roll = r.randint(1, 100)
		if based_on == 'first_encounter':
			if sett.current_game["current_creature"].attitude == 'elusive':
				flee_chance = 100*flee_modifier
				if flee_roll < flee_chance:
					return True

		# If elusive, the lower the life's creature, the higher the chances to flee #
		elif based_on == 'hp_left':
			hp_pct_left = int(sett.current_game["current_creature"].crstats['health']/sett.current_game["current_creature"].crstats['max_hp']*100)
			hp_pct_off = 100-hp_pct_left
			if flee_roll < round(hp_pct_off*0.1*flee_modifier):
				return True

	def attack(self):
		"""Defines the attacking action"""

		# TODO add methods on char and cr which take into account the defence to reduce the damage taken

		if self.turn == 'char':
			self.char_damage = r.randint(int(sett.current_game['current_char'].chstats['min_att']),
			                             int(sett.current_game['current_char'].chstats['max_att']))
			IOGUI.message(f'{sett.current_game["current_char"].char_name} attacks {sett.current_game["current_creature"].name} dealing '
			              f'{self.char_damage} points of damage!', 'combat')
			sett.current_game["current_creature"].mod_cr_stats('health', -self.char_damage)
		elif self.turn == 'creature':
			self.cr_damage = r.randint(sett.current_game["current_creature"].crstats['min_att'], sett.current_game["current_creature"].crstats['max_att'])
			IOGUI.message(f'{sett.current_game["current_creature"].name.title()} attacks {sett.current_game["current_char"].char_name} dealing '
			              f'{self.cr_damage} points of damage!', 'combat')
			sett.current_game['current_char'].mod_stats('health', -self.cr_damage)

	def show_cast_menu(self, enabled):
		"""Displays the available skill menu"""

		if enabled:
			self.combat_menu = 'cast'
		else:
			self.combat_menu = 'actions'

	@staticmethod
	def use_item():
		"""Defines the using item action"""

		IOGUI.message(f'Use item is not available yet')

	def retreat(self):
		"""Defines the retreating action"""

		if self.turn == 'char':
			self.end_combat('retreat')
		elif self.turn == 'creature':
			self.end_combat('flee')

	def set_turn(self):
		"""Defines whose turn it is ('char' or 'creature')"""
		def get_first_turn():
			"""Returns 'char' or 'creature' depending on their initiative. If equal initiative: it does a random choice"""

			if sett.current_game['current_char'].chstats['initiative'] > sett.current_game["current_creature"].crstats[
				'initiative']:
				return 'char'
			elif sett.current_game['current_char'].chstats['initiative'] <\
					sett.current_game["current_creature"].crstats['initiative']:
				return 'creature'
			else:
				return r.choice(['char', 'creature'])

		if self.turn == 'char':
			self.turn = 'creature'
		elif self.turn == 'creature':
			self.turn = 'char'
		else:
			self.turn = get_first_turn()


IOCombat = Combat()
