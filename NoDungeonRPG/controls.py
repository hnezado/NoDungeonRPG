import pygame

from main_menu import *


def controls_confirm_win(event):
	"""Defines the confirmation window interaction"""

	if IOConfirmWindow.type == 'main_menu':
		if mouse_down(event, 1, IOConfirmWindow.buttons['accept'].rect):
			IOConfirmWindow.buttons['accept'].pressed = True
		if mouse_up(event, 1, IOConfirmWindow.buttons['accept'].rect):
			IOConfirmWindow.buttons['accept'].pressed = False
			IOGUI.menu_active = False
			sett.active_screen = 'main_menu'
			IOConfirmWindow.active_win = False

		elif mouse_down(event, 1, IOConfirmWindow.buttons['cancel'].rect):
			IOConfirmWindow.buttons['cancel'].pressed = True
		if mouse_up(event, 1, IOConfirmWindow.buttons['cancel'].rect):
			IOConfirmWindow.buttons['cancel'].pressed = False
			IOConfirmWindow.active_win = False

		if key_down(event, pg.K_RETURN):
			IOGUI.menu_active = False
			sett.active_screen = 'main_menu'
			IOConfirmWindow.active_win = False

	elif IOConfirmWindow.type == 'quit':
		if mouse_down(event, 1, IOConfirmWindow.buttons['accept'].rect):
			IOConfirmWindow.buttons['accept'].pressed = True
		if mouse_up(event, 1, IOConfirmWindow.buttons['accept'].rect):
			IOConfirmWindow.buttons['accept'].pressed = False
			pg.quit()
			quit()

		elif mouse_down(event, 1, IOConfirmWindow.buttons['cancel'].rect):
			IOConfirmWindow.buttons['cancel'].pressed = True
		if mouse_up(event, 1, IOConfirmWindow.buttons['cancel'].rect):
			IOConfirmWindow.buttons['cancel'].pressed = False
			IOConfirmWindow.active_win = False

		if key_down(event, pg.K_RETURN):
			IOConfirmWindow.active_win = False
			pg.quit()
			quit()

	if key_down(event, pg.K_ESCAPE):
		IOConfirmWindow.active_win = False

	if mouse_up(event, 1):
		for button in IOConfirmWindow.buttons.keys():
			IOConfirmWindow.buttons[button].pressed = False


def controls_main_menu(event, main_menu):
	"""Defines the main menu interaction"""

	if sett.active_screen == 'main_menu':
		if mouse_down(event, 1, main_menu.buttons['continue'].rect):
			main_menu.buttons['continue'].pressed = True
		if main_menu.buttons['continue'].pressed:
			if mouse_up(event, 1, main_menu.buttons['continue'].rect):
				# sett.active_screen = 'game'
				IOGUI.menu_layer = 'load'
				IOGUI.menu_active = True

		if mouse_down(event, 1, main_menu.buttons['new_game'].rect):
			main_menu.buttons['new_game'].pressed = True
		if main_menu.buttons['new_game'].pressed:
			if mouse_up(event, 1, main_menu.buttons['new_game'].rect):
				main_menu.new_game()
				sett.active_screen = 'game'

		if mouse_down(event, 1, main_menu.buttons['settings'].rect):
			main_menu.buttons['settings'].pressed = True
		if main_menu.buttons['settings'].pressed:
			if mouse_up(event, 1, main_menu.buttons['settings'].rect):
				IOGUI.menu_layer = 'settings'
				IOGUI.menu_active = True

		if mouse_down(event, 1, main_menu.buttons['quit'].rect):
			main_menu.buttons['quit'].pressed = True
		if main_menu.buttons['quit'].pressed:
			if mouse_up(event, 1, main_menu.buttons['quit'].rect):
				IOConfirmWindow.set_msg('quit')
				IOConfirmWindow.active_win = True

		# Menu buttons interaction #
		if IOGUI.menu_active:

			if IOGUI.menu_layer == 'load':
				for socket in IOGUI.menu_but['save_game_buttons'].keys():
					if mouse_down(event, 1, IOGUI.menu_but['load_game_buttons'][socket]):
						IOGUI.menu_but['load_game_buttons'][socket].pressed = True
					if IOGUI.menu_but['load_game_buttons'][socket].pressed:
						if mouse_up(event, 1, IOGUI.menu_but['load_game_buttons'][socket]):
							if sett.save_sockets[socket] is not None:
								IOGUI.menu_layer = 'main'
								IOGUI.menu_active = False
								IOGUI.menu('load_game', socket)
								IOItem.refresh_surfaces()
								# sett.active_screen = 'game'

			if IOGUI.menu_layer == 'settings':
				pass

			if IOMouseHover.mouse_hover(sett.mouse_pos, IOGUI.menu_but['back'].rect):
				IOGUI.menu_but['back'].hovering = True
			else: IOGUI.menu_but['back'].hovering = False
			if mouse_down(event, 1, IOGUI.menu_but['back']): IOGUI.menu_but['back'].pressed = True
			if IOGUI.menu_but['back'].pressed:
				if mouse_up(event, 1, IOGUI.menu_but['back']):
					IOGUI.menu_layer = 'main'
					IOGUI.menu_active = False

		if mouse_up(event, 1):
			for button in main_menu.buttons.keys():
				main_menu.buttons[button].pressed = False
			for button in IOGUI.menu_but.keys():
				if type(IOGUI.menu_but[button]) != dict:
					IOGUI.menu_but[button].pressed = False


