from GUI import *


iquality_img = {'normal': pg.image.load('data/images/items/qualities/normal.png').convert_alpha(),
                'magic':   pg.image.load('data/images/items/qualities/magic.png').convert_alpha(),
                'rare':    pg.image.load('data/images/items/qualities/rare.png').convert_alpha(),
                'set':     pg.image.load('data/images/items/qualities/set.png').convert_alpha(),
                'unique':  pg.image.load('data/images/items/qualities/unique.png').convert_alpha(),
                'epic':    pg.image.load('data/images/items/qualities/epic.png').convert_alpha()}

item_img = {'null_item': pg.image.load('data/images/null32.png').convert_alpha(),
            'ragged_bandana': pg.image.load('data/images/items/helms/ragged_bandana.png').convert_alpha(),
            'mithril_helmet': pg.image.load('data/images/items/helms/mithril_helmet.png').convert_alpha(),
            'fist_knife': pg.image.load('data/images/items/weapons/fist_knife.png').convert_alpha(),
            'gladius': pg.image.load('data/images/items/weapons/gladius.png').convert_alpha(),
            'long_sword': pg.image.load('data/images/items/weapons/long_sword.png').convert_alpha(),
            'hand_wraps': pg.image.load('data/images/items/gloves/hand_wraps.png').convert_alpha(),
            'cobweb_string': pg.image.load('data/images/items/necklaces/cobweb_string.png').convert_alpha(),
            'ornamental_chain': pg.image.load('data/images/items/necklaces/ornamental_chain.png').convert_alpha(),
            'superstitious_amulet': pg.image.load('data/images/items/necklaces/superstitious_amulet.png'
                                                  ).convert_alpha(),
            'glowing_cord': pg.image.load('data/images/items/necklaces/glowing_cord.png').convert_alpha(),
            'mystical_collar': pg.image.load('data/images/items/necklaces/mystical_collar.png').convert_alpha(),
            'small_pouch': pg.image.load('data/images/items/bags/small_pouch.png').convert_alpha(),
            'plated_leather_armor': pg.image.load('data/images/items/armors/plated_leather_armor.png').convert_alpha(),
            'fate_ring': pg.image.load('data/images/items/rings/fate_ring.png').convert_alpha(),
            'light_heater': pg.image.load('data/images/items/shields/light_heater.png').convert_alpha(),
            'reforged_buckler': pg.image.load('data/images/items/shields/reforged_buckler.png').convert_alpha(),
            'kite_shield': pg.image.load('data/images/items/shields/kite_shield.png').convert_alpha(),
            'heavy_pavise': pg.image.load('data/images/items/shields/heavy_pavise.png').convert_alpha(),
            'holy_shield': pg.image.load('data/images/items/shields/holy_shield.png').convert_alpha(),
            }


