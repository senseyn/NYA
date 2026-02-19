import requests
from bs4 import BeautifulSoup
import lxml
import re

response = requests.get('https://tr.anidub.com/anime_tv/full/page/1/')
soup = BeautifulSoup(response.text, 'lxml')
anime_links = soup.select('div.lcol a[href*="/anime_tv/full/"]')

for link in anime_links:
    title = link.text.strip()
    if "Законченные сериалы" in title:
        continue
    url = link['href']

    anime_site = requests.get(f'{url}').content
    soups = BeautifulSoup(anime_site, 'lxml')
    file = soups.find('div', class_='torrent_h').find_all('a')
    title_name = soups.find('span', id='news-title')

    def clean_filename(filename):
        invalid_chars = r'[\\/*?:"<>|]'
        cleaned = re.sub(invalid_chars, '!', filename)
        cleaned = cleaned.replace(' ', '_')
        return cleaned

    for files in file:
        href = files['href']
        with open(f'{clean_filename(title_name.text)}.torrent', 'wb') as f:
            f.write(requests.get(f"https://tr.anidub.com{href}").content)