def controls_char(event):
	"""Defines the character movement controls"""

	if sett.active_screen == 'game':
		if key_down(event, pg.K_UP) or key_down(event, pg.K_w):
			sett.current_game['current_char'].move_up = True
		elif key_down(event, pg.K_DOWN) or key_down(event, pg.K_s):
			sett.current_game['current_char'].move_down = True
		elif key_down(event, pg.K_LEFT) or key_down(event, pg.K_a):
			sett.current_game['current_char'].move_left = True
		elif key_down(event, pg.K_RIGHT) or key_down(event, pg.K_d):
			sett.current_game['current_char'].move_right = True

	if IOAtlas.fading['transition'] != 'in':
		if key_up(event, pg.K_UP) or key_up(event, pg.K_w):
			sett.current_game['current_char'].move_up = False
		elif key_up(event, pg.K_DOWN) or key_up(event, pg.K_s):
			sett.current_game['current_char'].move_down = False
		elif key_up(event, pg.K_LEFT) or key_up(event, pg.K_a):
			sett.current_game['current_char'].move_left = False
		elif key_up(event, pg.K_RIGHT) or key_up(event, pg.K_d):
			sett.current_game['current_char'].move_right = False


def controls_map_interaction(event):
	"""Defines the interactions between the map and the character"""

	if sett.active_screen == 'game':
		if sett.current_game['current_container'] is not None:
			if key_down(event, pg.K_SPACE):
				sett.current_game['previous_container'] = sett.current_game['current_container']
				sett.current_game['current_container'].opened = True
				if IOLootContainer.active_window:
					IOLootContainer.pos = [sett.mouse_pos[0]-IOLootContainer.pos_rel[0], sett.mouse_pos[1]-IOLootContainer.pos_rel[1]]
					IOLootContainer.set_limits()
					IOLootContainer.update_window()
					IOLootContainer.focus_window()
				else:
					loot()

		if IOCombat.combat_ready:
			if key_down(event, pg.K_SPACE):
				IOCombat.start_combat()


# GUI controls #
def controls_equ(event):
	"""Defines the interaction with the equipment window"""

	if sett.active_screen == 'game':
		if IOEqu.active_window:

			# GUI button #
			if mouse_down(event, 1, IOEqu.gui_button.rect):
				IOEqu.gui_button.pressed = True
			if IOEqu.gui_button.pressed:
				if mouse_up(event, 1, IOEqu.gui_button.rect):
					IOEqu.close_win = True

			if key_down(event, pg.K_e):
				IOEqu.close_win = True

			if IOEqu.focused_window:

				# Close button #
				if mouse_down(event, 1, IOEqu.close_rect):
					IOEqu.close_pressed = True
				if IOEqu.close_pressed:
					if mouse_up(event, 1, IOEqu.close_rect):
						IOEqu.close_win = True

				# Window movement #
				if mouse_down(event, 1, IOEqu.move_win_rect):
					IOEqu.move_win_pressed = True
					IOEqu.mouse_pos_rel = (sett.mouse_pos[0]-IOEqu.pos[0], sett.mouse_pos[1]-IOEqu.pos[1])
				if IOEqu.move_win_pressed:
					IOEqu.move_window(IOEqu.mouse_pos_rel)

				if key_down(event, pg.K_ESCAPE):
					IOEqu.close_win = True

		elif not IOEqu.active_window:

			# GUI button #
			if mouse_down(event, 1, IOEqu.gui_button.rect):
				IOEqu.gui_button.pressed = True
			if IOEqu.gui_button.pressed:
				if mouse_up(event, 1, IOEqu.gui_button.rect):
					IOEqu.open_window()

			if key_down(event, pg.K_e):
				IOEqu.open_window()


