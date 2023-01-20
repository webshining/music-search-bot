import re
import aiohttp
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
URL = 'https://holychords.pro'
HEADERS = {
    'User-Agent': ua.chrome
}


async def get_musics(search_name: str):
    search_name = '+'.join(search_name.split(' '))
    musics = []
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{URL}/search?name={search_name}', headers=HEADERS) as response:
            soup = BeautifulSoup(await response.text(), "lxml")
            results = soup.find_all('a', class_='mr-3 play')
            for result in results:
                href = result['data-audio-id']
                name = result['data-audio-name']
                artist =result['data-artist-name']
                musics.append({'href': href, 'name': name, 'artist': artist})
    return musics


async def get_text(href: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{URL}/{href}', headers=HEADERS) as response:
            soup = BeautifulSoup(await response.text(), 'lxml')
            result = soup.find('pre', id='music_text').get_text(separator='\n').split('\n')
            return '\n'.join([
                re.sub(
                    r'(\d*\s*(Куплет|куплет|(Пред|пред)*Припев|(Пред|пред)*припев|Приспів|приспів|Брідж|брідж|Бридж|бридж)\d*\s*:*)',
                    r'\n<b>\1</b>',
                    i.strip()
                ) for i in result if i.strip()])
