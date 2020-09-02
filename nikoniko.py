#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Nécessite le navigateur firefox : 
# 	https://www.mozilla.org/fr/firefox/new/
# Nécessite le driver geckodriver (l'utilitaire doit être dans le même répertoire que ce script) :
# 	https://github.com/mozilla/geckodriver/releases

import os
import requests
import re



MODULE_PATH = os.path.dirname(os.path.abspath(__file__))
ERRORFILE = 'errors.log'
HISTOFILE = 'moods.log'


if __name__ == "__main__":
	# session = illuca_connection(CONFIG.endpoint, CONFIG.username, CONFIG.password)
	from src import Mood, Config
	CONFIG = Config(MODULE_PATH)