class Item:
	def __init__(self, main=False):
		# Item classes #
		self.cl_helms = ['ragged_bandana', 'mithril_helmet']
		# , 'executioner_hood', 'cursed_mask', 'steel_mailcoif', 'mithril_helmet']
		self.cl_weapons = ['fist_knife', 'gladius', 'long_sword']
		# , 'flexible_bow', 'double_blade', 'viking_axe', 'ancient_staff']
		self.cl_gloves = ['hand_wraps']
		# , 'wool_mittens', 'articulated_gloves', 'plated_gauntlets', 'heavenstone_gloves']
		self.cl_pants = ['worn_shorts', 'traditional_skirt', 'silk_long_pants', 'flexible_tights', 'chainmail_shorts']
		self.cl_boots = ['wicker_sandals', 'fitted_clogs', 'stiff_boots', 'bronze_greaves', 'great_sabatons']
		self.cl_necklaces = ['cobweb_string', 'ornamental_chain', 'superstitious_amulet', 'glowing_cord',
		                     'mystical_collar']
		self.cl_bags = ['small_pouch']# ['tied_cloth', 'small_pouch', 'strap_bag', 'knapsack', 'large_backpack']
		self.cl_shoulders = ['bark_shoulderpad', 'layered_shoulderpad', 'reinforced_shoulderpad', 'shiny_shoulderpad',
		                     'unpierceable_shoulderpad']
		self.cl_armors = ['plated_leather_armor']
		# , 'brazen_shirt', 'rusty_cuirass', 'knight_armor', 'sacred_brigandine']
		self.cl_rings = ['fate_ring']# ['finger_wrap', 'fate_ring', 'jammed_gem_ring', 'abysmal_ring', 'twisted_root']
		self.cl_shields = ['light_heater', 'reforged_buckler', 'kite_shield', 'heavy_pavise', 'holy_shield']
		self.cl_belts = ['peasant_rope', 'hip_strap', 'ossified_plated_belt', 'embedded_belt', 'mithril_chain_belt']

		self.all_items = {'helm':  self.cl_helms, 'weapon': self.cl_weapons, 'gloves': self.cl_gloves,
		                  'necklace': self.cl_necklaces, 'bag': self.cl_bags, 'armor': self.cl_armors,
		                  'ring': self.cl_rings, 'shield': self.cl_shields}
		# self.all_items = {'helm':  self.cl_helms, 'weapon': self.cl_weapons, 'gloves': self.cl_gloves,
		#                   'pants': self.cl_pants, 'boots': self.cl_boots, 'necklace': self.cl_necklaces,
		#                   'bag':   self.cl_bags, 'shoulder': self.cl_shoulders, 'armor': self.cl_armors,
		#                   'ring':  self.cl_rings, 'shield': self.cl_shields, 'belt': self.cl_belts}

		self.uuid = uuid4().hex if not main else 0
		self.iquality = None
		self.itype = None
		self.ilevel = None
		self.iclass = None
		self.iname = None
		self.item_locked = False

		# Item modifiers #
		self.base_imods = {
				'mov_speed': 0,
				'defense': 0,
				'additional_defense': 0,
				'pct_defense': 0,
				'min_att': 0,
				'max_att': 0,
				'pct_attack': 0,
				'max_hp': 0,
				'max_mp': 0,
				'max_vigor': 0,
				'extra_inv': 0}
		self.imods = {}

		# Item imod selection #
		self.max_additional_imod = {'normal': 0, 'magic': 2, 'rare': 3, 'set': 4, 'unique': 6, 'epic': 8}
		# self.max_additional_imod = {'normal': 0, 'magic': 2, 'rare': 2, 'set': 2, 'unique': 2, 'epic': 2}
		self.imod_multiplier = {'normal': 1, 'magic': 1.3, 'rare': 1.65, 'set': 2.05, 'unique': 2.5, 'epic': 3}
		self.general_possible_imods = {
				'helm': {'additional_defense': 25, 'pct_defense': 65, 'max_hp': 10},
				'weapon': {'min_att': 33, 'max_att': 33, 'pct_attack': 33},
				'gloves': {'additional_defense': 100},
				'pants': {'additional_defense': 95, 'extra_inv': 5},
				'boots': {'additional_defense': 85, 'mov_speed': 5, 'max_vigor': 10},
				'necklace': {'max_hp': 90, 'max_mp': 10},
				'bag': {'extra_inv': 90, 'mov_speed': 10},
				'shoulder': {'additional_defense': 35, 'pct_defense': 35, 'max_hp': 20, 'extra_inv': 10},
				'armor': {'additional_defense': 40, 'pct_defense': 40, 'max_hp': 20},
				'ring': {'max_hp': 10, 'max_mp': 90},
				'shield': {'additional_defense': 65, 'pct_defense': 30, 'max_hp': 5},
				'belt': {'max_vigor': 95, 'extra_inv': 5}}
		self.possible_imods = {}

		# Move items #
		self.item_drag = False
		self.cell_pressed, self.cell_released = None, None

	@staticmethod
	def refresh_surfaces():
		"""Refreshes the item info surfaces at the beginning of the loading (saved items info)"""

		for item in sett.current_game['equipped'].values():
			if item is not None: item.update_item_info()

		for item in sett.current_game['inv_items'].values():
			if item is not None and item != 'locked':
				item.update_item_info()

	def calc_iquality(self):
		"""Calculates the item quality"""

		# Item quality chance #
		epic_chance = 1
		unique_chance = 3
		set_chance = 8
		rare_chance = 15
		magic_chance = 25

		roll = r.randint(1, 100)
		if roll <= epic_chance:
			self.iquality = 'epic'
		if self.iquality is None:
			roll = r.randint(1, 100)
			if roll <= unique_chance:
				self.iquality = 'unique'
		if self.iquality is None:
			roll = r.randint(1, 100)
			if roll <= set_chance:
				self.iquality = 'set'
		if self.iquality is None:
			roll = r.randint(1, 100)
			if roll <= rare_chance:
				self.iquality = 'rare'
		if self.iquality is None:
			roll = r.randint(1, 100)
			if roll <= magic_chance:
				self.iquality = 'magic'
		if self.iquality is None:
			self.iquality = 'normal'

	def calc_imods(self):
		"""Calculates the item modifiers based on the item quality multiplier (better iquality: better imods)"""

		def calc_imod_values(imod):
			"""Returns a new generated value for the given item modifier"""

			val = 0

			if imod == 'mov_speed':
				val = 0.05
				if self.itype == 'bag': val = -val
			elif imod == 'additional_defense':
				val = r.randint(10, 50)
			elif imod == 'pct_defense':
				val = r.randint(5, 10)
			elif imod == 'min_att': # # Upgrading 5-10% of min_att as direct min_att #
				val = r.randint(int(5*0.01*self.imods['min_att']), int(10*0.01*self.imods['min_att']))
			elif imod == 'max_att': # # Upgrading 5-10% of max_att as direct max_att #
				val = r.randint(int(5*0.01*self.imods['max_att']), int(10*0.01*self.imods['max_att']))
			elif imod == 'pct_attack':
				val = r.randint(5, 10)
			elif imod == 'max_hp':
				val = r.randint(5, 8)
			elif imod == 'max_mp':
				val = r.randint(5, 8)
			elif imod == 'max_vigor':
				val = 1
			elif imod == 'extra_inv':
				val = r.randint(0, 1)

			return val

		# Base imod definition #
		for base_imod, value in self.base_imods.items():
			if base_imod == 'min_att':
				self.base_imods['min_att'] = self.base_imods['min_att']*self.imod_multiplier[self.iquality]
			elif base_imod == 'max_att':
				self.base_imods['max_att'] = self.base_imods['max_att']*self.imod_multiplier[self.iquality]
			else:
				self.base_imods[base_imod] *= self.imod_multiplier[self.iquality]
			self.imods[base_imod] = self.base_imods[base_imod]

		# Checking given % #
		# self.imods['additional_defense'] += self.base_imods['pct_defense']*0.01*self.base_imods['defense']

		# Generate item modifiers randomly #
		chance = 45 # Not used, maybe to modify the chances of adding another additional modifier after a successful one

		# Adding additional modifiers (imods) based on the iquality #
		for add_imod in range(self.max_additional_imod[self.iquality]):
			if r.randint(1, 100) <= chance: # 100% chance of get an additional modifier
				chance -= 5
				if len(self.possible_imods.keys()) > 0:
					sel_imod = r.choices(list(self.possible_imods.keys()), weights=list(self.possible_imods.values()), k=1)[0]
					value = calc_imod_values(sel_imod)
					self.base_imods[sel_imod] += value
					self.imods[sel_imod] = self.base_imods[sel_imod]

		if self.imods['min_att'] > self.imods['max_att']:
			self.imods['min_att'] = self.imods['max_att']

	def update_item_info(self):
		"""Should store imods as surfaces"""
		"""Return a dictionary with all the item modifiers information"""

		info = []

		iquality_color = ''
		if self.iquality == 'epic': iquality_color = col_purple
		if self.iquality == 'unique': iquality_color = col_gold
		if self.iquality == 'set': iquality_color = col_green
		if self.iquality == 'rare': iquality_color = col_yellow
		if self.iquality == 'magic': iquality_color = col_blue
		if self.iquality == 'normal': iquality_color = col_white
		if self.item_locked: iquality_color = col_grey

		txt_color = col_grey if self.item_locked else col_white

		name = readable_text(self.iname, '_')
		info.append(text(name, font_style=info_font, font_size=20, color=iquality_color)[0])
		info.append(text(f'({self.iquality.title()} quality)', font_style=info_font, font_size=11,
		                             color=iquality_color)[0])
		if self.item_locked:
			info.append(text(f'Item locked', font_style=info_font, font_size=12, color=col_red)[0])

		for imod, value in self.imods.items():
			if value != 0:
				if imod == 'min_att':
					info.append(text(f'Attack: ({int(value)}-{int(self.imods["max_att"])})',
					                             font_style=info_font, font_size=12, color=txt_color)[0])
				elif imod == 'max_att': pass
				elif imod == 'pct_defense':
					info.append(text(f'Upgraded defense: {int(self.imods["pct_defense"]*0.01*self.imods["defense"])} '
					                 f'({int(value)}%)', font_style=info_font, font_size=12, color=txt_color)[0])
				elif imod == 'pct_attack':
					info.append(text(f'Upgraded attack: ({int(self.imods["pct_attack"]*0.01*self.imods["min_att"])}-'
					                 f'{int(self.imods["pct_attack"]*0.01*self.imods["max_att"])}) ({int(value)}%)',
					                 font_style=info_font, font_size=12, color=txt_color)[0])
				elif imod == 'max_hp': info.append(text(f'Max HP: {int(value)}',
				                                        font_style=info_font, font_size=12, color=txt_color)[0])
				elif imod == 'max_mp': info.append(text(f'Max MP: {int(value)}',
				                                        font_style=info_font, font_size=12, color=txt_color)[0])
				else:
					info.append(text(f'{readable_text(imod, "_")}: {int(value)}', font_style=info_font, font_size=12,
					                             color=txt_color)[0])

		item_info[self.uuid] = info

	def equip(self, frm=None):
		"""Equips the item. The equipment socket has to be empty or it will replace it"""

		sett.current_game['equipped'][self.itype] = self
		if frm == 'cursor':
			IOGUI.item_on_cursor = None
		elif frm == 'inv':
			sett.current_game['inv_items'][IOItem.cell_pressed] = None

		self.add_imods_to_chstats('equ')

	def unequip(self, to=None):
		"""Unequips the given item. 'cursor' will replace any existing item"""

		if to == 'cursor':
			IOGUI.item_on_cursor = sett.current_game['equipped'][self.itype]
		elif to == 'inv':
			sett.current_game['equipped'][self.itype].pick_item()
		sett.current_game['equipped'][self.itype] = None

		self.add_imods_to_chstats('unequ')

	@staticmethod
	def swap_items(type='cursor'):
		"""Swaps the item_on_cursor (type='cursor') or right-clicked item (type='inventory')
			with the clicked/released item """

		win_pressed, win_released = 'inv', 'inv'
		for cell in sett.current_game['equipped'].keys():
			if cell == IOItem.cell_pressed:
				win_pressed = 'equ'
			if cell == IOItem.cell_released:
				win_released = 'equ'

		if type == 'cursor':
			if win_pressed == 'equ':
				if IOItem.item_drag:
					if sett.current_game['inv_items'][IOItem.cell_released].itype == IOGUI.item_on_cursor.itype:
						sett.current_game['inv_items'][IOItem.cell_released].equip()
						sett.current_game['inv_items'][IOItem.cell_released] = IOGUI.item_on_cursor
						IOGUI.item_on_cursor = None
				else:
					item_buffer = sett.current_game['equipped'][IOItem.cell_pressed]
					sett.current_game['equipped'][IOItem.cell_pressed].unequip()
					IOGUI.item_on_cursor.equip()
					IOGUI.item_on_cursor = item_buffer
			elif win_pressed == 'inv':
				if IOItem.item_drag:
					if win_released == 'equ':
						item_buffer = sett.current_game['equipped'][IOItem.cell_released]
						sett.current_game['equipped'][IOItem.cell_released].unequip()
						IOGUI.item_on_cursor.equip('cursor')
						sett.current_game['inv_items'][IOItem.cell_pressed] = item_buffer
					elif win_released == 'inv':
						sett.current_game['inv_items'][IOItem.cell_pressed], sett.current_game['inv_items'][IOItem.cell_released] = \
							sett.current_game['inv_items'][IOItem.cell_released], IOGUI.item_on_cursor
						IOGUI.item_on_cursor = None
				else:
					IOGUI.item_on_cursor, sett.current_game['inv_items'][IOItem.cell_pressed] = sett.current_game['inv_items'][
						                                                             IOItem.cell_pressed], IOGUI.item_on_cursor

		elif type == 'quick_eq':
			item_buffer = sett.current_game['equipped'][sett.current_game['inv_items'][IOItem.cell_pressed].itype]
			item_buffer.unequip()
			sett.current_game['inv_items'][IOItem.cell_pressed].equip()
			sett.current_game['inv_items'][IOItem.cell_pressed] = item_buffer
			IOInv.update_sub_win(rects=False)

	def add_imods_to_chstats(self, mode=None):
		"""Adds every item modifier to the character stats"""

		for imod, val in self.imods.items():
			if imod == 'pct_defense':
				stat = 'defense'
				value = val*0.01*self.imods['defense']
			elif imod == 'additional_defense':
				stat = 'defense'
				value = val
			elif imod == 'pct_attack':
				value = val*0.01*self.imods['min_att']
				if mode == 'equ': sett.current_game['current_char'].mod_stats('min_att', value)
				elif mode == 'unequ': sett.current_game['current_char'].mod_stats('min_att', -value)
				stat = 'max_att'
				value = val*0.01*self.imods['max_att']
			else:
				stat, value = imod, val

			if mode == 'equ': sett.current_game['current_char'].mod_stats(stat, value)
			elif mode == 'unequ': sett.current_game['current_char'].mod_stats(stat, -value)

		IOEqu.update_sub_win()
		IOInv.update_sub_win(rects=False)

	def pick_item(self):
		"""If enough space, places the item in the inventory"""

		for cell, item in sett.current_game['inv_items'].items():
			if item is None:
				sett.current_game['inv_items'][cell] = self
				break

		IOInv.update_sub_win(rects=False)

	@staticmethod
	def delete_item():
		"""Deletes the item on cursor"""

		del item_info[IOGUI.item_on_cursor.uuid]
		IOGUI.message(f'|| ({IOGUI.item_on_cursor.iquality.title()}) '
		              f'{readable_text(IOGUI.item_on_cursor.iname, "_")} || deleted')
		IOGUI.item_on_cursor = None

	def draw_single_item(self, position):
		"""Displays the item with its iquality background"""

		screen.blit(iquality_img[self.iquality], position)
		screen.blit(item_img[self.iname], position)


