from settings import *
import settings as sett

generic_floors = []
generic_walls = []
generic_decos = []
generic_containers = []

# When adding new map_object:
# 1.Create subclass itself with the required variables (self.name, self.type...)
# 2.Add update_mobj() at the end of the new __init__() with the required update strings
# 3.Add the class to create_mobj('instance.name')
# 4.Create an instance if the subclass from map and give it a nickname (Fdf = [DesertFloor()])

# Depth must be at least mov_speed higher than y pos to act like a "3d block"

mobj_imgs = {
		'null': pg.image.load('data/images/null64.png'),
		'blank_floor': pg.image.load('data/images/blank64.png').convert_alpha(),
		'desert_floor': pg.image.load('data/images/map_objects/floors/desert_floor.png').convert_alpha(),
		'grass_floor': pg.image.load('data/images/map_objects/floors/grass_floor.png').convert_alpha(),
		'sand_floor1': pg.image.load('data/images/map_objects/floors/tiled/sand_floor1.png').convert_alpha(),
		'sand_mound1': pg.image.load('data/images/map_objects/floors/tiled/sand_mound1.png').convert_alpha(),
		'wall_rock1': pg.image.load('data/images/map_objects/walls/wall_rock1.png').convert_alpha(),
		'wall_rock2': pg.image.load('data/images/map_objects/walls/wall_rock2.png').convert_alpha(),
		'wall_rock3': pg.image.load('data/images/map_objects/walls/wall_rock3.png').convert_alpha(),
		'wall_rock4': pg.image.load('data/images/map_objects/walls/wall_rock4.png').convert_alpha(),
		'mountain2': pg.image.load('data/images/map_objects/decorations/mountain2.png').convert_alpha(),
		'tree1': pg.image.load('data/images/map_objects/decorations/tree1.png').convert_alpha(),
		'grassy_rock1': pg.image.load('data/images/map_objects/decorations/grassy_rock1.png').convert_alpha(),
		'grassy_rock2': pg.image.load('data/images/map_objects/decorations/grassy_rock2.png').convert_alpha(),
		'grassy_rock3': pg.image.load('data/images/map_objects/decorations/grassy_rock3.png').convert_alpha(),
		'grassy_rock4': pg.image.load('data/images/map_objects/decorations/grassy_rock4.png').convert_alpha(),
		'chest': Sheet('data/images/map_objects/containers/chest.png', dimensions=(2, 1))
}


def create_map_obj(name):
	"""Returns a new instance of the matching provided name"""

	if name == 'blank_floor': return BlankFloor()
	elif name == 'desert_floor': return DesertFloor()
	elif name == 'sand_floor1': return SandFloor1()
	elif name == 'sand_mound1': return SandMound1()
	elif name == 'wall_rock1': return WallRock1()
	elif name == 'wall_rock2': return WallRock2()
	elif name == 'wall_rock3': return WallRock3()
	elif name == 'wall_rock4': return WallRock4()
	elif name == 'mountain2': return Mountain2()
	elif name == 'tree1': return Tree1()
	elif name == 'grassy_rock1': return GrassyRock1()
	elif name == 'grassy_rock2': return GrassyRock2()
	elif name == 'grassy_rock3': return GrassyRock3()
	elif name == 'grassy_rock4': return GrassyRock4()
	elif name == 'chest': return Chest()


class MapObject:
	def __init__(self):

		self.name = None
		self.type = None
		self.tiled = False
		self.map_elements = {'terrain': [], 'climate': []}
		self.pos = None
		self.visual_rect = None
		self.depth = 0
		self.spawnable = False

		self.given_block_rect = None
		self.block_rect = None
		self.opened = False
		self.loot_items = None

	def update_mobj(self, *args):
		"""If is not already in, adds the new instance to the generic object lists"""

		for i in args:
			if i == 'map_elements':
				if self.map_elements['terrain'] == 'all':
					self.map_elements['terrain'] = map_elements['terrain']
				if self.map_elements['climate'] == 'all':
					self.map_elements['climate'] = map_elements['climate']

			elif i == 'lists':
				existent = []
				if self.type == 'floor':
					for floor in generic_floors:
						if floor == self.name:
							existent.append(1)
					if not any(existent):
						generic_floors.append(self)
				elif self.type == 'wall':
					for wall in generic_walls:
						if wall == self.name:
							existent.append(1)
					if not any(existent):
						generic_walls.append(self)
				elif self.type == 'deco':
					for deco in generic_decos:
						if deco == self.name:
							existent.append(1)
					if not any(existent):
						generic_decos.append(self)
				elif self.type == 'container':
					for container in generic_containers:
						if container == self.name:
							existent.append(1)
					if not any(existent):
						generic_containers.append(self)

			elif i == 'v_rect':
				self.visual_rect = mobj_imgs[self.name].get_rect()

			elif i == 'v_rect_sheet':
				self.visual_rect = pg.Rect(0, 0, mobj_imgs[self.name].crop_w, mobj_imgs[self.name].crop_h)

			elif i == 'pos_change':
				if self.visual_rect.h > tile_h:     # Undo the positioning done in map_setting
					self.pos = (self.pos[0], (self.pos[1]-tile_h*0.5+self.visual_rect.h*0.5)+tile_h-self.visual_rect.h)
				self.depth = self.pos[1]+self.depth

			else: raise ValueError(f'The provided argument "{i}" is not registered')


class BlankFloor(MapObject):
	def __init__(self):
		super().__init__()

		self.name = 'blank_floor'
		self.type = 'floor'
		self.spawnable = True

		self.update_mobj('map_elements', 'v_rect')


