#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Nécessite le navigateur firefox : 
# 	https://www.mozilla.org/fr/firefox/new/
# Nécessite le driver geckodriver (l'utilitaire doit être dans le même répertoire que ce script) :
# 	https://github.com/mozilla/geckodriver/releases

import os
import requests
import re


from datetime import datetime
import time


MODULE_PATH = os.path.dirname(os.path.abspath(__file__))
ERRORFILE = 'errors.log'
HISTOFILE = 'moods.log'


def illuca_connection(endpoint, username, password):
	# Maintain the session cookies
	session = requests.Session()
	# grap the login page to fetch the CSRF token
	homePageResponse = session.get(endpoint)
	if homePageResponse.status_code != 200:
		with open(os.path.join(MODULE_PATH, "failed.html"), "wb") as f:
			f.write(homePageResponse.content)
		print(f"Failed to get the home page. Status code {homePageResponse.status_code}")
		exit(1)

	# Fetch the CSRF token
	homePageContent = homePageResponse.content
	regexToken = re.compile("<input name=\"__RequestVerificationToken\" type=\"hidden\" value=\"([a-zA-Z0-9_-]*)")
	token = regexToken.search(str(homePageContent)).group(1)
	if token == '':
		print("Failed to fetch the CSRF token")
		with open(os.path.join(MODULE_PATH, "failed.html"), "wb") as f:
			f.write(homePageResponse.content)
		exit(1)

	# login
	payload = {
		"ReturnUrl":None,
		"UserName":username,
		"Password":password,
		"IsPersistent":"false",
		"__RequestVerificationToken": token
	}
	conn = session.post(endpoint + "/identity/login", data=payload)
	if conn.status_code != 200:
		print(f"Failed to connect. Status code: {conn.status_code}")
		with open(os.path.join(MODULE_PATH, "failed.html"), "wb") as f:
			f.write(conn.content)
		exit(1)

	return session





def fill_mood(config):
    browser = webdriver.Firefox()
    browser.get(config.endpoint + '/identity/login/')
    
    check_page(browser, 'NOVEANE', '''Impossible d'atteindre la page Ilucca''')
    
    elem = browser.find_element_by_name('UserName')
    elem.send_keys(config.username)
    
    elem = browser.find_element_by_name('Password')
    elem.send_keys(config.password + Keys.RETURN)
    
    check_page(browser, 'Lucca | Accueil', 'Impossible de se connecter à Ilucca')
	
    mood = choice(MOODS, 1, p=MOODS_PROB)[0]
	
    moodsFile = open(HISTOFILE, 'a')
    moodsFile.write('\n' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' -> ' + READABLE_MOODS[mood])
    moodsFile.close()
	
    click_mood(browser, mood)
    
    #browser.close()

def click_mood(browser, mood):
    time.sleep(WAIT_DELAY)
    for i in range(TRIES_UNTIL_TIMEOUT) :
        try:
            browser.find_element_by_xpath("//*[name()='svg']//*[name()='circle' and @fill='" + mood + "']").click()
        except:
            time.sleep(WAIT_DELAY)
        else:
            break

def check_page(browser, pageName, errorMessage):
    time.sleep(WAIT_DELAY)
    if browser.execute_script('return document.readyState;') != 'complete' :
        for i in range(TRIES_UNTIL_TIMEOUT) :
            time.sleep(WAIT_DELAY)
            page_state = browser.execute_script('return document.readyState;')
            if page_state == 'complete':
                break
    else:
        try :
            assert pageName in browser.title
        except AssertionError as error:
            logFile = open(ERRORFILE, "a")
            logFile.write('\n' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' : ' + errorMessage + ' (nom de la page atteinte : ' + browser.title + ')')
            logFile.close()
            browser.close()
            exit()

if __name__ == "__main__":
	# session = illuca_connection(CONFIG.endpoint, CONFIG.username, CONFIG.password)
	# print(session)
	from src import Mood, Config
	for i in range(50):
		print(Mood.random_pick())
	print(Config(MODULE_PATH).username)