def controls_inv(event):
	"""Defines the interaction with the inventory window"""

	if sett.active_screen == 'game':
		if IOInv.active_window:

			# GUI button #
			if mouse_down(event, 1, IOInv.gui_button.rect):
				IOInv.gui_button.pressed = True
			if IOInv.gui_button.pressed:
				if mouse_up(event, 1, IOInv.gui_button.rect):
					IOInv.close_win = True

			if key_down(event, pg.K_i):
				IOInv.close_win = True

			if IOInv.focused_window:
				# Close button #
				if mouse_down(event, 1, IOInv.close_rect):
					IOInv.close_pressed = True
				if IOInv.close_pressed:
					if mouse_up(event, 1, IOInv.close_rect):
						IOInv.close_win = True

				# Window movement #
				if mouse_down(event, 1, IOInv.move_win_rect):
					IOInv.move_win_pressed = True
					IOInv.mouse_pos_rel = (sett.mouse_pos[0]-IOInv.pos[0], sett.mouse_pos[1]-IOInv.pos[1])
				if IOInv.move_win_pressed:
					IOInv.move_window(IOInv.mouse_pos_rel)

				if key_down(event, pg.K_ESCAPE):
					IOInv.close_win = True

		elif not IOInv.active_window:

			# GUI button #
			if mouse_down(event, 1, IOInv.gui_button.rect):
				IOInv.gui_button.pressed = True
			if IOInv.gui_button.pressed:
				if mouse_up(event, 1, IOInv.gui_button.rect):
					IOInv.open_window()

			if key_down(event, pg.K_i):
				IOInv.open_window()


def controls_loot(event):
	"""Defines the interaction with the loot window"""

	if sett.active_screen == 'game':
		# Combat container #
		if IOLootCombat.active_window:
			if IOLootCombat.focused_window:
				# Close button #
				if mouse_down(event, 1, IOLootCombat.close_rect):
					IOLootCombat.close_pressed = True
				if IOLootCombat.close_pressed:
					if mouse_up(event, 1, IOLootCombat.close_rect):
						IOLootCombat.close_win = True
						if sett.current_game['previous_container'] is not None:
							sett.current_game['previous_container'].opened = False

				# Window movement #
				if mouse_down(event, 1, IOLootCombat.move_win_rect):
					IOLootCombat.move_win_pressed = True
					IOLootCombat.mouse_pos_rel = (sett.mouse_pos[0]-IOLootCombat.pos[0], sett.mouse_pos[1]-IOLootCombat.pos[1])
				if IOLootCombat.move_win_pressed:
					IOLootCombat.move_window(IOLootCombat.mouse_pos_rel)

				if key_down(event, pg.K_ESCAPE):
					IOLootCombat.close_win = True

		# Loot container #
		if IOLootContainer.active_window:

			if IOLootContainer.focused_window:
				# Close button #
				if mouse_down(event, 1, IOLootContainer.close_rect):
					IOLootContainer.close_pressed = True
				if IOLootContainer.close_pressed:
					if mouse_up(event, 1, IOLootContainer.close_rect):
						IOLootContainer.close_win = True
						if sett.current_game['previous_container'] is not None:
							sett.current_game['previous_container'].opened = False

				# Window movement #
				if mouse_down(event, 1, IOLootContainer.move_win_rect):
					IOLootContainer.move_win_pressed = True
					IOLootContainer.mouse_pos_rel = \
						(sett.mouse_pos[0]-IOLootContainer.pos[0], sett.mouse_pos[1]-IOLootContainer.pos[1])
				if IOLootContainer.move_win_pressed:
					IOLootContainer.move_window(IOLootContainer.mouse_pos_rel)

				if key_down(event, pg.K_ESCAPE):
					IOLootContainer.close_win = True
					if sett.current_game['previous_container'] is not None:
						sett.current_game['previous_container'].opened = False