class DesertFloor(MapObject):
	def __init__(self):
		super().__init__()

		self.name = 'desert_floor'
		self.type = 'floor'
		self.map_elements = {'terrain': ['sand'], 'climate': ['arid']}
		self.spawnable = True

		self.update_mobj('map_elements', 'lists', 'v_rect')


class GrassFloor(MapObject):
	def __init__(self):
		super().__init__()

		self.name = 'grass_floor'
		self.type = 'floor'
		self.map_elements = {'terrain': ['dirt'], 'climate': ['template']}
		self.spawnable = True

		self.update_mobj('map_elements', 'lists', 'v_rect')


class SandFloor1(MapObject):
	def __init__(self):
		super().__init__()

		self.name = 'sand_floor1'
		self.type = 'floor'
		self.tiled = True
		self.map_elements = {'terrain': ['sand'], 'climate': ['arid']}
		self.spawnable = True

		self.update_mobj('map_elements', 'lists', 'v_rect')


class SandMound1(MapObject):
	def __init__(self):
		super().__init__()

		self.name = 'sand_mound1'
		self.type = 'floor'
		self.tiled = True
		self.map_elements = {'terrain': ['sand'], 'climate': ['arid']}
		self.spawnable = True

		self.update_mobj('map_elements', 'lists', 'v_rect')


class WallRock1(MapObject):
	def __init__(self):
		super().__init__()

		self.name = 'wall_rock1'
		self.type = 'wall'
		self.map_elements = {'terrain': 'all', 'climate': 'all'}
		self.depth = 25
		self.given_block_rect = pg.Rect(0, 20, 104, 64)

		self.update_mobj('map_elements', 'lists', 'v_rect')


class WallRock2(MapObject):
	def __init__(self):
		super().__init__()

		self.name = 'wall_rock2'
		self.type = 'wall'
		self.map_elements = {'terrain': 'all', 'climate': 'all'}
		self.depth = 25
		self.given_block_rect = pg.Rect(0, 20, 104, 64)

		self.update_mobj('map_elements', 'lists', 'v_rect')


class WallRock3(MapObject):
	def __init__(self):
		super().__init__()

		self.name = 'wall_rock3'
		self.type = 'wall'
		self.map_elements = {'terrain': 'all', 'climate': 'all'}
		self.depth = 25
		self.given_block_rect = pg.Rect(0, 20, 104, 64)

		self.update_mobj('map_elements', 'lists', 'v_rect')


class WallRock4(MapObject):
	def __init__(self):
		super().__init__()

		self.name = 'wall_rock4'
		self.type = 'wall'
		self.map_elements = {'terrain': 'all', 'climate': 'all'}
		self.depth = 25
		self.given_block_rect = pg.Rect(0, 20, 104, 64)

		self.update_mobj('map_elements', 'lists', 'v_rect')


class Mountain2(MapObject):
	def __init__(self):
		super().__init__()

		self.name = 'mountain2'
		self.type = 'deco'
		self.map_elements = {'terrain': [], 'climate': []}
		self.depth = 55
		self.given_block_rect = pg.Rect(6, 37, 54, 20)

		self.update_mobj('map_elements', 'lists', 'v_rect')


class Tree1(MapObject):
	def __init__(self):
		super().__init__()

		self.name = 'tree1'
		self.type = 'deco'
		self.map_elements = {'terrain': 'all', 'climate': ['arid', 'template', 'tropical']}
		self.depth = 118

		self.given_block_rect = pg.Rect(86, 100, 10, 20)

		self.update_mobj('map_elements', 'lists', 'v_rect')


class GrassyRock1(MapObject):
	def __init__(self):
		super().__init__()

		self.name = 'grassy_rock1'
		self.type = 'deco'
		self.map_elements = {'terrain': ['dirt', 'rock'], 'climate': ['template', 'tropical', 'tundra']}
		self.depth = 30

		self.given_block_rect = pg.Rect(40, 19, 84, 50)

		self.update_mobj('map_elements', 'lists', 'v_rect')


class GrassyRock2(MapObject):
	def __init__(self):
		super().__init__()

		self.name = 'grassy_rock2'
		self.type = 'deco'
		self.map_elements = {'terrain': ['dirt', 'rock'], 'climate': ['template', 'tropical', 'tundra']}
		self.depth = 30

		self.given_block_rect = pg.Rect(35, 25, 60, 70)

		self.update_mobj('map_elements', 'lists', 'v_rect')


class GrassyRock3(MapObject):
	def __init__(self):
		super().__init__()

		self.name = 'grassy_rock3'
		self.type = 'deco'
		self.map_elements = {'terrain': ['dirt', 'rock'], 'climate': ['template', 'tropical', 'tundra']}
		self.depth = 38

		self.given_block_rect = pg.Rect(34, 25, 60, 36)

		self.update_mobj('map_elements', 'lists', 'v_rect')


class GrassyRock4(MapObject):
	def __init__(self):
		super().__init__()

		self.name = 'grassy_rock4'
		self.type = 'deco'
		self.map_elements = {'terrain': ['dirt', 'rock'], 'climate': ['template', 'tropical', 'tundra']}

		self.update_mobj('map_elements', 'lists', 'v_rect')


class Chest(MapObject):
	def __init__(self):
		super().__init__()

		self.name = 'chest'
		self.type = 'container'
		self.map_elements = {'terrain': 'all', 'climate': 'all'}
		self.depth = 35

		self.given_block_rect = pg.Rect(4, 12, 36, 20)

		self.update_mobj('map_elements', 'lists', 'v_rect_sheet')
