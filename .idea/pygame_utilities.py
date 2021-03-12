import pygame as pg
import pickle as pkl


def savegame(data, filename):
	"""Saves the game status"""

	directory = 'saves/'+filename+'.dgn'
	with open(directory, 'wb') as f:
		pkl.dump(data, f)


def loadgame(filename):
	"""Loads and returns the saved data (saved game)"""

	directory = 'saves/'+filename+'.dgn'
	with open(directory, 'rb') as f:
		var = pkl.load(f)
	return var


def add_to(var_name, value, save_to):
	"""Adds the variable to the given dict (to save the game progress)"""

	save = save_to
	save[var_name] = value

	return save


def generate_grid_status(dimensions=(0, 0), default_value=None):
	"""Generates a dictionary with grid coordinates and values (e.g.: {'1x1': 0, '1x2': 0})"""

	dictionary = {}
	lst = []
	row = 0
	for rw in range(dimensions[0]):
		col = 0
		row += 1
		for cell in range(dimensions[1]):
			col += 1
			lst.clear()
			lst.append(str(row))
			lst.append('x')
			lst.append(str(col))
			string = ''.join(lst)
			dictionary[string] = default_value
	return dictionary


def generate_grid_rects(dimensions=(6, 6), pos=(0, 0), var_x=21, var_y=71, cell_size=(32, 32)):
	"""Generates the cell grid with its rect"""

	rects = {}
	row = 0
	list1 = []
	y = pos[1]+var_y
	for rw in range(dimensions[0]):
		col = 0
		x = pos[0]+var_x
		row += 1
		for cell in range(dimensions[1]):
			col += 1
			list1.clear()
			list1.append(str(row))
			list1.append('x')
			list1.append(str(col))
			string = ''.join(list1)
			rects[string] = pg.Rect(x, y, cell_size[0], cell_size[1])
			x += 40
		y += 40

	return rects


def check_cell_rect(event, button, rects, mouse_click_up=False):
	"""When click on a rect (as a provided dictionary value), returns the key"""

	pg.event.clear()
	if mouse_click_up:
		if event.type == pg.MOUSEBUTTONUP and event.button == button:
			for key, value in rects.items():
				if value.collidepoint(event.pos):
					return key
	else:
		if event.type == pg.MOUSEBUTTONDOWN and event.button == button:
			for key, value in rects.items():
				if value.collidepoint(event.pos):
					return key


def text(txt, font_style='Arial', font_size=10, color=(0, 0, 0), max_length=None, rendered=True):
	"""Separates and renders the provided text and returns a list of text surfaces (one element per line)
	The symbols '$' in the string are taken as line separators"""

	first_word = True
	lines = txt.split('$')
	rendered_lines = []
	lines_list = []

	if font_style == 'Arial': font = pg.font.SysFont(font_style, font_size)
	else: font = pg.font.Font(font_style, font_size)

	if max_length is None:
		for line in lines:
			rendered_lines.append(font.render(line, True, color))
		return rendered_lines

	else:
		str_main = ''
		for line in lines:
			words = line.split(' ')
			for word in words:
				if first_word:
					if len(word) <= max_length:
						str_main += word
						first_word = False
				else:
					if len(str_main+' '+word) <= max_length:
						str_main += ' '+word
					else:
						if rendered:
							rendered_lines.append(font.render(str_main, True, color))
						else:
							lines_list.append(str_main)
						str_main = word

		if rendered:
			rendered_lines.append(font.render(str_main, True, color))
			return rendered_lines
		else:
			lines_list.append(str_main)
			return lines_list


def blit_alpha(surface, img, pos, opacity, area=None):
	"""Displays the provided image on the position (x, y) with the given opacity. May take some extra ms"""

	pos_x = pos[0]
	pos_y = pos[1]
	surf = pg.Surface((img.get_width(), img.get_height())).convert()
	surf.blit(surface, (-pos_x, -pos_y))
	surf.blit(img, (0, 0))
	surf.set_alpha(opacity)
	if area is not None:
		surface.blit(surf, pos, area)
	else:
		surface.blit(surf, pos)


def readable_text(raw_text, separator, fist_capital=True):
	"""Converts the given text into something readable"""

	txt = ''
	words_list = raw_text.split(separator)
	if fist_capital: txt = words_list.pop(0).title()
	for word in words_list: txt += ' '+word

	return txt


def key_down(event, key=None):
	"""Detects if a keyboard key is pressed"""

	pg.event.clear()
	if event.type == pg.KEYDOWN:
		if key is not None:
			if event.key == key:
				return True
		else:
			return True


def key_up(event, key=None):
	"""Detects if a keyboard key is released"""

	pg.event.clear()
	if event.type == pg.KEYUP:
		if key is not None:
			if event.key == key:
				return True
		else:
			return True


