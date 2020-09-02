#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Nécessite le navigateur firefox : 
# 	https://www.mozilla.org/fr/firefox/new/
# Nécessite le driver geckodriver (l'utilitaire doit être dans le même répertoire que ce script) :
# 	https://github.com/mozilla/geckodriver/releases

import os

MODULE_PATH = os.path.dirname(os.path.abspath(__file__))
ERRORFILE = 'errors.log'
HISTOFILE = 'moods.log'

if __name__ == "__main__":
	from src import Mood, Config, Illuca
	CONFIG = Config(MODULE_PATH)
	conn = Illuca(CONFIG.endpoint, os.path.join(MODULE_PATH, "failures_pages"))
	conn.connect(CONFIG.username, CONFIG.password)
	print(conn)