def controls_gui(event):
	"""Defines the GUI interactions"""

	if sett.active_screen == 'game':
		if not IOGUI.menu_active and not IOCombat.combat_active:

			# Focus window #
			for window in opened_windows:
				if mouse_down(event, 1, window.rect):
					window.focus_window()
					break
				elif mouse_down(event, 3, window.rect):
					window.focus_window()
					break

			controls_equ(event)
			controls_inv(event)
			controls_loot(event)

		if mouse_down(event, 1, IOGUI.ingame_menu_button.rect):
			IOGUI.ingame_menu_button.pressed = True

		if IOGUI.ingame_menu_button.pressed:
			if mouse_up(event, 1, IOGUI.ingame_menu_button.rect):
				if not IOGUI.menu_active:
					IOGUI.menu('open')
				elif IOGUI.menu_active:
					IOGUI.menu('close')

		if key_down(event, pg.K_ESCAPE):
			if not IOGUI.menu_active:
				if len(opened_windows) == 0:
					IOGUI.menu('open')
			elif IOGUI.menu_active:
				IOGUI.menu('close')


def controls_ingame_menu(event):
	"""Defines the ingame menu interactions"""

	if sett.active_screen == 'game':
		if IOGUI.menu_active:

			# Main layer #
			if IOGUI.menu_layer == 'main':
				if IOMouseHover.mouse_hover(sett.mouse_pos, IOGUI.menu_but['resume'].rect):
					IOGUI.menu_but['resume'].hovering = True
				else: IOGUI.menu_but['resume'].hovering = False
				if IOMouseHover.mouse_hover(sett.mouse_pos, IOGUI.menu_but['save'].rect):
					IOGUI.menu_but['save'].hovering = True
				else: IOGUI.menu_but['save'].hovering = False
				if IOMouseHover.mouse_hover(sett.mouse_pos, IOGUI.menu_but['load'].rect):
					IOGUI.menu_but['load'].hovering = True
				else: IOGUI.menu_but['load'].hovering = False
				if IOMouseHover.mouse_hover(sett.mouse_pos, IOGUI.menu_but['settings'].rect):
					IOGUI.menu_but['settings'].hovering = True
				else: IOGUI.menu_but['settings'].hovering = False
				if IOMouseHover.mouse_hover(sett.mouse_pos, IOGUI.menu_but['main_menu'].rect):
					IOGUI.menu_but['main_menu'].hovering = True
				else: IOGUI.menu_but['main_menu'].hovering = False

				if mouse_down(event, 1, IOGUI.menu_but['resume']): IOGUI.menu_but['resume'].pressed = True
				if IOGUI.menu_but['resume'].pressed:
					if mouse_up(event, 1, IOGUI.menu_but['resume']):
						IOGUI.menu('close')
				if mouse_down(event, 1, IOGUI.menu_but['save']): IOGUI.menu_but['save'].pressed = True
				if IOGUI.menu_but['save'].pressed:
					if mouse_up(event, 1, IOGUI.menu_but['save']):
						IOGUI.menu('save')
				if mouse_down(event, 1, IOGUI.menu_but['load']): IOGUI.menu_but['load'].pressed = True
				if IOGUI.menu_but['load'].pressed:
					if mouse_up(event, 1, IOGUI.menu_but['load']):
						IOGUI.menu('load')
				if mouse_down(event, 1, IOGUI.menu_but['settings']): IOGUI.menu_but['settings'].pressed = True
				if IOGUI.menu_but['settings'].pressed:
					if mouse_up(event, 1, IOGUI.menu_but['settings']):
						IOGUI.menu('settings')
				if mouse_down(event, 1, IOGUI.menu_but['main_menu']): IOGUI.menu_but['main_menu'].pressed = True
				if IOGUI.menu_but['main_menu'].pressed:
					if mouse_up(event, 1, IOGUI.menu_but['main_menu']):
						IOConfirmWindow.set_msg('main_menu')
						IOConfirmWindow.active_win = True
						# IOGUI.menu('main_menu')

			# Save layer #
			elif IOGUI.menu_layer == 'save':
				for socket in IOGUI.menu_but['save_game_buttons'].keys():
					if mouse_down(event, 1, IOGUI.menu_but['save_game_buttons'][socket]):
						IOGUI.menu_but['save_game_buttons'][socket].pressed = True
					if IOGUI.menu_but['save_game_buttons'][socket].pressed:
						if mouse_up(event, 1, IOGUI.menu_but['save_game_buttons'][socket]):
							IOGUI.menu('save_game', socket)
							IOGUI.menu('close')

				if IOMouseHover.mouse_hover(sett.mouse_pos, IOGUI.menu_but['back'].rect):
					IOGUI.menu_but['back'].hovering = True
				else: IOGUI.menu_but['back'].hovering = False
				if mouse_down(event, 1, IOGUI.menu_but['back']): IOGUI.menu_but['back'].pressed = True
				if IOGUI.menu_but['back'].pressed:
					if mouse_up(event, 1, IOGUI.menu_but['back']):
						IOGUI.menu('main')

				for delete_but in IOGUI.menu_but['delete_game'].keys():
					if IOMouseHover.mouse_hover(sett.mouse_pos, IOGUI.menu_but['delete_game'][delete_but].rect):
						IOGUI.menu_but['delete_game'][delete_but].hovering = True
					else: IOGUI.menu_but['delete_game'][delete_but].hovering = False
					if sett.save_sockets[delete_but] is not None:
						if mouse_down(event, 1, IOGUI.menu_but['delete_game'][delete_but]):
							IOGUI.menu_but['delete_game'][delete_but].pressed = True
						if IOGUI.menu_but['delete_game'][delete_but].pressed:
							if mouse_up(event, 1, IOGUI.menu_but['delete_game'][delete_but]):
								sett.save_sockets[delete_but] = None
								os.remove('saves/'+delete_but+'.dgn')
								IOGUI.message(f'Deleting game: {delete_but}.dgn')

			# Load layer #
			elif IOGUI.menu_layer == 'load':
				for socket in IOGUI.menu_but['save_game_buttons'].keys():
					if mouse_down(event, 1, IOGUI.menu_but['load_game_buttons'][socket]):
						IOGUI.menu_but['load_game_buttons'][socket].pressed = True
					if IOGUI.menu_but['load_game_buttons'][socket].pressed:
						if mouse_up(event, 1, IOGUI.menu_but['load_game_buttons'][socket]):
							if sett.save_sockets[socket] is not None:
								IOGUI.menu('load_game', socket)
								IOItem.refresh_surfaces()
								IOGUI.menu('close')

				if IOMouseHover.mouse_hover(sett.mouse_pos, IOGUI.menu_but['back'].rect):
					IOGUI.menu_but['back'].hovering = True
				else: IOGUI.menu_but['back'].hovering = False
				if mouse_down(event, 1, IOGUI.menu_but['back']): IOGUI.menu_but['back'].pressed = True
				if IOGUI.menu_but['back'].pressed:
					if mouse_up(event, 1, IOGUI.menu_but['back']):
						IOGUI.menu('main')

			# Settings layer #
			elif IOGUI.menu_layer == 'settings':
				if sett.current_game['settings']['sound_active']:
					if IOMouseHover.mouse_hover(sett.mouse_pos, IOGUI.menu_but['sound_on'].rect):
						IOGUI.menu_but['sound_on'].hovering = True
					else: IOGUI.menu_but['sound_on'].hovering = False

					if mouse_down(event, 1, IOGUI.menu_but['sound_on']): IOGUI.menu_but['sound_on'].pressed = True
					if IOGUI.menu_but['sound_on'].pressed:
						if mouse_up(event, 1, IOGUI.menu_but['sound_on']):
							IOGUI.menu('sound_off')

				else:
					if IOMouseHover.mouse_hover(sett.mouse_pos, IOGUI.menu_but['sound_off'].rect):
						IOGUI.menu_but['sound_off'].hovering = True
					else: IOGUI.menu_but['sound_off'].hovering = False

					if mouse_down(event, 1, IOGUI.menu_but['sound_off']): IOGUI.menu_but['sound_off'].pressed = True
					if IOGUI.menu_but['sound_off'].pressed:
						if mouse_up(event, 1, IOGUI.menu_but['sound_off']):
							IOGUI.menu('sound_on')

				if IOMouseHover.mouse_hover(sett.mouse_pos, IOGUI.menu_but['back'].rect):
					IOGUI.menu_but['back'].hovering = True
				else: IOGUI.menu_but['back'].hovering = False
				if mouse_down(event, 1, IOGUI.menu_but['back']): IOGUI.menu_but['back'].pressed = True
				if IOGUI.menu_but['back'].pressed:
					if mouse_up(event, 1, IOGUI.menu_but['back']):
						IOGUI.menu('main')


