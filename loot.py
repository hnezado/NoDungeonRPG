from skills import *


def loot(stats=False):
	"""Combine every action after calling for a loot"""

	if stats:
		earn_stats()
		generate_loot('combat')
		IOLootCombat.open_window()
	else:
		generate_loot('container')
		IOLootContainer.open_window()


def earn_stats():
	"""Upgrades some stats when success"""

	# Upgrading spirit #
	sett.current_game['current_char'].mod_stats('spirit', 1)
	IOGUI.message(f'I feel a little bit stronger...', 'thought')


def generate_loot(type):
	"""Generates loot"""

	chance = 100

	if type == 'combat':
		for cell, item in sett.current_game['current_creature'].loot_items.items():
			roll = r.randint(1, 100)
			if item is None:
				if roll < chance:
					chance *= 3/5
					sett.current_game['current_creature'].loot_items[cell] = gen_item()
				else:
					break

	elif type == 'container':
		if not sett.current_game['current_container'].loot_generated:
			for cell, item in sett.current_game['current_container'].loot_items.items():
				roll = r.randint(1, 100)
				if item is None:
					if roll < chance:
						chance *= 3/5
						sett.current_game['current_container'].loot_items[cell] = gen_item()
					else:
						break
			sett.current_game['current_container'].loot_generated = True
