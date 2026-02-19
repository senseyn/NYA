import time
from bs4 import BeautifulSoup
import lxml
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument('--headless')
driver = webdriver.Firefox()

driver.get("https://myanimelist.net/anime/season/2026/winter")
driver.implicitly_wait(5)
html = driver.page_source

soup = BeautifulSoup(html, 'lxml')
element = soup.find_all('div', class_='js-anime-category-producer seasonal-anime js-seasonal-anime js-anime-type-all js-anime-type-1')
for elements in element:
    href = elements.find('a')['href']
    print(href)
    driver.get(href)
    driver.implicitly_wait(5)
    time.sleep(5)
    html_title = driver.page_source
    soups = BeautifulSoup(html_title, 'lxml')
    try:
        title_orig = soups.find('div', id='contentWrapper').find('h1', class_='title-name h1_bold_none').text
        print(title_orig)
    except:
        print('no title name')
    try:
        title_en = soups.find('div', id='contentWrapper').find('p', class_='title-english title-inherit').text
        print(title_en)
    except:
        print('no title name en')

driver.close()
driver.quit()