def controls_meditation(event):
	"""Defines the meditation rect interaction"""

	if sett.active_screen == 'game':
			# Spirit bar #
			if sett.current_game['current_char'].meditation_ready:
				if mouse_down(event, 1, IOGUI.stat_rects['meditation']):
					if IOCombat.combat_active:
						IOGUI.message(f"I can't meditate right now. it's not safe!", type='thought')
					else:
						IOGUI.message('I can feel very relaxed now...', type='thought')
						meditation = sett.current_game['current_char'].meditation()
						if meditation is not None:
							[IOGUI.message(f'{stat.title()} has been upgraded!') for stat in meditation]


# Item movement controls #
def equ_item_mov(event):
	"""Defines the item movement in the equipment window"""

	if IOEqu.focused_window:
		if mouse_down(event, 1, IOEqu.equ_rects, multiple_rect=True):
			IOItem.cell_pressed = check_cell_rect(event, 1, IOEqu.equ_rects)
			cell_status = sett.current_game['equipped'][IOItem.cell_pressed]
			if IOGUI.item_on_cursor is None:
				if cell_status is not None:
					IOItem.item_drag = True
					sett.current_game['equipped'][IOItem.cell_pressed].unequip(to='cursor')
			else:
				if IOGUI.item_on_cursor.itype == IOItem.cell_pressed:
					if cell_status is None:
						IOGUI.item_on_cursor.equip(frm='cursor')
					else:
						cell_status.swap_items()

	if IOItem.item_drag:
		if mouse_up(event, 1, IOEqu.equ_rects, multiple_rect=True):
			if not IOInv.rect.collidepoint(sett.mouse_pos):
				IOItem.cell_released = check_cell_rect(event, 1, IOEqu.equ_rects, mouse_click_up=True)
				cell_status = sett.current_game['equipped'][IOItem.cell_released]
				if cell_status is None:
					if IOItem.cell_pressed != IOItem.cell_released:
						if IOGUI.item_on_cursor.itype == IOItem.cell_released:
							IOGUI.item_on_cursor.equip(frm='cursor')
				else:
					if IOGUI.item_on_cursor.itype == IOItem.cell_released:
						cell_status.swap_items()


