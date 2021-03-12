from map import *


class Atlas:
	def __init__(self):
		self.img_fade_bg = pg.image.load('data/images/gui/fade_bg.png').convert_alpha()
		self.layout = [
				[0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000],
				[0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000],
				[0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000],
				[0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000],
				[0000, 0000, PrLa, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000],
				[0000, 0000, ArPl, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000],
				[0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000],
				[0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000],
				[0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 1111, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000],
				[0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000],
				[0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000],
				[0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000],
				[0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000],
				[0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000],
				[0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000],
				[0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000],
				[0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000],
				]
		self.current_coords = ()
		self.surrounding_coords = {}

		self.check_surrounding_areas()
		self.fading = {'menu': 'off', 'transition': 'off', 'combat': 'off'}
		self.opacity_counter = {'menu': 0, 'transition': 0, 'combat': 0}

	def locate_current_area(self):
		"""Locates the current area and saves its coordinates"""

		def get_current_coords():
			"""Loops through the tiles of the given row (used to break from both main loop and nested loop with 'return')"""

			for row_index, row in enumerate(self.layout):
				for col_index, area in enumerate(row):
					if area == sett.current_game['current_map']:
						coord = (row_index, col_index)
						return coord

		self.current_coords = get_current_coords()
		self.surrounding_coords = {
				'north': (self.current_coords[0]-1, self.current_coords[1]),
				'south': (self.current_coords[0]+1, self.current_coords[1]),
				'west': (self.current_coords[0], self.current_coords[1]-1),
				'east': (self.current_coords[0], self.current_coords[1]+1)}

	def check_surrounding_areas(self):
		"""Checks the surrounding areas to the current map"""

		def explore(cardinal):
			"""Returns the content of the given direction"""

			return self.layout[self.surrounding_coords[cardinal][0]][self.surrounding_coords[cardinal][1]]

		self.locate_current_area()
		for direction in self.surrounding_coords.keys():
			if type(explore(direction)) != int:
				self.open_path(direction)

	@staticmethod
	def open_path(cardinal):
		"""Opens a path towards the given cardinal direction"""

		print('Opening path to:', cardinal)

		if sett.current_game['current_map'].paths_opened[cardinal] is None:
			print('No path pre-existant')
			tile, wider_tile = None, None
			if cardinal == 'west' or cardinal == 'east':
				sel_tile = r.randint(1, 8)
				if cardinal == 'west': tile = sett.current_game['current_map'].map_layout[sel_tile][0]
				elif cardinal == 'east': tile = sett.current_game['current_map'].map_layout[sel_tile][-1]
			elif cardinal == 'north' or cardinal == 'south':
				sel_tile = r.randint(1, 13)
				if cardinal == 'north':
					tile = sett.current_game['current_map'].map_layout[0][sel_tile]
					wider_tile = sett.current_game['current_map'].map_layout[0][sel_tile+1]
				elif cardinal == 'south':
					tile = sett.current_game['current_map'].map_layout[-1][sel_tile]
					wider_tile = sett.current_game['current_map'].map_layout[-1][sel_tile+1]
			else: raise ValueError(f'The given cardinal point is not valid')

			if type(tile) is not int:
				sett.current_game['current_map'].remove_from_map(tile[1])
				sett.current_game['current_map'].paths_opened[cardinal] = sel_tile
			else: print('The main path is already opened')
			if type(wider_tile) is not int: sett.current_game['current_map'].remove_from_map(wider_tile[1])

		else:
			if cardinal == 'north':
				tile = sett.current_game['current_map'].map_layout[0][sett.current_game['current_map'].paths_opened[cardinal]]
				wider_tile = sett.current_game['current_map'].map_layout[0][
					sett.current_game['current_map'].paths_opened[cardinal]+1]
			elif cardinal == 'south':
				tile = sett.current_game['current_map'].map_layout[-1][sett.current_game['current_map'].paths_opened[cardinal]]
				wider_tile = sett.current_game['current_map'].map_layout[-1][
						sett.current_game['current_map'].paths_opened[cardinal]+1]
			elif cardinal == 'west':
				tile = sett.current_game['current_map'].map_layout[sett.current_game['current_map'].paths_opened[cardinal][0]]
				wider_tile = sett.current_game['current_map'].map_layout[
						sett.current_game['current_map'].paths_opened[cardinal]+1][0]
			elif cardinal == 'east':
				tile = sett.current_game['current_map'].map_layout[sett.current_game['current_map'].paths_opened[cardinal][-1]]
				wider_tile = sett.current_game['current_map'].map_layout[
						sett.current_game['current_map'].paths_opened[cardinal]+1][-1]
			else: raise ValueError(f'The given cardinal point is not valid')

			try:
				if type(tile) is not int: sett.current_game['current_map'].remove_from_map(tile[1])
			except IndexError: pass
			try:
				if type(wider_tile) is not int: sett.current_game['current_map'].remove_from_map(wider_tile[1])
			except IndexError: pass

		# TODO After, check the spawning on the removed tiles (paths) to disable it (not blocking paths)

	def check_transition(self):
		"""Checks continuously the map transition (if character changes to another adjacent map)"""

		char_pos = sett.current_game['current_char'].pos
		char_rect = sett.current_game['current_char'].visual_rect
		path = sett.current_game['current_map'].paths_opened
		if char_pos[1] < 0:
			if path['north'] is not None:
				if self.fading['menu'] == 'off':
					self.fade_bg('transition', 'in')
					sett.current_game['current_char'].stop_movement()
					sett.current_game['current_char'].move_up = True
					if self.opacity_counter['transition'] >= 255:
						self.fading['transition'] = 'out'
						self.displace_char('north')
						self.change_map('north')

		elif char_pos[1]+char_rect.h*0.5 > 608:
			if path['south'] is not None:
				if self.fading['menu'] == 'off':
					self.fade_bg('transition', 'in')
					sett.current_game['current_char'].stop_movement()
					sett.current_game['current_char'].move_down = True
					if self.opacity_counter['transition'] >= 255:
						self.fading['transition'] = 'out'
						self.displace_char('south')
						self.change_map('south')
		elif char_pos[0] < 0:
			if path['west'] is not None:
				if self.fading['menu'] == 'off':
					self.fade_bg('transition', 'in')
					sett.current_game['current_char'].stop_movement()
					sett.current_game['current_char'].move_left = True
					if self.opacity_counter['transition'] >= 255:
						self.fading['transition'] = 'out'
						self.displace_char('west')
						self.change_map('west')
		elif char_pos[0]+char_rect.w > sett.disp_w:
			if path['east'] is not None:
				if self.fading['menu'] == 'off':
					self.fade_bg('transition', 'in')
					sett.current_game['current_char'].stop_movement()
					sett.current_game['current_char'].move_right = True
					if self.opacity_counter['transition'] >= 255:
						self.fading['transition'] = 'out'
						self.displace_char('east')
						self.change_map('east')
		else:
			if self.fading['transition'] == 'out':
				self.fade_bg('transition', 'out')
				if self.opacity_counter['transition'] <= 0:
					self.fading['transition'] = 'off'

	def fade_bg(self, type, mode, opacity_limit=255):
		"""Gradually fades in the black background"""

		fading_speed = 5
		if mode == 'in':
			blit_alpha(screen, self.img_fade_bg, (0, 0), self.opacity_counter[type])
			if self.opacity_counter[type] < opacity_limit:
				self.opacity_counter[type] += fading_speed
			self.fading[type] = 'in'
		elif mode == 'out':
			if self.opacity_counter[type] > 0:
				blit_alpha(screen, self.img_fade_bg, (0, 0), self.opacity_counter[type])
				self.opacity_counter[type] -= fading_speed

	@staticmethod
	def displace_char(cardinal):
		"""Displaces the character when a map transaction is happening"""

		if cardinal == 'north':
			sett.current_game['current_char'].pos[1] = 608-sett.current_game['current_char'].visual_rect.h*0.5
		elif cardinal == 'south':
			sett.current_game['current_char'].pos[1] = 0
		elif cardinal == 'west':
			sett.current_game['current_char'].pos[0] = sett.disp_w-sett.current_game['current_char'].visual_rect.w
		elif cardinal == 'east':
			sett.current_game['current_char'].pos[0] = 0

	def change_map(self, cardinal):
		"""Changes the current map to the one on the given cardinal point"""

		print('changing to:', cardinal)
		paths_opened_buffer = sett.current_game['current_map'].paths_opened
		sett.current_game['current_map'] = \
			self.layout[self.surrounding_coords[cardinal][0]][self.surrounding_coords[cardinal][1]]
		if cardinal == 'north':
			sett.current_game['current_map'].paths_opened['south'] = paths_opened_buffer['north']
		elif cardinal == 'south':
			sett.current_game['current_map'].paths_opened['north'] = paths_opened_buffer['south']
		elif cardinal == 'west':
			sett.current_game['current_map'].paths_opened['east'] = paths_opened_buffer['west']
		elif cardinal == 'east':
			sett.current_game['current_map'].paths_opened['west'] = paths_opened_buffer['east']

		self.check_surrounding_areas()


IOAtlas = Atlas()