def mouse_down(event, button, rect=None, multiple_rect=False):
	"""Detects if a mouse button is pressed. The area can be specified as a rect or multiples rects (list or dict)"""

	pg.event.clear()
	if event.type == pg.MOUSEBUTTONDOWN and event.button == button:
		if multiple_rect:
			if type(rect) == dict:
				for value in rect.values():
					if value.collidepoint(event.pos):
						return True
			elif type(rect) == list:
				for element in rect:
					if element.collidepoint(event.pos):
						return True
		else:
			if rect is not None:
				if pg.Rect(rect).collidepoint(event.pos):
					return True
			else:
				return True


def mouse_up(event, button, rect=None, multiple_rect=False):
	"""Detects if a mouse button is released. The area can be specified as a rect or multiples rects (list or dict)"""

	pg.event.clear()
	if event.type == pg.MOUSEBUTTONUP and event.button == button:
		if multiple_rect:
			if type(rect) == dict:
				for value in rect.values():
					if value.collidepoint(event.pos):
						return True
			elif type(rect) == list:
				for element in rect:
					if element.collidepoint(event.pos):
						return True
		else:
			if rect is not None:
				if pg.Rect(rect).collidepoint(event.pos):
					return True
			else:
				return True


def mouse_visible(show=True, surface=None, image=None, mouse_pos=None):
	if image is not None:
		pg.mouse.set_visible(False)
		cursor = pg.image.load(image).convert_alpha()
		surface.blit(cursor, mouse_pos)
	else:
		if show:
			pg.mouse.set_visible(True)
		else:
			pg.mouse.set_visible(False)


def clock(ticks):
	"""Setting the ticks on the pygame clock"""

	clk = pg.time.Clock()
	clk.tick(ticks)


class Damage:
	movement_pos_limit = 80
	counter_num = movement_pos_limit
	num_opacity = 255

	counter_portrait = movement_pos_limit*0.5
	portrait_opacity = 255

	@staticmethod
	def draw_damage(dmg, pos1, surface, font, color, img=None, pos2=None):
		"""Displays the given damage animation in the given starting pos"""

		damage = text(txt=dmg, font_style=font, font_size=25, color=color)[0]
		pos_num = damage.get_rect(center=pos1)
		pos_num[1] += Damage.counter_num-Damage.movement_pos_limit

		if img is not None: Damage.portrait_opacity -= 10
		if Damage.counter_num < Damage.movement_pos_limit*0.5:
			Damage.num_opacity -= 10

		if img is not None: blit_alpha(surface, img, pos2, Damage.portrait_opacity)
		blit_alpha(surface, damage, pos_num, Damage.num_opacity)

		if Damage.counter_portrait > 0:
			Damage.counter_portrait -= 2
		if Damage.counter_num > 0:
			Damage.counter_num -= 2

		# Resetting values #
		elif Damage.counter_num <= 0:

			Damage.counter_num = Damage.movement_pos_limit
			Damage.num_opacity = 255

			Damage.counter_portrait = Damage.movement_pos_limit*0.5
			Damage.portrait_opacity = 255

			return 'end_anim'


class BlinkingText:
	opacity = 255
	adding = False

	@staticmethod
	def show_blinking_text(surface, txt, pos, font, size, color, variance, centered=True):
		"""Displays fading out and in text or surface in a loop"""

		surf = text(txt, font, size, color)[0]
		centered_pos = surf.get_rect(center=pos)

		if not BlinkingText.adding:
			if 0 < BlinkingText.opacity < 255*0.5:
				BlinkingText.opacity -= variance*3
			elif 255*0.5 < BlinkingText.opacity:
				BlinkingText.opacity -= variance
			elif BlinkingText.opacity <= 0:
				BlinkingText.adding = True
		elif BlinkingText.adding:
			if BlinkingText.opacity < 255*0.5:
				BlinkingText.opacity += variance*3
			elif 255*0.5 < BlinkingText.opacity < 255:
				BlinkingText.opacity += variance
			elif BlinkingText.opacity >= 255:
				BlinkingText.adding = False

		if centered:
			blit_alpha(surface, surf, centered_pos, BlinkingText.opacity)
		else:
			blit_alpha(surface, surf, pos, BlinkingText.opacity)


class MouseHover:
	def __init__(self):
		self.time = pg.time.get_ticks()

	def reset_time(self):
		"""Resets the time variable"""

		self.time = pg.time.get_ticks()

	def mouse_hover(self, mouse_pos, rect, ms=None, return_rect=False):
		"""Detects collision between rect and mouse position. If ms provided, delays the return
		If dict is provided and return_rect=True, returns the matching key"""

		if type(rect) == list:
			for rct in rect:
				if rct.collidepoint(mouse_pos):
					if ms is not None:
						if pg.time.get_ticks() > self.time:
							if return_rect:
								return rct
							else:
								return True
					else:
						if return_rect:
							return rct
						else:
							return True
		elif type(rect) == dict:
			for key, rct in rect.items():
				if rct.collidepoint(mouse_pos):
					if ms is not None:
						if pg.time.get_ticks() > self.time:
							if return_rect:
								return key
							else:
								return True
					else:
						if return_rect:
							return key
						else:
							return True
		else:
			if rect.collidepoint(mouse_pos):
				if ms is not None:
					if pg.time.get_ticks() > self.time:
						if return_rect:
							return rect
						else:
							return True
				else:
					if return_rect:
						return rect
					else:
						return True