IOItem = Item(main=True)


# Helms #
class RaggedBandana(Item):
	def __init__(self):
		super().__init__()

		self.itype = 'helm'
		self.ilevel = 1
		self.iname = 'ragged_bandana'
		self.base_imods['defense'] = r.randint(1, 8)

		self.possible_imods = self.general_possible_imods[self.itype]


class MithrilHelmet(Item):
	def __init__(self):
		super().__init__()

		self.itype = 'helm'
		self.ilevel = 20
		self.iname = 'mithril_helmet'
		self.name = 'Mithril helmet'
		self.base_imods['defense'] = r.randint(200, 250)

		self.possible_imods = self.general_possible_imods[self.itype]


# Weapons #
class FistKnife(Item):
	def __init__(self):
		super().__init__()

		self.itype = 'weapon'
		self.ilevel = 1
		self.iname = 'fist_knife'
		self.base_imods['min_att'] = r.randint(1, 3)
		self.base_imods['max_att'] = r.randint(2, 5)

		self.possible_imods = self.general_possible_imods[self.itype]


class Gladius(Item):
	def __init__(self):
		super().__init__()

		self.itype = 'weapon'
		self.ilevel = 5
		self.iname = 'gladius'
		self.base_imods['min_att'] = r.randint(8, 16)
		self.base_imods['max_att'] = r.randint(10, 22)

		self.possible_imods = self.general_possible_imods[self.itype]


