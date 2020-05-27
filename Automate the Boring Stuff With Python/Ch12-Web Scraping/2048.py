# Vasallius

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')
gameover = False
verify = []
whole_page_elem = browser.find_element_by_tag_name('html')

while gameover == False:
    whole_page_elem.send_keys(Keys.UP)
    whole_page_elem.send_keys(Keys.RIGHT)
    whole_page_elem.send_keys(Keys.DOWN)
    whole_page_elem.send_keys(Keys.LEFT)
    gameovertext = browser.find_elements_by_xpath(
        '//div[@class="game-message game-over"]/p')
    if len(gameovertext) == 1:
        verify.append(gameovertext)
    if len(verify) > 0:
        gameover = True

if gameover == True:
    score = browser.find_element_by_class_name('score-container')
    print(f"Game over, you score was {score.text}")