class Sheet:
	"""Creates a list of cropped images (x, y, width, height) of the given sheet"""

	def __init__(self, sheet, dimensions, transparency=True):
		self.sheet = pg.image.load(sheet).convert_alpha() if transparency else pg.image.load(sheet).convert()

		self.rows, self.columns = dimensions[0], dimensions[1]
		self.total_crops = self.rows*self.columns

		self.rect = self.sheet.get_rect()
		self.crop_w = self.rect.width/self.columns
		self.crop_h = self.rect.height/self.rows

		# List with the positions and sizes (surface objects) of all the cells of the sprite #
		self.crops = list([(int(cell % self.columns)*self.crop_w, int(cell/self.columns)*self.crop_h,
		                    self.crop_w, self.crop_h) for cell in range(self.total_crops)])


class Button:
	"""Works with Sheet class (requires sheets as surfaces) except img
	icon_*_custom takes a value if a different crop from the sheet are going to be used
	otherwise the same crop given in icon will move down slightly by default"""

	def __init__(self, surface, bg=None, icon=None, icon_pressed_custom=False, icon_active_custom=False,
	             img=None, img_hover=None, img_pressed=None, img_active=None,
	             sheet_index=0, pos=None, hover_on=False, press_on=True, activate_on=False,
	             displace_pressed=(0, 4), displace_active=(0, 2)):

		self.surface = surface
		self.pos = pos
		self.pos_pressed = None
		self.pos_active = None

		self.displace_pressed, self.displace_active = displace_pressed, displace_active
		self.hover_on, self.press_on, self.activate_on = hover_on, press_on, activate_on

		self.bg = bg
		self.icon = icon
		self.icon_pressed_custom = icon_pressed_custom
		self.icon_active_custom = icon_active_custom
		self.img = img
		self.img_hover = img_hover
		self.img_pressed = img_pressed
		self.img_active = img_active

		if bg is not None:
			self.rect = pg.Rect(self.pos[0], self.pos[1], self.bg.crop_w, self.bg.crop_h)
		elif icon is not None:
			self.rect = pg.Rect(self.pos[0], self.pos[1], self.icon.crop_w, self.icon.crop_h)
		elif img is not None:
			self.rect = pg.Rect(self.pos[0], self.pos[1], self.img.get_width(), self.img.get_height())

		# if there is any pressed and/or active: the order in the sheet must be: index=img index+1=img_pressed 3=img_active
		self.sheet_index = sheet_index

		self.hovering = False
		self.pressed = False
		self.active = False

	def draw_button(self):
		"""Displays the button on its state"""

		self.pos_pressed = (self.pos[0]+self.displace_pressed[0], self.pos[1]+self.displace_pressed[1])
		self.pos_active = (self.pos[0]+self.displace_active[0], self.pos[1]+self.displace_active[1])

		if self.bg is not None:
			if self.pressed and self.press_on:
				self.surface.blit(self.bg.sheet, self.pos, self.bg.crops[1])
			elif self.active and self.activate_on:
				self.surface.blit(self.bg.sheet, self.pos, self.bg.crops[2])
			else:
				self.surface.blit(self.bg.sheet, self.pos, self.bg.crops[0])

		if self.icon is not None:
			if self.pressed and self.press_on:
				if self.icon_pressed_custom:
					self.surface.blit(self.icon.sheet, self.pos_pressed, self.icon.crops[self.sheet_index+1])
				else:
					self.surface.blit(self.icon.sheet, self.pos_pressed, self.icon.crops[self.sheet_index])
			elif self.active and self.activate_on:
				if self.icon_active_custom:
					self.surface.blit(self.icon.sheet, self.pos_active, self.icon.crops[self.sheet_index+2])
				else:
					self.surface.blit(self.icon.sheet, self.pos_active, self.icon.crops[self.sheet_index])
			else:
				self.surface.blit(self.icon.sheet, self.pos, self.icon.crops[self.sheet_index])

		if self.img is not None:
			if self.active and self.activate_on:
				self.surface.blit(self.img_active, self.pos)
			elif self.pressed and self.press_on:
				self.surface.blit(self.img_pressed, self.pos)
			elif self.hovering and self.hover_on:
				self.surface.blit(self.img_hover, self.pos)
			else:
				self.surface.blit(self.img, self.pos)
