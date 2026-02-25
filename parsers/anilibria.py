import time
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from selenium import webdriver
import qbittorrentapi
import os

load_dotenv()

conn_info = dict(
        host=os.getenv('QB_HOST'),
        port=int(os.getenv('QB_PORT')),
        username=os.getenv('QB_USER'),
        password=int(os.getenv('QB_PASS')),
    )

client = qbittorrentapi.Client(**conn_info)
client.auth_log_in()

options = webdriver.FirefoxOptions()
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)
driver.get("https://anilibria.top/anime/torrents/")
driver.implicitly_wait(5)
for a in range(1):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
html = driver.page_source
soup = BeautifulSoup(html, 'lxml')
get_title_name = soup.find_all('div', class_='ff-heading lh-120 fz-95')
for title_name in get_title_name:
    print(title_name.text)
get_magnet_url = soup.find_all('a', class_='v-btn v-btn--flat v-theme--dark v-btn--density-comfortable v-btn--size-default v-btn--variant-flat px-2 br-root ml-1')
for a in get_magnet_url:

    magnet_link = a.get('href')
    client.torrents.add(urls=magnet_link, save_path=os.getenv('SAVE_PATH'))

time.sleep(2)

try:
    driver.close()
    driver.quit()
except Exception as e:
    print(e)
