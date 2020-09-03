#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os

MODULE_PATH = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
	from src import Mood, Config, Illuca
	CONFIG = Config(MODULE_PATH)
	conn = Illuca(CONFIG.endpoint, os.path.join(MODULE_PATH, "failures_pages"))
	conn.connect(CONFIG.username, CONFIG.password)
	pick = Mood.random_pick()
	print(f"Mood selected: ${pick}")
	pst = conn.post_mood(pick)
	print("Is post successful: ${pst}")