class LongSword(Item):
	def __init__(self):
		super().__init__()

		self.itype = 'weapon'
		self.ilevel = 15
		self.iname = 'long_sword'
		self.base_imods['min_att'] = r.randint(12, 25)
		self.base_imods['max_att'] = r.randint(8, 28)

		self.possible_imods = self.general_possible_imods[self.itype]


# Gloves #
class HandWraps(Item):
	def __init__(self):
		super().__init__()

		self.itype = 'gloves'
		self.ilevel = 1
		self.iname = 'hand_wraps'
		self.base_imods['defense'] = r.randint(3, 8)

		self.possible_imods = self.general_possible_imods[self.itype]


# Necklaces #
class CobwebString(Item):
	def __init__(self):
		super().__init__()

		self.itype = 'necklace'
		self.ilevel = 5
		self.iname = 'cobweb_string'
		self.base_imods['max_hp'] = r.randint(0, 10)

		self.possible_imods = self.general_possible_imods[self.itype]


class OrnamentalChain(Item):
	def __init__(self):
		super().__init__()

		self.itype = 'necklace'
		self.ilevel = 5
		self.iname = 'ornamental_chain'
		self.base_imods['max_hp'] = r.randint(5, 25)

		self.possible_imods = self.general_possible_imods[self.itype]


