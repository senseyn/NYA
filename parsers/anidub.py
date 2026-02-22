import glob
import time
import requests
from bs4 import BeautifulSoup
import lxml
import re
import qbittorrentapi
import schedule
from icecream import ic



anime_name_list = []


def get_anime_torrent_file():

    try:
        number = 1

        for i in range(1,136):
            response = requests.get(f'https://tr.anidub.com/anime_tv/full/page/{number}/')
            ic(response)
            soup = BeautifulSoup(response.text, 'lxml')
            anime_links = soup.select('div.lcol a[href*="/anime_tv/full/"]')
            for link in anime_links:
                title = link.text.strip()
                if "Законченные сериалы" in title:
                    continue
                url = link['href']
                if url in anime_name_list:
                    continue
                anime_name_list.append(url)
                anime_site = requests.get(f'{url}').content
                soups = BeautifulSoup(anime_site, 'lxml')
                file = soups.find('div', class_='torrent_h').find_all('a')
                title_name = soups.find('span', id='news-title')
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
            host="localhost",
            port=8080,
            username="FAKE",
            password="202000",
        )
        ic(conn_info)
        client = qbittorrentapi.Client(**conn_info)
        ic(client)
        print(f"qBittorrent: {client.app.version}")
        print(f"qBittorrent Web API: {client.app.web_api_version}")

        client.auth_log_in()
        torrent_files = glob.glob('torrent_file/*.torrent')
        ic(torrent_files)
        for torrent_file in torrent_files:
            with open(f'{torrent_file}', 'rb') as f:
                client.torrents_add(
                    torrent_files=[f],
                    save_path="C:/Users/fake/PycharmProjects/saitsave_anime_title/",
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
