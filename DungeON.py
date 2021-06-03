# TODO bugs to fix:

# Fix loot generation based on creature or container modifiers
# Add friendly attitude
# Add more map and create transaction between them

### IDEAS ###

# Spirit bar can be filled killing creatures or completing actions/requests
# There is a slight chance to learn or improve a magic_skill or ability during meditation

# Vigor is used in every action: (crafting, mining, gathering, fishing, reading...(not combat))

# Food can be found around: fishing, gathering plants or meat (better quality if you cook it)
# Food regenerates hp, mp, and maybe vigor (all with time) and boosts the comfort*

	## ADVANCED ##
# Comfort is affected by some factors like campfire creation, well feeding, bad weather...
# A high level of comfort enhances the meditating/sleeping results

# Trees, mining veins, writings (ancient runes), fishing spots, artifacts studying require learn abilities (non magic)
# and there is a chance to improve known abilities when those actions finish successfully

# There is not a fixed currency to trade with. If any, trades are based on logrolling (favors) and bartering.
# Crux (essence) can be obtained from almost everything you find, and this can be used to craft or enhance objects.
# Crux can be reduced/divided to the most elemental or combined to get a more complex one.
# A special device (Cruxer) is required to divide or combine crux, and knowledge is required to do that.
# Cruxer parts are found along the story. They can be combined to obtain the full device (It may require some knowledge)
# The Cruxer can be upgraded somehow to divide or combine more complex crux.


from controls import *

# gen_item(iclass='ragged_bandana', iqual='unique').pick_item()
# gen_item(iclass='fist_knife', iqual='rare').equip()


def refresh_controls():
	"""Detects if any action takes place"""

	if IOAtlas.fading['transition'] != 'in':
		if not any(pg.key.get_pressed()):
			sett.current_game['current_char'].stop_movement()

	if not any(pg.mouse.get_pressed()):
		IOEqu.gui_button.pressed = False
		IOEqu.close_pressed = False
		IOEqu.move_win_pressed = False
		IOInv.gui_button.pressed = False
		IOInv.close_pressed = False
		IOInv.move_win_pressed = False
		IOLootCombat.close_pressed = False
		IOLootCombat.move_win_pressed = False
		IOLootContainer.close_pressed = False
		IOLootContainer.move_win_pressed = False
		IOMainMenuButton.pressed = False
		IOGUI.menu_but['resume'].pressed = False
		IOGUI.menu_but['save'].pressed = False
		IOGUI.menu_but['load'].pressed = False
		IOGUI.menu_but['settings'].pressed = False
		IOGUI.menu_but['quit'].pressed = False
		if IOGUI.menu_active:
			for socket in IOGUI.menu_but['save_game_buttons'].keys():
				IOGUI.menu_but['save_game_buttons'][socket].pressed = False
				IOGUI.menu_but['delete_game'][socket].pressed = False
			for socket in IOGUI.menu_but['load_game_buttons'].keys():
				IOGUI.menu_but['load_game_buttons'][socket].pressed = False
		IOGUI.menu_but['sound_on'].pressed = False
		IOGUI.menu_but['sound_off'].pressed = False
		IOGUI.menu_but['back'].pressed = False
		IOItem.item_drag = False
		IOCombat.button_attack.pressed = False
		IOCombat.button_cast.pressed = False
		IOCombat.button_item.pressed = False
		IOCombat.button_retreat.pressed = False
		IOCombat.button_back.pressed = False


def intro():
	"""Defines the intro"""

	pass


def main_menu():
	"""Defines the main menu"""

	pass


def game():
	"""Defines the in-game screen"""

	sett.current_game['current_map'].draw_map()
	IOGUI.draw_gui()
	IOCombat.draw_combat()
	IOGUI.draw_menu()
	IOAtlas.check_transition()


def main():
	"""Runs the main script loop"""

	IOGUI.check_saved_games()
	while True:

		for event in pg.event.get():
			controls_main(event)

		intro()
		main_menu()
		game()

		IOGUI.draw_cursor()

		pg.display.update()
		clock(default_clock)

		sett.timer = pg.time.get_ticks()

		refresh_controls()


if __name__ == '__main__':
	main()
