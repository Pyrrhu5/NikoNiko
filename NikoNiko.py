#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
from datetime import datetime

MODULE_PATH = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
	from src import Mood, Config, Illuca
	CONFIG = Config(MODULE_PATH)

	# Print current date for logs
	print("="*80)
	today = datetime.today().strftime("%d/%m/%y")
	print(f"{' ' * ((80 - len(today))//2)}{today}")
	print("="*80)

	conn = Illuca(CONFIG.endpoint, os.path.join(MODULE_PATH, "failures_pages"))
	conn.connect(CONFIG.username, CONFIG.password)
	pick = Mood.random_pick()
	print(f"Mood selected: {pick}")
	pst = conn.post_mood(pick)
	print(f"Is post successful: {pst}")
