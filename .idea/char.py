from creatures import *

character_classes = []
adventurer_img = Sheet('data/images/chars/adventurer.png', dimensions=(4, 9))
current_char_img = adventurer_img


class Char:
	def __init__(self):

		self.char_name = None
		self.char_class = None

		self.pos = [0, 0]
		self.visual_rect = None             # (30 x 52)

		self.facing = 'down'
		self.frame_up_start, self.frame_down_start, self.frame_left_start, self.frame_right_start = 1, 10, 19, 28
		self.frame_up, self.frame_down, self.frame_left, self.frame_right = \
			self.frame_up_start, self.frame_down_start, self.frame_left_start, self.frame_right_start
		self.frames_per_direction = 8
		self.delay_anim, self.delay_count = 3, 0
		self.move_up, self.move_down, self.move_left, self.move_right = False, False, False, False

		# Stats #
		# Only modify them when is a permanent change (like upgrading stats with meditation e.g.) #
		self.base_stats = {
				'mov_speed': 3,
				'max_hp': 100,
				'max_mp': 30,
				'max_vigor': 10,
				'max_spirit': 10,
				'health': 0,
				'mana': 0,
				'vigor': 0,
				'spirit': 0,
				'min_att': 1,
				'max_att': 1,
				'defense': 0,
				'initiative': 0,
				'extra_inv': 0
		}
		self.additional_stats = {
				'mov_speed': 0,
				'max_hp': 0,
				'max_mp': 0,
				'max_vigor': 0,
				'max_spirit': 0,
				'health': 0,
				'mana': 0,
				'vigor': 0,
				'spirit': 0,
				'defense': 0,
				'additional_defense': 0,
				'min_att': 0,
				'max_att': 0,
				'additional_attack': 0,
				'initiative': 0,
				'extra_inv': 0
		}
		self.chstats = {}
		self.stat_modify = True
		self.meditation_ready = False

	def load_char_img(self):
		"""Defines the image based on the chosen char"""

		global current_char_img

		if self.char_class == 'adventurer':
			current_char_img = adventurer_img

	def mod_stats(self, stat, value):
		"""Modifies an additional stat and updates some values after"""

		self.stat_modify = True
		self.additional_stats[stat] += value

		if self.additional_stats[stat] < 0:
			self.additional_stats[stat] = 0
		if stat == 'health':
			if self.additional_stats['health'] > self.chstats['max_hp']:
				self.additional_stats['health'] = self.chstats['max_hp']
		elif stat == 'mana':
			if self.additional_stats[stat] > self.chstats['max_mp']:
				self.additional_stats[stat] = self.chstats['max_mp']
		elif stat == 'vigor':
			if self.additional_stats[stat] > self.chstats['max_vigor']:
				self.additional_stats[stat] = self.chstats['max_vigor']
		elif stat == 'spirit':
			if self.additional_stats[stat] > self.chstats['max_spirit']:
				self.additional_stats[stat] = self.chstats['max_spirit']

		self.chstats[stat] = self.base_stats[stat]+self.additional_stats[stat]

		# Setting limits #
		if stat == 'max_hp':
			if self.additional_stats['health'] > self.chstats['max_hp']:
				self.additional_stats['health'] = self.chstats['max_hp']
			self.chstats['health'] = self.additional_stats['health']
		elif stat == 'max_mp':
			if self.additional_stats['mana'] > self.chstats['max_mp']:
				self.additional_stats['mana'] = self.chstats['max_mp']
			self.chstats['mana'] = self.additional_stats['mana']
		elif stat == 'max_vigor':
			if self.additional_stats['vigor'] > self.chstats['max_vigor']:
				self.additional_stats['vigor'] = self.chstats['max_vigor']
			self.chstats['vigor'] = self.additional_stats['vigor']

		# Meditation triggering (when spirit full) #
		if self.additional_stats['spirit'] == self.chstats['max_spirit']:
			self.meditation_ready = True
		else: self.meditation_ready = False

		# Capping speed to avoid to be stuck into blocks #
		if self.chstats['mov_speed'] > self.visual_rect.w*0.5:
			self.chstats['mov_speed'] = self.visual_rect.w*0.5
		if self.chstats['mov_speed'] > self.visual_rect.h*0.6:
			self.chstats['mov_speed'] = self.visual_rect.h*0.6

	def update_char(self, first_load=False):
		"""Centralizes every instance update"""

		if first_load:
			for base_stat, base_value in self.base_stats.items():
				self.chstats[base_stat] = self.base_stats[base_stat]

			existent = []
			for char in character_classes:
				if char == self.char_class:
					existent.append(1)
			if not any(existent):
					character_classes.append(self.char_class)

		self.visual_rect = pg.Rect(0, 0, current_char_img.crop_w, current_char_img.crop_h)

	@staticmethod
	def set_collided(*args):
		"""Sets the current collided object (instance) to a variable if collision, else None"""

		# if current_container is not None: current_container.opened = False
		sett.current_game['current_container'] = None
		sett.current_game['current_creature'] = None

		for i in args:
			if i.type == 'container':
				sett.current_game['current_container'] = i
			elif i.type == 'creature':
				sett.current_game['current_creature'] = i

	def collision(self, direction, return_collided_object=False):
		"""Checks if there is a collision between the character and any map object"""

		# ATTENTION If speed is higher than w=(*1) h=(*0.4) of char visual_rect it will pass through (no blocking lines) #

		margin = self.chstats['mov_speed']
		up_collision_line, down_collision_line, left_collision_line, right_collision_line = \
			pg.Rect(self.pos[0]+margin, self.pos[1]+self.visual_rect.h*0.6, self.visual_rect.w-margin*2, 1), \
			pg.Rect(self.pos[0]+margin, self.pos[1]+self.visual_rect.h, self.visual_rect.w-margin*2, 1), \
			pg.Rect(self.pos[0], self.pos[1]+self.visual_rect.h*0.6+margin, 1, self.visual_rect.h*0.4-margin*2), \
			pg.Rect(self.pos[0]+self.visual_rect.w, self.pos[1]+self.visual_rect.h*0.6+margin,
			        1, self.visual_rect.h*0.4-margin*2)

		collided = []
		for obj in sett.current_game['blocking_objs']:
			if direction == 'up':
				if obj.block_rect.colliderect(up_collision_line):
					collided.append(obj)
			elif direction == 'down':
				if obj.block_rect.colliderect(down_collision_line):
					collided.append(obj)
			elif direction == 'left':
				if obj.block_rect.colliderect(left_collision_line):
					collided.append(obj)
			elif direction == 'right':
				if obj.block_rect.colliderect(right_collision_line):
					collided.append(obj)

		if return_collided_object:
			return collided[0]
		else:
			return any(collided)

	def animate(self, direction):
		"""Animates the character sprite while moving"""

		if direction == 'up':
			screen.blit(current_char_img.sheet, self.pos, current_char_img.crops[self.frame_up])
			self.delay_count += 1
			if self.delay_count >= self.delay_anim:
				self.frame_up += 1
				self.delay_count = 0
			if self.frame_up == self.frame_up_start+self.frames_per_direction:
				self.frame_up = self.frame_up_start
		elif direction == 'down':
			screen.blit(current_char_img.sheet, self.pos, current_char_img.crops[self.frame_down])
			self.delay_count += 1
			if self.delay_count >= self.delay_anim:
				self.frame_down += 1
				self.delay_count = 0
			if self.frame_down == self.frame_down_start+self.frames_per_direction:
				self.frame_down = self.frame_down_start
		elif direction == 'left':
			screen.blit(current_char_img.sheet, self.pos, current_char_img.crops[self.frame_left])
			self.delay_count += 1
			if self.delay_count >= self.delay_anim:
				self.frame_left += 1
				self.delay_count = 0
			if self.frame_left == self.frame_left_start+self.frames_per_direction:
				self.frame_left = self.frame_left_start
		elif direction == 'right':
			screen.blit(current_char_img.sheet, self.pos, current_char_img.crops[self.frame_right])
			self.delay_count += 1
			if self.delay_count >= self.delay_anim:
				self.frame_right += 1
				self.delay_count = 0
			if self.frame_right == self.frame_right_start+self.frames_per_direction:
				self.frame_right = self.frame_right_start

	def displace(self, direction, modifier_value=1.0):
		"""Defines the sprite displacement direction (position change)"""

		moving_value = self.chstats['mov_speed']*modifier_value

		if direction == 'up':
			self.pos[1] -= moving_value
		elif direction == 'down':
			self.pos[1] += moving_value
		elif direction == 'left':
			self.pos[0] -= moving_value
		elif direction == 'right':
			self.pos[0] += moving_value
		elif direction == 'up_l':
			self.pos[0] -= moving_value
			self.pos[1] -= moving_value
		elif direction == 'up_r':
			self.pos[0] += moving_value
			self.pos[1] -= moving_value
		elif direction == 'down_l':
			self.pos[0] -= moving_value
			self.pos[1] += moving_value
		elif direction == 'down_r':
			self.pos[0] += moving_value
			self.pos[1] += moving_value

	def movement(self):
		"""Defines the sprite actions if there is any kind of motion"""

		# UP & DIAGONALS #
		if self.move_up and self.move_left:
			self.facing = 'up'
			self.animate(self.facing)
			if not self.collision('up'):
				if not self.collision('left'):
					self.set_collided()
					self.displace('up_l', modifier_value=0.6)
				elif self.collision('left'):
					self.set_collided(self.collision('left', return_collided_object=True))
					self.displace('up', modifier_value=0.6)
			elif self.collision('up'):
				if not self.collision('left'):
					self.set_collided(self.collision('up', return_collided_object=True))
					self.displace('left', modifier_value=0.6)
				elif self.collision('left'):
					self.set_collided(self.collision('up', return_collided_object=True))
					self.set_collided(self.collision('left', return_collided_object=True))

		elif self.move_up and self.move_right:
			self.facing = 'up'
			self.animate(self.facing)
			if not self.collision('up'):
				if not self.collision('right'):
					self.set_collided()
					self.displace('up_r', modifier_value=0.6)
				elif self.collision('right'):
					self.set_collided(self.collision('right', return_collided_object=True))
					self.displace('up', modifier_value=0.6)

			elif self.collision('up'):
				if not self.collision('right'):
					self.set_collided(self.collision('up', return_collided_object=True))
					self.displace('right', modifier_value=0.6)
				elif self.collision('right'):
					self.set_collided(self.collision('up', return_collided_object=True))
					self.set_collided(self.collision('right', return_collided_object=True))

		elif self.move_up:
			self.facing = 'up'
			self.animate(self.facing)
			if not self.collision(self.facing):
				self.set_collided()
				self.displace(self.facing)
			elif self.collision(self.facing):
				self.set_collided(self.collision(self.facing, return_collided_object=True))

		# DOWN & DIAGONALS #
		elif self.move_down and self.move_left:
			self.facing = 'down'
			self.animate(self.facing)
			if not self.collision('down'):
				if not self.collision('left'):
					self.set_collided()
					self.displace('down_l', modifier_value=0.6)
				elif self.collision('left'):
					self.set_collided(self.collision('left', return_collided_object=True))
					self.displace('down', modifier_value=0.6)
			if self.collision('down'):
				if not self.collision('left'):
					self.set_collided(self.collision('down', return_collided_object=True))
					self.displace('left', modifier_value=0.6)
				elif self.collision('left'):
					self.set_collided(self.collision('down', return_collided_object=True))
					self.set_collided(self.collision('left', return_collided_object=True))

		elif self.move_down and self.move_right:
			self.facing = 'down'
			self.animate(self.facing)
			if not self.collision('down'):
				if not self.collision('right'):
					self.set_collided()
					self.displace('down_r', modifier_value=0.6)
				elif self.collision('right'):
					self.set_collided(self.collision('right', return_collided_object=True))
					self.displace('down', modifier_value=0.6)
			if self.collision('down'):
				if not self.collision('right'):
					self.set_collided(self.collision('down', return_collided_object=True))
					self.displace('right', modifier_value=0.6)
				elif self.collision('right'):
					self.set_collided(self.collision('down', return_collided_object=True))
					self.set_collided(self.collision('right', return_collided_object=True))

		elif self.move_down:
			self.facing = 'down'
			self.animate(self.facing)
			if not self.collision(self.facing):
				self.set_collided()
				self.displace(self.facing)
			elif self.collision(self.facing):
				self.set_collided(self.collision(self.facing, return_collided_object=True))

		# LEFT #
		elif self.move_left:
			self.facing = 'left'
			self.animate(self.facing)
			if not self.collision(self.facing):
				self.set_collided()
				self.displace(self.facing)
			elif self.collision(self.facing):
				self.set_collided(self.collision(self.facing, return_collided_object=True))

		# RIGHT #
		elif self.move_right:
			self.facing = 'right'
			self.animate(self.facing)
			if not self.collision(self.facing):
				self.set_collided()
				self.displace(self.facing)
			elif self.collision(self.facing):
				self.set_collided(self.collision(self.facing, return_collided_object=True))

	def stop_movement(self):
		"""Stops the character animation and movement"""

		self.move_up, self.move_down, self.move_left, self.move_right = False, False, False, False

	def stand(self, direction):
		"""Defines the sprite standing position (facing towards the last direction it was moved)"""

		if direction == 'up':
			screen.blit(current_char_img.sheet, self.pos, current_char_img.crops[0])
		elif direction == 'down':
			screen.blit(current_char_img.sheet, self.pos, current_char_img.crops[9])
		elif direction == 'left':
			screen.blit(current_char_img.sheet, self.pos, current_char_img.crops[18])
		elif direction == 'right':
			screen.blit(current_char_img.sheet, self.pos, current_char_img.crops[27])

	def draw_char(self):
		"""Displays the character sprite"""

		self.movement()

		if not self.move_up and not self.move_down and not self.move_left and not self.move_right:
			self.stand(self.facing)

	def meditation(self):
		"""Sets every action when meditation occurs"""

		stats_upgraded = self.upgrade_base_stats()

		# Resets the spirit to 0 #
		self.mod_stats('spirit', -self.chstats['spirit'])

		# Recovers life, mana and vigor #
		self.mod_stats('health', self.chstats['max_hp'])
		self.mod_stats('mana', self.chstats['max_mp'])
		self.mod_stats('vigor', self.chstats['max_vigor']*0.5)

		if len(stats_upgraded) > 0: return stats_upgraded

	def upgrade_base_stats(self):
		"""Upgrades some base stats if the upgrading chance is successful (permanent change)"""

		modifiable_stats = ['mov_speed', 'max_hp', 'max_mp', 'max_vigor', 'attack', 'defense', 'initiative']
		stats_upg = []

		for stat in modifiable_stats:
			upgrade_chance = r.randint(1, 100)
			if upgrade_chance <= 10:
				if stat == 'mov_speed':
					self.base_stats[stat] += 0.01
				elif stat == 'max_vigor':
					self.base_stats['max_vigor'] += 1
				elif stat == 'attack':
					if self.base_stats['min_att'] < 11:
						self.base_stats['min_att'] += 1
						self.base_stats['max_att'] += 1
					else:
						self.base_stats['min_att'] += self.base_stats['min_att']*0.1
						self.base_stats['max_att'] += self.base_stats['max_att']*0.1
				elif stat == 'initiative':
					self.base_stats[stat] += 1
				else:
					if self.base_stats[stat] < 11:
						self.base_stats[stat] += 1
					self.base_stats[stat] += self.base_stats[stat]*0.1

				stats_upg.append(stat)
				if stat == 'attack':
					self.chstats['min_att'] = self.base_stats['min_att']+self.additional_stats['min_att']
					self.chstats['max_att'] = self.base_stats['max_att']+self.additional_stats['max_att']
				else:
					self.chstats[stat] = self.base_stats[stat]+self.additional_stats[stat]

		# Capping speed to avoid to be stuck into blocks #
		if self.chstats['mov_speed'] > self.visual_rect.w*0.5:
			self.chstats['mov_speed'] = self.visual_rect.w*0.5

		self.stat_modify = True

		# Return the upgraded stats as a list of str #
		return stats_upg


class Adventurer(Char):
	def __init__(self):
		super().__init__()

		self.char_name = 'Timmy'
		self.char_class = 'adventurer'
		self.load_char_img()
		# self.image = Sheet('data/images/chars/adventurer.png', dimensions=(4, 9))
		self.update_char(first_load=True)

		# Update any stat or equip any item after update_char
		self.mod_stats('health', self.base_stats['max_hp'])
		self.mod_stats('mana', 15)
		self.mod_stats('vigor', 2)
		# self.mod_stats('spirit', 10)
		self.mod_stats('initiative', 10)


sett.current_game['current_char'] = Adventurer()
