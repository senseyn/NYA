import glob
import time
import requests
from bs4 import BeautifulSoup
import lxml
import re
import qbittorrentapi
import schedule
from icecream import ic
import json
import os
from dotenv import load_dotenv

load_dotenv()

def get_anime_torrent_file():
    try:
        number = 1
        for i in range(1,2):
            response = requests.get(f'https://tr.anidub.com/anime_tv/full/page/{number}/')
            soup = BeautifulSoup(response.text, 'lxml')
            anime_links = soup.select('div.lcol a[href*="/anime_tv/full/"]')
            for link in anime_links:
                title = link.text.strip()
                if "Законченные сериалы" in title:
                    continue
                url = link['href']

                exists = False
                if os.path.exists('save_anime_title.json'):
                    with open('save_anime_title.json', 'r', encoding='utf-8') as f:
                        for line in f:
                            try:
                                existing_data = json.loads(line)
                                if existing_data.get('url') == url:
                                    exists = True
                                    break
                            except json.JSONDecodeError:
                                continue

                if exists:
                    print('Skip: ', url)
                    continue

                anime_site = requests.get(f'{url}').content
                soups = BeautifulSoup(anime_site, 'lxml')
                file = soups.find('div', class_='torrent_h').find_all('a')
                title_name = soups.find('span', id='news-title')

                anime_data = {
                    "name": title_name.text,
                    "url": url,
                }

                with open('save_anime_title.json', 'a', encoding='utf-8') as f:
                    f.write(json.dumps(anime_data, ensure_ascii=False) + '\n')

                print('Save: ', title_name.text)

                def clean_filename(filename):
                    invalid_chars = r'[\\/*?:"<>|]'
                    cleaned = re.sub(invalid_chars, '!', filename)
                    cleaned = cleaned.replace(' ', '_')
                    return cleaned

                for files in file:
                    href = files['href']
                    with open(f'torrent_file/{clean_filename(title_name.text)}.torrent', 'wb') as f:
                        f.write(requests.get(f"https://tr.anidub.com{href}").content)
            number += 1
    except Exception as e:
        print(e)

def down_anime_title():
    try:
        conn_info = dict(
            host=os.getenv('QB_HOST'),
            port=int(os.getenv('QB_PORT')),
            username=os.getenv('QB_USER'),
            password=int(os.getenv('QB_PASS')),
        )
        ic(conn_info)
        client = qbittorrentapi.Client(**conn_info)
        ic(client)

        client.auth_log_in()
        torrent_files = glob.glob(os.getenv('TORR_FILE'))
        ic(torrent_files)
        for torrent_file in torrent_files:
            with open(f'{torrent_file}', 'rb') as f:
                client.torrents_add(
                    torrent_files=[f],
                    save_path=os.getenv('SAVE_PATH'),
                    is_paused=False
                )

    except qbittorrentapi.LoginFailed as e:
            print(e)

def main():
    print('Program started')
    time.sleep(1)
    print('Down torrent file')
    get_anime_torrent_file()
    print('Done')
    time.sleep(1)
    print('Down anime title')
    down_anime_title()
    print('Done')
    time.sleep(1)
    print('Program ended')

if __name__ == '__main__':
    main()
