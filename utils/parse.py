import os
import re

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from selenium import webdriver

URL = 'https://holychords.pro'
HEADERS = {
    'user-agent': UserAgent().random
}
service = webdriver.ChromeService(executable_path=os.environ.get("CHROMEDRIVER_PATH"))
options = webdriver.ChromeOptions()
options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
options.add_argument('--headless')
options.add_argument('--disable-dev-shm-usage')   
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=options)


def get_songs(search_name: str):
    search_name = '+'.join(search_name.split(' '))
    response = requests.get(f'{URL}/search?name={search_name}', headers=HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')
    results = [{'href': a['data-audio-id'], 'name': a['data-audio-name'], 'artist': a['data-artist-name']} for a in soup.find_all('a', class_='mr-3 play')]
    return results



def get_text(href: str):
    driver.get(f'{URL}/{href}')
    soup = BeautifulSoup(driver.page_source, 'lxml')
    text_chords = soup.find('pre', id='music_text').get_text()
    for b in soup.find_all('div', class_='blocks'):
        for row in b.find_all('span', class_='chopds'):
            row.decompose()
    text = '\n'.join(['\n'.join([re.sub(r'(\d*\s*(Куплет|куплет|(Пред|пред)*Припев|(Пред|пред)*припев|Приспів|приспів|Брідж|брідж|Бридж|бридж)\d*\s*:*)',
                                        r'\n<b>\1</b>',
                                        i.strip()) for i in b.get_text().split('\n') if i.strip()]) for b in soup.find_all('div', class_='blocks')])

    return text_chords, text