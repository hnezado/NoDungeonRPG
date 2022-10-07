from map_old import *


class Atlas:
	def __init__(self):
		self.img_fade_bg = pg.image.load('data/images/gui/fade_bg.png').convert_alpha()
		self.layout = [
				[0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000],
				[0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000],
				[0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000],
				[0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000],
				[0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000],
				[0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000],
				[0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, CoPl, 0000, 0000, 0000, 0000, 0000, 0000],
				[0000, 0000, 0000, 0000, 0000, 0000, 0000, HTNW, HeTN, HTNE, FrLa, 0000, 0000, 0000, 0000, 0000, 0000],
				[0000, 0000, 0000, 0000, 0000, 0000, 0000, HeTW, HeTo, HeTE, PrLa, ArPl, 0000, 0000, 0000, 0000, 0000],
				[0000, 0000, 0000, 0000, 0000, 0000, 0000, HTSW, HeTS, HTSE, 0000, 0000, 0000, 0000, 0000, 0000, 0000],
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

		self.explore_area()
		self.fading = {'menu': 'off', 'transition': 'off'}
		self.opacity_counter = 0

	def explore_area(self):
		"""Explores the current area and its surroundings in the atlas layout (North, South, West, East)"""

		self.set_maps_coords()
		self.current_coords = self.get_current_area_coords()
		self.surrounding_coords = self.get_surrounding_areas_coords()
		self.set_paths()
		self.match_paths()
		self.open_paths()

	def set_maps_coords(self):
		"""Reads and sets the atlas coordinates of every map"""

		for row_index, row in enumerate(self.layout):
			for col_index, map in enumerate(row):
				if type(map) != int:
					map.coordinates = (row_index, col_index)

	def get_current_area_coords(self):
		"""Returns the current area coordinates"""

		for row_index, row in enumerate(self.layout):
			for col_index, map in enumerate(row):
				# Esta forma no va a funcionar ya que son dos instancias diferentes en el momento que carges un juego guardado
				# Está comparando las intancias
				# Tal vez si guardo las coordenadas correspondientes a cada instancia de mapa en el mismo mapa
				if type(map) != int:
					if map.coordinates == sett.current_game['current_map'].coordinates:
						coordinates = (row_index, col_index)
						return coordinates

	def get_surrounding_areas_coords(self):
		"""Returns the surrounding area coordinates"""

		return {'north': (self.current_coords[0]-1, self.current_coords[1]),
		        'south': (self.current_coords[0]+1, self.current_coords[1]),
		        'west': (self.current_coords[0], self.current_coords[1]-1),
		        'east': (self.current_coords[0], self.current_coords[1]+1)}

	def set_paths(self):
		"""Sets paths towards existent surrounding areas"""

		for cardinal in self.surrounding_coords.keys():
			area = self.layout[self.surrounding_coords[cardinal][0]][self.surrounding_coords[cardinal][1]]
			if type(area) != int:
				if sett.current_game['current_map'].paths_opened[cardinal] is None:
					if cardinal == 'north' or cardinal == 'south':
						sett.current_game['current_map'].paths_opened[cardinal] = r.randint(1, 13)
					elif cardinal == 'west' or cardinal == 'east':
						sett.current_game['current_map'].paths_opened[cardinal] = r.randint(1, 8)

	def match_paths(self):
		"""Match the connected areas paths with the current area paths positions"""

		for cardinal in self.surrounding_coords.keys():
			connected_area = self.layout[self.surrounding_coords[cardinal][0]][self.surrounding_coords[cardinal][1]]
			opposite_cardinal = None
			if cardinal == 'north': opposite_cardinal = 'south'
			elif cardinal == 'south': opposite_cardinal = 'north'
			elif cardinal == 'west': opposite_cardinal = 'east'
			elif cardinal == 'east': opposite_cardinal = 'west'

			if type(connected_area) != int:
				connected_area.paths_opened[opposite_cardinal] = sett.current_game['current_map'].paths_opened[cardinal]

	@staticmethod
	def open_paths():
		"""Updates the paths and opens them if they haven't been opened yet"""

		for cardinal in sett.current_game['current_map'].paths_opened.keys():
			tile_index = sett.current_game['current_map'].paths_opened[cardinal]
			if tile_index is not None:
				# Here is opened the path extension (only north and south paths are wide x2)
				tile, tile_extended = None, None
				if cardinal == 'north' or cardinal == 'south':
					if cardinal == 'north':
						tile = sett.current_game['current_map'].map_layout[0][tile_index]
						tile_extended = sett.current_game['current_map'].map_layout[0][tile_index+1]
					elif cardinal == 'south':
						tile = sett.current_game['current_map'].map_layout[-1][tile_index]
						tile_extended = sett.current_game['current_map'].map_layout[-1][tile_index+1]

					if tile_extended is not None and type(tile_extended) != int:
						if len(tile_extended) > 1:
							if tile_extended[1].type == 'wall':
								sett.current_game['current_map'].remove_from_map(tile_extended[1])

				elif cardinal == 'west':
					tile = sett.current_game['current_map'].map_layout[tile_index][0]
				elif cardinal == 'east':
					tile = sett.current_game['current_map'].map_layout[tile_index][-1]

				if tile is not None and type(tile) != int:
					if len(tile) > 1:
						if tile[1].type == 'wall':
							sett.current_game['current_map'].remove_from_map(tile[1])

	def check_transition(self):
		"""Checks continuously the map transition (if character changes to another adjacent map)"""

		char_pos = sett.current_game['current_char'].pos
		char_rect = sett.current_game['current_char'].visual_rect
		path = sett.current_game['current_map'].paths_opened
		if char_pos[1] < 0:
			if path['north'] is not None:
				sett.current_game['current_char'].move_left = False
				sett.current_game['current_char'].move_right = False
				if self.fading['menu'] == 'off':
					self.fading['transition'] = 'in'
					self.fade_bg('in', 255)
					sett.current_game['current_char'].move_up = True
					if self.opacity_counter >= 255:
						self.fading['transition'] = 'out'
						self.displace_char('north')
						self.change_map('north')

		elif char_pos[1]+char_rect.h*0.5 > 608:
			if path['south'] is not None:
				sett.current_game['current_char'].move_left = False
				sett.current_game['current_char'].move_right = False
				if self.fading['menu'] == 'off':
					self.fading['transition'] = 'in'
					self.fade_bg('in', 255)
					sett.current_game['current_char'].move_down = True
					if self.opacity_counter >= 255:
						self.fading['transition'] = 'out'
						self.displace_char('south')
						self.change_map('south')
		elif char_pos[0] < 0:
			if path['west'] is not None:
				sett.current_game['current_char'].move_up = False
				sett.current_game['current_char'].move_down = False
				if self.fading['menu'] == 'off':
					self.fading['transition'] = 'in'
					self.fade_bg('in', 255)
					sett.current_game['current_char'].move_left = True
					if self.opacity_counter >= 255:
						self.fading['transition'] = 'out'
						self.displace_char('west')
						self.change_map('west')
		elif char_pos[0]+char_rect.w > sett.disp_w:
			if path['east'] is not None:
				sett.current_game['current_char'].move_up = False
				sett.current_game['current_char'].move_down = False
				if self.fading['menu'] == 'off':
					self.fading['transition'] = 'in'
					self.fade_bg('in', 255)
					sett.current_game['current_char'].move_right = True
					if self.opacity_counter >= 255:
						self.fading['transition'] = 'out'
						self.displace_char('east')
						self.change_map('east')
		else:
			if self.fading['transition'] == 'out':
				self.fade_bg('out')
				if self.opacity_counter <= 0:
					self.fading['transition'] = 'off'

	def fade_bg(self, mode, opacity_limit=200):
		"""Gradually fades in the black background"""

		fading_speed = 5
		if mode == 'in':
			blit_alpha(screen, self.img_fade_bg, (0, 0), self.opacity_counter)
			if self.opacity_counter < opacity_limit:
				self.opacity_counter += fading_speed
		elif mode == 'out':
			if self.opacity_counter > 0:
				blit_alpha(screen, self.img_fade_bg, (0, 0), self.opacity_counter)
				self.opacity_counter -= fading_speed

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

		sett.current_game['current_map'] = \
			self.layout[self.surrounding_coords[cardinal][0]][self.surrounding_coords[cardinal][1]]

		self.explore_area()


IOAtlas = Atlas()
