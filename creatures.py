from map_objects import *

generic_creatures = []

cr_imgs = {
		'rat': pg.image.load('data/images/creatures/rat.png').convert_alpha(),
		'snake': pg.image.load('data/images/creatures/snake.png').convert_alpha(),
		'yeti': pg.image.load('data/images/creatures/yeti.png').convert_alpha()
}

cr_imgs_big = {
		'rat': pg.image.load('data/images/creatures/big/big_rat.png').convert_alpha(),
		'snake': pg.image.load('data/images/creatures/big/big_snake.png').convert_alpha(),
		'yeti': pg.image.load('data/images/creatures/big/big_yeti.png').convert_alpha()
}


def create_creature(name):
	"""Returns a new instance of the matching provided name"""

	if name == 'rat': return Rat()
	elif name == 'snake': return Snake()
	elif name == 'yeti': return Yeti()


class Creature:
	def __init__(self):

		self.name = None
		self.type = 'creature'
		self.affinities = {'terrain': [], 'climate': []}

		self.pos = None
		self.rel_pos = ()
		self.visual_rect = None
		self.depth = 0
		self.given_block_rect = None
		self.block_rect = None

		self.attitude = None
		self.escaped = False
		self.affinities = {'terrain': [], 'temperature': []}
		self.loot_items = generate_grid_status(dimensions=(3, 3))

		self.base_stats = {
				'max_hp': 10,
				'max_mp': 0,
				'health': 0,
				'mana': 0,
				'defense': 0,
				'additional_defense': 0,
				'min_att': 1,
				'max_att': 2,
				'additional_attack': 0,
				'initiative': 1}
		self.additional_stats = {
				'max_hp': 0,
				'max_mp': 0,
				'health': 0,
				'mana': 0,
				'defense': 0,
				'additional_defense': 0,
				'min_att': 0,
				'max_att': 0,
				'additional_attack': 0,
				'initiative': 0}

		self.crstats = {}

	def mod_cr_stats(self, stat, value):
		"""Modifies an additional stat and updates the total creature stats ('crstats') afterwards"""

		self.additional_stats[stat] += value

		if self.additional_stats[stat] < 0:
			self.additional_stats[stat] = 0
		if stat == 'health':
			if self.additional_stats['health'] > self.crstats['max_hp']:
				self.additional_stats['health'] = self.crstats['max_hp']
		elif stat == 'mana':
			if self.additional_stats[stat] > self.crstats['max_mp']:
				self.additional_stats[stat] = self.crstats['max_mp']
		elif stat == 'vigor':
			if self.additional_stats[stat] > self.crstats['max_vigor']:
				self.additional_stats[stat] = self.crstats['max_vigor']
		elif stat == 'spirit':
			if self.additional_stats[stat] > self.crstats['max_spirit']:
				self.additional_stats[stat] = self.crstats['max_spirit']

		self.crstats[stat] = self.base_stats[stat]+self.additional_stats[stat]

		# Setting limits #
		if stat == 'max_hp':
			if self.additional_stats['health'] > self.crstats['max_hp']:
				self.additional_stats['health'] = self.crstats['max_hp']
			self.crstats['health'] = self.additional_stats['health']
		elif stat == 'max_mp':
			if self.additional_stats['mana'] > self.crstats['max_mp']:
				self.additional_stats['mana'] = self.crstats['max_mp']
			self.crstats['mana'] = self.additional_stats['mana']

	def gen_creature_stats(self, map_level):
		"""Calculates its stats when a creature is spawned"""

		for base_stat, base_value in self.base_stats.items():
			if base_stat == 'max_hp' or base_stat == 'max_mp':
				self.base_stats[base_stat] = base_value+5*map_level
			elif base_stat == 'defense' or base_stat == 'min_att' or base_stat == 'max_att':
				self.base_stats[base_stat] = base_value+map_level

		for base_stat, base_value in self.base_stats.items():
			self.crstats[base_stat] = self.base_stats[base_stat] + self.additional_stats[base_stat]

		self.mod_cr_stats('health', self.crstats['max_hp'])
		self.mod_cr_stats('mana', self.crstats['max_mp'])

	def update_cr(self, *args):
		"""If is not already in, adds the new instance to the generic object lists and updates some variables"""

		for i in args:
			if i == 'lists':
				existent = []
				for cr in generic_creatures:
					if cr == self.name:
						existent.append(1)
				if not any(existent):
					generic_creatures.append(self)

			elif i == 'v_rect':
				self.visual_rect = cr_imgs[self.name].get_rect()

			elif i == 'pos_change':
				if self.visual_rect.h > tile_h:     # Redo the positioning done in map_setting
					self.pos = (self.pos[0], (self.pos[1]-tile_h*0.5+self.visual_rect.h*0.5)+tile_h-self.visual_rect.h)
				self.depth = self.pos[1]+self.depth

			else: raise ValueError(f'The provided argument "{i}" is not registered')

			self.gen_creature_stats(0)


class Rat(Creature):
	def __init__(self):
		super().__init__()

		self.name = 'rat'

		self.depth = 39
		self.given_block_rect = pg.Rect(10, 16, 24, 30)

		self.attitude = 'elusive'
		self.affinities = {'terrain': ['dirt', 'rock'], 'climate': ['tropical']}

		self.base_stats['max_hp'] = 8
		self.base_stats['min_att'] = 2
		self.base_stats['max_att'] = 4
		self.base_stats['initiative'] = 6

		self.update_cr('lists', 'v_rect')


class Snake(Creature):
	def __init__(self):
		super().__init__()

		self.name = 'snake'

		self.depth = 24
		self.given_block_rect = pg.Rect(4, 17, 30, 24)

		self.attitude = 'neutral'
		self.affinities = {'terrain': ['sand'], 'climate': ['arid']}

		self.base_stats['max_hp'] = r.randint(1, 2)
		self.base_stats['min_att'] = 2
		self.base_stats['max_att'] = 4
		self.base_stats['initiative'] = 3

		self.update_cr('lists', 'v_rect')


class Yeti(Creature):
	def __init__(self):
		super().__init__()

		self.name = 'yeti'

		self.depth = 24
		self.given_block_rect = pg.Rect(4, 17, 30, 24)

		self.attitude = 'aggressive'
		self.affinities = {'terrain': ['rock'], 'climate': ['tundra']}

		self.base_stats['max_hp'] = r.randint(20, 50)
		self.base_stats['min_att'] = 12
		self.base_stats['max_att'] = 22
		self.base_stats['initiative'] = 3

		self.update_cr('lists', 'v_rect')
