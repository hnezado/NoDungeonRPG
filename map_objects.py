from confirm_win import *

generic_floors = []
generic_walls = []
generic_decos = []
generic_containers = []

# When adding new map_object:
# 1.Create subclass itself with the required variables (self.name, self.type...)
# 2.Add update_mobj() at the end of the new __init__() with the required update strings
# 3.Add the class to create_mobj('instance.name')
# 4.Create an instance if the subclass from 'map.py' and give it a nickname (Fdf = [DesertFloor()])

# Depth must be at least mov_speed higher than y pos to act like a "3d block"
mobj_imgs = {
		'null': pg.image.load('data/images/null64.png'),
		'blank_floor': pg.image.load('data/images/blank64.png').convert_alpha(),
		'town_floor': pg.image.load('data/images/map_objects/floors/town_floor.png').convert_alpha(),
		'prairie_floor': pg.image.load('data/images/map_objects/floors/prairie_floor.png').convert_alpha(),
		'desert_floor': pg.image.load('data/images/map_objects/floors/desert_floor.png').convert_alpha(),
		'grass_floor': pg.image.load('data/images/map_objects/floors/grass_floor.png').convert_alpha(),
		'snowy_floor': pg.image.load('data/images/map_objects/floors/snowy_floor.png').convert_alpha(),
		'icy_floor': pg.image.load('data/images/map_objects/floors/icy_floor.png').convert_alpha(),
		'rock_floor1': pg.image.load('data/images/map_objects/floors/tiled/rock_floor1.png').convert_alpha(),
		'sand_floor1': pg.image.load('data/images/map_objects/floors/tiled/sand_floor1.png').convert_alpha(),
		'sand_mound1': pg.image.load('data/images/map_objects/floors/tiled/sand_mound1.png').convert_alpha(),
		'wall_rock1': pg.image.load('data/images/map_objects/walls/wall_rock1.png').convert_alpha(),
		'wall_rock2': pg.image.load('data/images/map_objects/walls/wall_rock2.png').convert_alpha(),
		'wall_rock3': pg.image.load('data/images/map_objects/walls/wall_rock3.png').convert_alpha(),
		'wall_rock4': pg.image.load('data/images/map_objects/walls/wall_rock4.png').convert_alpha(),
		'house1': pg.image.load('data/images/map_objects/decorations/house1.png').convert_alpha(),
		'house2': pg.image.load('data/images/map_objects/decorations/house2.png').convert_alpha(),
		'house3': pg.image.load('data/images/map_objects/decorations/house3.png').convert_alpha(),
		'house4': pg.image.load('data/images/map_objects/decorations/house4.png').convert_alpha(),
		'house5': pg.image.load('data/images/map_objects/decorations/house5.png').convert_alpha(),
		'house6': pg.image.load('data/images/map_objects/decorations/house6.png').convert_alpha(),
		'tower': pg.image.load('data/images/map_objects/decorations/tower.png').convert_alpha(),
		'well': pg.image.load('data/images/map_objects/decorations/well.png').convert_alpha(),
		'mountain2': pg.image.load('data/images/map_objects/decorations/mountain2.png').convert_alpha(),
		'bush1': pg.image.load('data/images/map_objects/decorations/bush1.png').convert_alpha(),
		'bush2': pg.image.load('data/images/map_objects/decorations/bush2.png').convert_alpha(),
		'tree1': pg.image.load('data/images/map_objects/decorations/tree1.png').convert_alpha(),
		'tree2': pg.image.load('data/images/map_objects/decorations/tree2.png').convert_alpha(),
		'rock1': pg.image.load('data/images/map_objects/decorations/rock1.png').convert_alpha(),
		'grassy_rock1': pg.image.load('data/images/map_objects/decorations/grassy_rock1.png').convert_alpha(),
		'grassy_rock2': pg.image.load('data/images/map_objects/decorations/grassy_rock2.png').convert_alpha(),
		'grassy_rock3': pg.image.load('data/images/map_objects/decorations/grassy_rock3.png').convert_alpha(),
		'chest': Sheet('data/images/map_objects/containers/chest.png', dimensions=(2, 1))
}


