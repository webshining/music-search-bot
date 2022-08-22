import requests, re
from bs4 import BeautifulSoup

URL = 'https://holychords.pro'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
CHORDS = ['C', 'D', '']


def get_html(url: str):
    return requests.get(url, headers=HEADERS)


def find_songs(name: str):
    name = '+'.join(name.split(' '))
    soup = BeautifulSoup(get_html(f'{URL}/search?name={name}').text, 'html.parser')
    result = soup.find_all('div', class_='media-body text-truncate')
    items = [r.find('a') for r in result]
    return [{'href': i['href'][1:], 'name': i.get_text()} for i in items]


def get_text(href: str):
    soup = BeautifulSoup(get_html(f'{URL}/{href}').text, 'html.parser')
    elements = soup.find('pre', id='music_text').get_text(separator='\n').split('\n')
    text = [re.sub(
        r'(\d*\s*(Куплет|куплет|(Пред|пред)*Припев|(Пред|пред)*припев|Приспів|приспів|Брідж|брідж|Бридж|бридж):*)',
        r'\n<b>\1</b>', e) for e in elements if
        not re.match('(\s{2,}|\s[A-Z]|#|H|A|D|F|E|C|G|Hm|Em|Cm|Am|Bm|Bb|Ab|Eb|Cb)', e)]
    return '\n'.join(text)
