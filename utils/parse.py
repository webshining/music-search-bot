import re
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
URL = 'https://holychords.pro'
HEADERS = {
    'User-Agent': ua.chrome
}


def get_names(name: str):
    if name:
        name = '+'.join(name.split(' '))
        soup = BeautifulSoup(requests.get(f"{URL}/search?name={name}", headers=HEADERS).text, "html.parser")
        names = soup.findAll('div', class_='media-body text-truncate')
        names = [{"href": n.find('a')['href'], "name": n.find('a').text,
                "group": re.sub('\\n|\\t', '', n.find('div', class_='text-muted text-truncate w-100').text)} for n in names]
    return names if name else None


def get_text(href: str):
    soup = BeautifulSoup(requests.get(f"{URL}/{href}", headers=HEADERS).text, "html.parser")
    text = soup.find('pre', id='music_text').get_text(separator='\n').split('\n')
    text = [
        re.sub(
            r'(\d*\s*(Куплет|куплет|(Пред|пред)*Припев|(Пред|пред)*припев|Приспів|приспів|Брідж|брідж|Бридж|бридж):*)', 
            r'\n<b>\1</b>', 
            t
        ) for t in text if not re.match('(\s{2,}|\s[A-Z]|#|H|A|D|F|E|C|G|Hm|Em|Cm|Am|Bm|Bb|Ab|Eb|Cb)', t)
    ]
    return '\n'.join(text)
