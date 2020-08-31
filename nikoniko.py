# Nécessite les packages selenium, datetime, time et numpy :
# 	pip install -U selenium
#   etc...
# Nécessite le navigateur firefox : 
# 	https://www.mozilla.org/fr/firefox/new/
# Nécessite le driver geckodriver (l'utilitaire doit être dans le même répertoire que ce script) :
# 	https://github.com/mozilla/geckodriver/releases

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from datetime import datetime

from numpy.random import choice

import time

USERNAME = 'xxx@noveane.com'
PWD = 'xxx'

ERRORFILE = 'errors.log'
HISTOFILE = 'moods.log'

# check_page and click_mood functions will wait a maximum of WAIT_DELAY * TRIES_UNTIL_TIMEOUT before it kills the script execution
WAIT_DELAY = 1
TRIES_UNTIL_TIMEOUT = 5

MOODS = ('#EE5555','#EE8C55','#CCF576','#62DA84') # de gauche à droite : du pire au meilleur

READABLE_MOODS = {'#EE5555' : 'D:','#EE8C55' : '):','#CCF576' : '(:','#62DA84' : 'C:'}

MOODS_PROB = (0.05,0.25,0.6,0.1) # probabilities of mood, in the same order

def fill_mood():
    browser = webdriver.Firefox()
    browser.get('https://noveane.ilucca.net/identity/login/')
    
    check_page(browser, 'NOVEANE', '''Impossible d'atteindre la page Ilucca''')
    
    elem = browser.find_element_by_name('UserName')
    elem.send_keys(USERNAME)
    
    elem = browser.find_element_by_name('Password')
    elem.send_keys(PWD + Keys.RETURN)
    
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
	fill_mood()