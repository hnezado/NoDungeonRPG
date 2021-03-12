from skills import *


def loot(stats=False):
	"""Combine every action after calling for a loot"""

	if stats:
		earn_stats()
		# generate_loot('combat')
		IOLootCombat.open_window()
	else:
		# generate_loot('container')
		IOLootContainer.open_window()


def earn_stats():
	"""Upgrades some stats when success"""

	# Upgrading spirit #
	sett.current_game['current_char'].mod_stats('spirit', 1)
	IOGUI.message(f'I feel a little bit stronger...', 'thought')


def generate_loot(type):
	"""Generates loot"""

	chance = 100

	for cell, item in sett.current_game[type].loot_items.items():
		roll = r.randint(1, 100)
		if item is None:
			if roll < chance:
				chance *= 3/5
				sett.current_game[type].loot_items[cell] = gen_item()
			else:
				break


def update_loot():
	"""Updates and pre-generates loot on creatures and containers"""

	if sett.current_game['current_creature'] is not None:
		if sett.current_game['current_creature'].loot_items is None:
			sett.current_game['current_creature'].loot_items = generate_grid_status(dimensions=(3, 3))
			generate_loot('current_creature')

	if sett.current_game['current_container'] is not None:
		if sett.current_game['current_container'].loot_items is None:
			sett.current_game['current_container'].loot_items = generate_grid_status(dimensions=(3, 3))
			generate_loot('current_container')

# TODO pre-generate the loot on creatures and containers to prevent the "save-load" bug
