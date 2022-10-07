from items import *

img_sk_icons = Sheet('data/images/skills/sk_icons.png', dimensions=(1, 6))
all_skills = []
learnable_skills = []


sk_button = {
		'Heal': Button(screen, bg=IOGUI.img_but_bg50, icon=img_sk_icons, pos=(0, 0), sheet_index=1),
		'Regeneration': Button(screen, bg=IOGUI.img_but_bg50, icon=img_sk_icons, pos=(0, 0), sheet_index=2),
		'Boost damage': Button(screen, bg=IOGUI.img_but_bg50, icon=img_sk_icons, pos=(0, 0), sheet_index=3),
		'Life leech': Button(screen, bg=IOGUI.img_but_bg50, icon=img_sk_icons, pos=(0, 0), sheet_index=4),
		'Boost critical': Button(screen, bg=IOGUI.img_but_bg50, icon=img_sk_icons, pos=(0, 0), sheet_index=5)
}


class Skill:
	def __init__(self):
		self.name = None
		self.img_index = None

		self.level = None
		self.learned = False
		self.mana_cost = None

	def message(self):

		if self.name is not None:
			IOGUI.message(f'Casting {self.name.lower()}!', 'combat')
		else:
			IOGUI.message(f'Skill not available')

	def castable(self):
		"""Checks if the skill is castable"""

		if self.mana_cost is not None:
			if sett.current_game['current_char'].chstats['mana'] >= self.mana_cost:
				return True
			else:
				IOGUI.message(f'I need more mana', 'thought')
		else:
			return True

	def cast(self):
		"""Casts the skill"""

		if self.castable():
			if self.mana_cost is not None: sett.current_game['current_char'].mod_stats('mana', -self.mana_cost)
			self.message()
			self.skill()
			return True

	def skill(self):
		"""Defines the skill action"""

	@staticmethod
	def learn_new_skill():
		"""Learns a new skill based on the skill level"""

		sk =  r.choice(learnable_skills)
		sk.learned = True
		learnable_skills.remove(sk)

	def update_skills(self, ):
		"""Updates the skills lists"""

		if self not in all_skills:
			all_skills.append(self)

		sett.current_game['skills'] = []
		learnable_skills.clear()

		for sk in all_skills:
			if sk.learned:
				sett.current_game['skills'].append(sk)
			else:
				learnable_skills.append(sk)

		sett.current_game['skills'].sort(key=lambda x: x.level)


class Heal(Skill):
	def __init__(self):
		super().__init__()

		self.name = 'Heal'
		self.img_index = 1
		self.level = 1
		self.learned = True
		self.mana_cost = 10

		self.update_skills()

	def skill(self):
		"""Casts the heal skill"""

		sett.current_game['current_char'].mod_stats('health', 15)


class Regeneration(Skill):
	def __init__(self):
		super().__init__()

		self.name = 'Regeneration'
		self.img_index = 2
		self.level = 10
		self.learned = True
		self.mana_cost = 25

		self.update_skills()

	def skill(self):
		"""Casts the regeneration skill"""


class BoostDamage(Skill):
	def __init__(self):
		super().__init__()

		self.name = 'Boost damage'
		self.img_index = 3
		self.level = 5
		self.learned = True
		self.mana_cost = 2

		self.update_skills()

	def skill(self):
		"""Casts the boost damage skill"""


class LifeLeech(Skill):
	def __init__(self):
		super().__init__()

		self.name = 'Life leech'
		self.img_index = 4
		self.level = 15
		self.learned = True
		self.mana_cost = 3

		self.update_skills()

	def skill(self):
		"""Casts the life leech skill"""

		char_damage = r.randint(int(sett.current_game['current_char'].chstats['min_att']),
		                        int(sett.current_game['current_char'].chstats['max_att']))
		sett.current_game['current_char'].mod_stats('health', int(char_damage*0.5))
		sett.current_game["current_creature"].mod_cr_stats('health', -char_damage)


class BoostCritical(Skill):
	def __init__(self):
		super().__init__()

		self.name = 'Boost critical'
		self.img_index = 5
		self.level = 20
		self.learned = True
		self.mana_cost = 5

		self.update_skills()

	def skill(self):
		"""Casts the boost critical skill"""


IOHeal = Heal()
IORegeneration = Regeneration()
IOBoostDamage = BoostDamage()
IOLifeLeech = LifeLeech()
IOBoostCritical = BoostCritical()
