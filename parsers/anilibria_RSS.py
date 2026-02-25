import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import lxml
import os
from dotenv import load_dotenv
import qbittorrentapi

load_dotenv()

options = webdriver.FirefoxOptions()
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)

conn_info = dict(
        host=os.getenv('QB_HOST'),
        port=int(os.getenv('QB_PORT')),
        username=os.getenv('QB_USER'),
        password=int(os.getenv('QB_PASS')),
    )
rule_def = {
    "savePath": os.getenv('SAVE_PATH'),
}
client = qbittorrentapi.Client(**conn_info)
client.auth_log_in()

dataset = []
def main():
    try:
        driver.get("https://anilibria.top/anime/torrents/")
        driver.implicitly_wait(5)
        html = driver.page_source

        driver.close()
        driver.quit()

        soup = BeautifulSoup(html, 'lxml')
        title_url = soup.find_all('a', class_= 'v-btn v-btn--flat v-theme--dark v-btn--density-comfortable v-btn--size-default v-btn--variant-flat px-2 br-root')

        for title in title_url:
            if title.attrs['href'] not in dataset:
                dataset.append(title.attrs['href'])

        for item in dataset:
            page = 'https://anilibria.top' + item
            href = requests.get(page).text
            soup = BeautifulSoup(href, 'lxml')
            title_name = soup.find('div', class_ = 'text-autosize ff-heading lh-110 font-weight-bold mb-1').text
            get_rss=soup.find_all('a', class_= 'v-btn v-btn--flat v-theme--dark v-btn--density-default v-btn--size-default v-btn--variant-elevated px-3 br-root ml-2 fill-height')
            for rss in get_rss:
                url = 'https://anilibria.top' + rss.attrs['href']
                feed_data = client.rss.items()
                if title_name in feed_data:
                    print(feed_data[title_name])
                    continue

                client.rss.add_feed(url=url, item_path=title_name)

    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()