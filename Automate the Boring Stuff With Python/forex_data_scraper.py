from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup

start_time = time.time()
profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.folderList', 2)  # custom location
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.download.dir',
                       r'C:\Users\Joseph\Desktop\Forex') #change location
profile.set_preference(
    'browser.helperApps.neverAsk.saveToDisk', 'application/octet-stream')

# GET ALL PAIRS
homepage = requests.get(
    'https://www.histdata.com/download-free-forex-data/?/excel/1-minute-bar-quotes')
soup = BeautifulSoup(homepage.text, 'lxml')
pair_links = []  # List of hrefs
for link in soup.find_all('a')[14:-25]:
    pair_links.append(link.get('href'))
homepage.close()


# LOOPING OVER EACH PAIR LINK
for index, pair_link in enumerate(pair_links):
    pair_link = 'https://www.histdata.com' + pair_links[index]
    pair_page = requests.get(pair_link)
    date_links = []
    soup = BeautifulSoup(pair_page.text, 'lxml')
    for y in soup.find_all('a')[14:-25]:
        date_links.append('https://histdata.com' + y.get('href'))
    # LOOPING OVER EACH DATE OF THE PAIR
    browser = webdriver.Firefox(profile)
    for z in date_links:
        browser.get(z)
        z = browser.find_element_by_id('a_file')
        z.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.1)
        z.click()
        time.sleep(0.2)
    time.sleep(20)
    browser.close()

end_time = time.time()
print(f'{round(end_time-start_time)} have elapsed. Download complete.')
