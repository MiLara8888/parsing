from bs4 import BeautifulSoup
from selenium import webdriver
import re

from requests_html import HTMLSession
import pyppdf.patch_pyppeteer
import ssl
import random
import urllib3  # две строки убирают ошибку

# первый вариант с селениумом
urllib3.disable_warnings()
driver = webdriver.Chrome()  # открываем сессию
driver.get("https://www.pik.ru/projects/commercial")
block = []
resultHtml = driver.page_source  # перевод в HTML
soup = BeautifulSoup(resultHtml, 'lxml')
for i in soup.find_all('a'):
    if re.match(r'https:\/\/www.pik.ru\/search\/.+\/commercial', 'https://www.pik.ru' + (str(i.get('href')))):
        block.append('https://www.pik.ru' + str(i.get('href')))
driver.close()
print('Блоки сайта - ', block)
print('Колличество блоков -', len(block))

# Второй вариант с requests_html
url1 = 'https://www.pik.ru/projects/commercial'
headers = {'accept': '/',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
session = HTMLSession(verify=False)  # три строки запроса
context = ssl.SSLContext()
r = session.get(url=url1, headers=headers, verify=False)
r.html.render(timeout=random.randrange(20, 31, 1))  # очень важно чтобы все прогрузилось
content = r.html.html  # достаем НТМЛ
block = []
soup = BeautifulSoup(content, "html.parser")
for i in soup.find_all('a'):
    if re.match(r'https:\/\/www.pik.ru\/search\/.+\/commercial', 'https://www.pik.ru' + (str(i.get('href')))):
        block.append('https://www.pik.ru' + str(i.get('href')))
print('Колличество блоков', len(block))
print('Блоки сайта', block)