def inv_item_mov(event):
	"""Defines the item movement on the inventory window"""

	if IOInv.focused_window:
		if mouse_down(event, 1, IOInv.inv_rects, multiple_rect=True):
			IOItem.cell_pressed = check_cell_rect(event, 1, IOInv.inv_rects)
			cell_status = sett.current_game['inv_items'][IOItem.cell_pressed]
			if IOGUI.item_on_cursor is None:
				if cell_status is not None and cell_status != 'locked':
					if not cell_status.item_locked:
						IOItem.item_drag = True
						IOGUI.item_on_cursor = cell_status
						sett.current_game['inv_items'][IOItem.cell_pressed] = None
			else:
				if cell_status is None:
					sett.current_game['inv_items'][IOItem.cell_pressed] = IOGUI.item_on_cursor
					IOGUI.item_on_cursor = None
				elif cell_status is not None and cell_status != 'locked':
					if not cell_status.item_locked:
						cell_status.swap_items()

	if IOItem.item_drag:
		if mouse_up(event, 1, IOInv.inv_rects, multiple_rect=True):
			if not IOEqu.rect.collidepoint(sett.mouse_pos):
				IOItem.cell_released = check_cell_rect(event, 1, IOInv.inv_rects, mouse_click_up=True)
				cell_status = sett.current_game['inv_items'][IOItem.cell_released]
				if cell_status is None:
					if IOItem.cell_pressed != IOItem.cell_released:
						sett.current_game['inv_items'][IOItem.cell_released] = IOGUI.item_on_cursor
						IOGUI.item_on_cursor = None
				elif cell_status is not None and cell_status != 'locked':
					if not cell_status.item_locked:
						cell_status.swap_items()