class SuperstitiousAmulet(Item):
	def __init__(self):
		super().__init__()

		self.itype = 'necklace'
		self.ilevel = 15
		self.iname = 'superstitious_amulet'
		self.base_imods['max_hp'] = r.randint(0, 10)
		self.base_imods['max_mp'] = r.randint(0, 10)

		self.possible_imods = self.general_possible_imods[self.itype]


class GlowingCord(Item):
	def __init__(self):
		super().__init__()

		self.itype = 'necklace'
		self.ilevel = 22
		self.iname = 'glowing_cord'

		self.possible_imods = self.general_possible_imods[self.itype]


class MysticalCollar(Item):
	def __init__(self):
		super().__init__()

		self.itype = 'necklace'
		self.ilevel = 30
		self.iname = 'mystical_collar'

		self.possible_imods = self.general_possible_imods[self.itype]


# Bags #
class SmallPouch(Item):
	def __init__(self):
		super().__init__()

		self.itype = 'bag'
		self.ilevel = 5
		self.iname = 'small_pouch'
		self.base_imods['extra_inv'] = 1

		self.possible_imods = self.general_possible_imods[self.itype]


# Armors #
class PlatedLeatherArmor(Item):
	def __init__(self):
		super().__init__()

		self.itype = 'armor'
		self.ilevel = 5
		self.iname = 'plated_leather_armor'
		self.base_imods['defense'] = r.randint(15, 32)

		self.possible_imods = self.general_possible_imods[self.itype]


