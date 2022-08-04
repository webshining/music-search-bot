import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

URL = 'https://holychords.pro'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
options = Options()
options.add_argument('headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


def get_html(url: str):
    return requests.get(url, headers=HEADERS)


def find_songs(name: str):
    name = '+'.join(name.split(' '))
    soup = BeautifulSoup(get_html(f'{URL}/search?name={name}').text, 'html.parser')
    result = soup.find_all('div', class_='media-body text-truncate')
    items = [r.find('a') for r in result]
    print([{'href': i['href'][1:], 'name': i.get_text()} for i in items])


def get_text(href: str):
    driver.get(f'{URL}/{href}')
    driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div[1]/div[2]/div/div[2]/div/div[1]/a[2]').click()
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    print([r.get_text(separator='\n') for r in soup.find_all('div', 'blocks')])


get_text('2712')