def quick_equ(event):
	"""Enables the quick equip/unequip/swap item control (right click on item) """

	# Quick unequip (click on equipment) #
	if IOEqu.focused_window:
		if mouse_down(event, 3, IOEqu.equ_rects, multiple_rect=True):
			IOItem.cell_pressed = check_cell_rect(event, 3, IOEqu.equ_rects)
			if sett.current_game['equipped'][IOItem.cell_pressed] is not None:
				if not IOInv.full_inv:
					sett.current_game['equipped'][IOItem.cell_pressed].unequip('inv')
				else:
					IOGUI.message('The inventory is full!')

	# Quick equip (click on inventory) #
	if IOInv.focused_window:
		if mouse_down(event, 3, IOInv.inv_rects, multiple_rect=True):
			IOItem.cell_pressed = check_cell_rect(event, 3, IOInv.inv_rects)
			cell_status = sett.current_game['inv_items'][IOItem.cell_pressed]
			if cell_status is not None and cell_status != 'locked':
				if not cell_status.item_locked:
					# Quick equip item #
					if sett.current_game['equipped'][cell_status.itype] is None:
						cell_status.equip('inv')
					# Quick swap item #
					else:
						cell_status.swap_items(type='quick_eq')


def loot_item_mov(event):
	"""Defines the item movement on the loot window"""

	if IOLootCombat.active_window:
		if IOLootCombat.focused_window:
			if mouse_down(event, 1, IOLootCombat.loot_rects, multiple_rect=True):
				IOItem.cell_pressed = check_cell_rect(event, 1, IOLootCombat.loot_rects)
				cell_status = IOLootCombat.loot_buffer[IOItem.cell_pressed]
				if cell_status is not None:
					if not IOInv.full_inv:
						cell_status.pick_item()
						IOLootCombat.loot_buffer[IOItem.cell_pressed] = None
						IOLootCombat.check_loot()

					else:
						IOGUI.message('The inventory is full!')

	if IOLootContainer.active_window:
		if IOLootContainer.focused_window:
			if mouse_down(event, 1, IOLootContainer.loot_rects, multiple_rect=True):
				IOItem.cell_pressed = check_cell_rect(event, 1, IOLootContainer.loot_rects)
				cell_status = sett.current_game['current_container'].loot_items[IOItem.cell_pressed]
				if cell_status is not None:
					if not IOInv.full_inv:
						cell_status.pick_item()
						sett.current_game['current_container'].loot_items[IOItem.cell_pressed] = None
						IOLootContainer.check_loot()

					else:
						IOGUI.message('The inventory is full!')


def controls_items(event):
	"""Defines the interaction with the items"""

	if sett.active_screen == 'game':

		if IOGUI.item_on_cursor is not None:
			if key_down(event, pg.K_DELETE):
				IOItem.delete_item()
				IOInv.update_window()

		equ_item_mov(event)
		inv_item_mov(event)
		if IOEqu.active_window and IOInv.active_window:
			quick_equ(event)

		loot_item_mov(event)