# Rings #
class FateRing(Item):
	def __init__(self):
		super().__init__()

		self.itype = 'ring'
		self.ilevel = 5
		self.iname = 'fate_ring'

		self.possible_imods = self.general_possible_imods[self.itype]


# Shields #
class LightHeater(Item):
	def __init__(self):
		super().__init__()

		self.itype = 'shield'
		self.ilevel = 10
		self.iname = 'light_heater'
		self.base_imods['defense'] = r.randint(12, 24)

		self.possible_imods = self.general_possible_imods[self.itype]


class ReforgedBuckler(Item):
	def __init__(self):
		super().__init__()

		self.itype = 'shield'
		self.ilevel = 20
		self.iname = 'reforged_buckler'
		self.base_imods['defense'] = r.randint(18, 36)
		self.base_imods['pct_defense'] = r.randint(10, 20)

		self.possible_imods = self.general_possible_imods[self.itype]


class KiteShield(Item):
	def __init__(self):
		super().__init__()

		self.itype = 'shield'
		self.ilevel = 30
		self.iname = 'kite_shield'
		self.base_imods['defense'] = r.randint(32, 64)

		self.possible_imods = self.general_possible_imods[self.itype]


class HeavyPavise(Item):
	def __init__(self):
		super().__init__()

		self.itype = 'shield'
		self.ilevel = 40
		self.iname = 'heavy_pavise'
		self.base_imods['defense'] = r.randint(48, 96)
		self.base_imods['pct_defense'] = r.randint(0, 10)

		self.possible_imods = self.general_possible_imods[self.itype]