def create_map_obj(name):
	"""Returns a new instance of the matching provided name"""

	if name == 'blank_floor': return BlankFloor()
	elif name == 'town_floor': return TownFloor()
	elif name == 'prairie_floor': return PrairieFloor()
	elif name == 'desert_floor': return DesertFloor()
	elif name == 'grass_floor': return GrassFloor()
	elif name == 'snowy_floor': return SnowyFloor()
	elif name == 'icy_floor': return SnowyFloor()
	elif name == 'rock_floor1': return RockFloor1()
	elif name == 'sand_floor1': return SandFloor1()
	elif name == 'sand_mound1': return SandMound1()
	elif name == 'wall_rock1': return WallRock1()
	elif name == 'wall_rock2': return WallRock2()
	elif name == 'wall_rock3': return WallRock3()
	elif name == 'wall_rock4': return WallRock4()
	elif name == 'house1': return House1()
	elif name == 'house2': return House2()
	elif name == 'house3': return House3()
	elif name == 'house4': return House4()
	elif name == 'house5': return House5()
	elif name == 'house6': return House6()
	elif name == 'tower': return Tower()
	elif name == 'well': return Well()
	elif name == 'mountain2': return Mountain2()
	elif name == 'bush1': return Bush1()
	elif name == 'bush2': return Bush2()
	elif name == 'tree1': return Tree1()
	elif name == 'tree2': return Tree2()
	elif name == 'rock1': return Rock1()
	elif name == 'grassy_rock1': return GrassyRock1()
	elif name == 'grassy_rock2': return GrassyRock2()
	elif name == 'grassy_rock3': return GrassyRock3()
	elif name == 'chest': return Chest()


class MapObject:
	def __init__(self):

		self.name = None
		self.type = None
		self.tiled = False
		self.map_elements = {'terrain': [], 'climate': []}
		self.pos = None
		self.rel_pos = ()
		self.visual_rect = None
		self.depth = 0
		self.spawnable = False

		self.given_block_rect = None
		self.block_rect = None
		self.opened = False
		self.loot_generated = False

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


### Floors ###
class BlankFloor(MapObject):
	def __init__(self):
		super().__init__()

		self.name = 'blank_floor'
		self.type = 'floor'
		self.spawnable = True

		self.update_mobj('map_elements', 'v_rect')


class TownFloor(MapObject):
	def __init__(self):
		super().__init__()

		self.name = 'town_floor'
		self.type = 'floor'
		self.spawnable = True

		self.update_mobj('map_elements', 'lists', 'v_rect')


class PrairieFloor(MapObject):
	def __init__(self):
		super().__init__()

		self.name = 'prairie_floor'
		self.type = 'floor'
		self.map_elements = {'terrain': ['dirt, rock'], 'climate': ['template, tropical']}
		self.spawnable = True

		self.update_mobj('map_elements', 'lists', 'v_rect')


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


class SnowyFloor(MapObject):
	def __init__(self):
		super().__init__()

		self.name = 'snowy_floor'
		self.type = 'floor'
		self.map_elements = {'terrain': ['dirt'], 'climate': ['tundra']}
		self.spawnable = True

		self.update_mobj('map_elements', 'lists', 'v_rect')


class IcyFloor(MapObject):
	def __init__(self):
		super().__init__()

		self.name = 'icy_floor'
		self.type = 'floor'
		self.map_elements = {'terrain': ['rock'], 'climate': ['tundra']}
		self.spawnable = True

		self.update_mobj('map_elements', 'lists', 'v_rect')


class RockFloor1(MapObject):
	def __init__(self):
		super().__init__()

		self.name = 'rock_floor1'
		self.type = 'floor'
		self.tiled = True
		self.map_elements = {'terrain': ['dirt', 'rock'], 'climate': ['template', 'tropical', 'tundra']}
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


### Walls ###
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


### Decorations ###
class House1(MapObject):
	def __init__(self):
		super().__init__()

		self.name = 'house1'
		self.type = 'deco'
		self.rel_pos = (24, 45)     # It wont center itself at it's base (rel_pos is the exact pos from 0,0 of the sel_tile)
		self.depth = 194            # given_block_rect.y + given_block_rect.h (full_obj -> no transparencies)
		self.given_block_rect = pg.Rect(64, 104, 200, 90)

		self.update_mobj('map_elements', 'lists', 'v_rect')


class House2(MapObject):
	def __init__(self):
		super().__init__()

		self.name = 'house2'
		self.type = 'deco'
		self.rel_pos = (47, 23)
		self.depth = 165
		self.given_block_rect = pg.Rect(48, 81, 188, 84)

		self.update_mobj('map_elements', 'lists', 'v_rect')