# Combat controls #
def controls_combat(event):
	"""Defines the interaction in combat"""

	if sett.active_screen == 'game':
		if IOCombat.combat_active:
			if IOCombat.combat_menu == 'actions':
				if mouse_down(event, 1, IOCombat.button_attack.rect):
					IOCombat.button_attack.pressed = True
				if IOCombat.button_attack.pressed:
					if mouse_up(event, 1, IOCombat.button_attack.rect):
						IOCombat.char_action('attack')

				if mouse_down(event, 1, IOCombat.button_cast.rect):
					IOCombat.button_cast.pressed = True
				if IOCombat.button_cast.pressed:
					if mouse_up(event, 1, IOCombat.button_cast.rect):
						IOCombat.char_action('cast')

				if mouse_down(event, 1, IOCombat.button_item.rect):
					IOCombat.button_item.pressed = True
				if IOCombat.button_item.pressed:
					if mouse_up(event, 1, IOCombat.button_item.rect):
						IOCombat.char_action('use_item')

				if mouse_down(event, 1, IOCombat.button_retreat.rect):
					IOCombat.button_retreat.pressed = True
				if IOCombat.button_retreat.pressed:
					if mouse_up(event, 1, IOCombat.button_retreat.rect):
						IOCombat.char_action('retreat')

			elif IOCombat.combat_menu == 'cast':
				if mouse_down(event, 1, IOCombat.button_back.rect):
					IOCombat.button_back.pressed = True
				if IOCombat.button_back.pressed:
					if mouse_up(event, 1, IOCombat.button_back.rect):
						IOCombat.combat_menu = 'actions'

				for sk in sett.current_game['skills']:
					if mouse_down(event, 1, sk_button[sk.name].rect):
						sk_button[sk.name].pressed = True
					if sk_button[sk.name].pressed:
						if mouse_up(event, 1, sk_button[sk.name].rect):
							is_sk_possible = sk.cast()
							if is_sk_possible:
								IOCombat.combat_menu = 'actions'
								IOCombat.check_turn = True

			if mouse_up(event, 1):
				for sk in sett.current_game['skills']:
					sk_button[sk.name].pressed = False


# General controls #
def controls_main(event, main_menu):
	"""Interprets the keyboard and mouse events"""

	sett.mouse_pos = pg.mouse.get_pos()

	### Debugging keys ###
	if key_down(event, pg.K_z):
		sett.current_game['current_char'].mod_stats('health', 10)
	if key_down(event, pg.K_x):
		sett.current_game['current_char'].mod_stats('health', -10)
	if key_down(event, pg.K_KP_PLUS):
		sett.current_game['current_char'].mod_stats('spirit', 1)
	if key_down(event, pg.K_KP_MINUS):
		sett.current_game['current_char'].mod_stats('spirit', -1)
	if key_down(event, pg.K_9):
		sett.current_game['current_char'].mod_stats('spirit', 10)

	if sett.current_game['current_container'] is not None:
		if key_down(event, pg.K_b):
			for cell, item in sett.current_game['current_container'].loot_items.items():
				if item is None:
					sett.current_game['current_container'].loot_items[cell] = gen_item()
					break

	if key_down(event, pg.K_p):
		gen_item(iclass='gladius', iqual='magic').pick_item()

	if key_down(event, pg.K_0):
		for cell, item in sett.current_game['inv_items'].items():
			if item is None:
				gen_item(itype='shield', iqual='epic').pick_item() # (iclass='reforged_buckler', iqual='normal').pick_item()

	if key_down(event, pg.K_c):
		for cell, item in sett.current_game['inv_items'].items():
			if item is not None and item != 'locked':
				sett.current_game['inv_items'][cell] = None
				IOInv.update_sub_win(rects=False)

	if key_down(event, pg.K_o):
		IOGUI.message(f'Hello, this is a long text. This is a test with multiple lines.$'
		              f'Super pneumonoultramicroscopicsilicovolcanoconiosis sounds like a very long word to test it out '
		              f'in my message box so we can check the length of this text.')

	if key_down(event, pg.K_y):
		pass

	if key_down(event, pg.K_u):
		if sett.current_game['current_map'] == PrLa:
			sett.current_game['current_map'] = ArPl
		else:
			sett.current_game['current_map'] = PrLa

	######################

	if event.type == pg.QUIT:
		pg.quit()
		quit()

	if IOConfirmWindow.active_win:
		controls_confirm_win(event)

	else:
		controls_main_menu(event, main_menu)
		controls_gui(event)             # Special conditions (e.g. ingame menu button)
		controls_ingame_menu(event)     # if ingame menu

		if not IOGUI.menu_active:
			controls_combat(event)      # if combat_active

			if not IOCombat.combat_active:
				controls_char(event)
				controls_map_interaction(event)
				controls_meditation(event)
				controls_items(event)