class HolyShield(Item):
	def __init__(self):
		super().__init__()

		self.itype = 'shield'
		self.ilevel = 50
		self.iname = 'holy_shield'
		self.base_imods['defense'] = r.randint(128, 256)
		self.base_imods['pct_defense'] = r.randint(5, 25)

		self.possible_imods = self.general_possible_imods[self.itype]


def gen_item(itype=None, iclass=None, iqual=None):
	"""Generates a new instance of the possible items"""

	iquality = iqual
	if itype is not None: item_type = itype
	else: item_type = r.choice(list(IOItem.all_items.keys()))

	if iclass is not None: item_class = iclass
	else: item_class = r.choice(IOItem.all_items[item_type])

	# Helms #
	if item_class == 'ragged_bandana':
		item = RaggedBandana()
	elif item_class == 'mithril_helmet':
		item = MithrilHelmet()

	# Weapons #
	elif item_class == 'fist_knife':
		item = FistKnife()
	elif item_class == 'gladius':
		item = Gladius()
	elif item_class == 'long_sword':
		item = LongSword()

	# Gloves #
	elif item_class == 'hand_wraps':
		item = HandWraps()

	# Necklaces #
	elif item_class == 'cobweb_string':
		item = CobwebString()
	elif item_class == 'ornamental_chain':
		item = OrnamentalChain()
	elif item_class == 'superstitious_amulet':
		item = SuperstitiousAmulet()
	elif item_class == 'glowing_cord':
		item = GlowingCord()
	elif item_class == 'mystical_collar':
		item = MysticalCollar()

	# Bags #
	elif item_class == 'small_pouch':
		item = SmallPouch()

	# Armors #
	elif item_class == 'plated_leather_armor':
		item = PlatedLeatherArmor()

	# Rings #
	elif item_class == 'fate_ring':
		item = FateRing()

	# Shields #
	elif item_class == 'light_heater':
		item = LightHeater()

	elif item_class == 'reforged_buckler':
		item = ReforgedBuckler()

	elif item_class == 'kite_shield':
		item = KiteShield()

	elif item_class == 'heavy_pavise':
		item = HeavyPavise()

	elif item_class == 'holy_shield':
		item = HolyShield()

	else: raise ValueError("The item_class doesn't exist")

	item.iclass = iclass

	if iquality is not None: item.iquality = iquality
	else: item.calc_iquality()

	item.calc_imods()
	item.update_item_info()

	return item