class House3(MapObject):
	def __init__(self):
		super().__init__()

		self.name = 'house3'
		self.type = 'deco'
		self.rel_pos = (33, 45)
		self.depth = 201
		self.given_block_rect = pg.Rect(81, 83, 231, 118)

		self.update_mobj('map_elements', 'lists', 'v_rect')


class House4(MapObject):
	def __init__(self):
		super().__init__()

		self.name = 'house4'
		self.type = 'deco'
		self.rel_pos = (-115, 51)
		self.depth = 266
		self.given_block_rect = pg.Rect(152, 165, 208, 101)

		self.update_mobj('map_elements', 'lists', 'v_rect')


class House5(MapObject):
	def __init__(self):
		super().__init__()

		self.name = 'house5'
		self.type = 'deco'
		self.rel_pos = (17, 51)
		self.depth = 312
		self.given_block_rect = pg.Rect(127, 194, 244, 118)

		self.update_mobj('map_elements', 'lists', 'v_rect')


class House6(MapObject):
	def __init__(self):
		super().__init__()

		self.name = 'house6'
		self.type = 'deco'
		self.rel_pos = (14, 47)
		self.depth = 199
		self.given_block_rect = pg.Rect(83, 129, 204, 70)

		self.update_mobj('map_elements', 'lists', 'v_rect')


class Tower(MapObject):
	def __init__(self):
		super().__init__()

		self.name = 'tower'
		self.type = 'deco'
		self.rel_pos = (48, 30)
		self.depth = 186
		self.given_block_rect = pg.Rect(143, 118, 90, 68)

		self.update_mobj('map_elements', 'lists', 'v_rect')


class Well(MapObject):
	def __init__(self):
		super().__init__()

		self.name = 'well'
		self.type = 'deco'
		self.rel_pos = (7, 37)
		self.depth = 129
		self.given_block_rect = pg.Rect(71, 87, 81, 42)

		self.update_mobj('map_elements', 'lists', 'v_rect')


class Mountain2(MapObject):
	def __init__(self):
		super().__init__()

		self.name = 'mountain2'
		self.type = 'deco'
		self.depth = 55
		self.given_block_rect = pg.Rect(6, 37, 54, 20)

		self.update_mobj('map_elements', 'lists', 'v_rect')


class Bush1(MapObject):
	def __init__(self):
		super().__init__()

		self.name = 'bush1'
		self.type = 'deco'
		self.map_elements = {'terrain': 'all', 'climate': 'all'}
		self.depth = 64

		self.update_mobj('map_elements', 'lists', 'v_rect')


class Bush2(MapObject):
	def __init__(self):
		super().__init__()

		self.name = 'bush2'
		self.type = 'deco'
		self.map_elements = {'terrain': 'all', 'climate': 'all'}
		self.depth = 124

		self.update_mobj('map_elements', 'lists', 'v_rect')


class Tree1(MapObject):
	def __init__(self):
		super().__init__()

		self.name = 'tree1'
		self.type = 'deco'
		self.map_elements = {'terrain': 'all', 'climate': ['arid', 'template', 'tropical']}
		self.depth = 116

		self.given_block_rect = pg.Rect(86, 100, 10, 20)

		self.update_mobj('map_elements', 'lists', 'v_rect')


class Tree2(MapObject):
	def __init__(self):
		super().__init__()

		self.name = 'tree2'
		self.type = 'deco'
		self.map_elements = {'terrain': ['dirt'], 'climate': ['template']}
		self.depth = 248

		self.given_block_rect = pg.Rect(59, 224, 10, 22)

		self.update_mobj('map_elements', 'lists', 'v_rect')


class Rock1(MapObject):
	def __init__(self):
		super().__init__()

		self.name = 'rock1'
		self.type = 'deco'
		self.map_elements = {'terrain': ['dirt', 'rock'], 'climate': 'all'}
		self.depth = 48

		self.given_block_rect = pg.Rect(25, 20, 75, 28)

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
		self.depth = 40

		self.given_block_rect = pg.Rect(26, 21, 64, 52)

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


class Chest(MapObject):
	def __init__(self):
		super().__init__()

		self.name = 'chest'
		self.type = 'container'
		self.map_elements = {'terrain': 'all', 'climate': 'all'}
		self.depth = 35

		self.given_block_rect = pg.Rect(4, 12, 36, 20)

		self.loot_items = generate_grid_status(dimensions=(3, 3))

		self.update_mobj('map_elements', 'lists', 'v_rect_sheet')
