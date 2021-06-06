from requests_html import HTMLSession
import pyppdf.patch_pyppeteer
import ssl
from bs4 import BeautifulSoup
import re
import time
import random
import urllib3

urllib3.disable_warnings()
url1 = 'https://samolet.ru/commercial/'
headers = {'accept': '/',
           'user-agent': 'user'}  #поставить агента
session = HTMLSession(verify=False)  # три строки запроса
context = ssl.SSLContext()
r = session.get(url=url1, headers=headers, verify=False)
r.html.render(timeout=random.randrange(20, 31, 1))  # очень важно чтобы все прогрузилось
content = r.html.html
spisok = []
soup = BeautifulSoup(content, "html.parser")
for i in soup.find_all('a'):
    if re.match(r'\/commercial\/project\/\w+-?\w+\/$', str(i.get('href'))):  # row строкa убрала ненужную ссылку
        spisok.append('https://samolet.ru' + str(i.get('href')))
print(spisok)
print(len(spisok))

spisok_block_samolet=[]
for i in spisok:
    url_block = i
    session = HTMLSession(verify=False)  # три строки запроса
    context = ssl.SSLContext()
    r = session.get(url=i, headers=headers, verify=False)
    time.sleep(5)
    r.html.render(timeout=random.randrange(80, 90, 1))  # очень важно чтобы все прогрузилось
    content = r.html.html
    soup = BeautifulSoup(content, 'html.parser')
    for i in soup.find_all('a'):
        if re.match(r'\/commercial\/project\/\w+-?\w+\/objects\/\d+\/', str(i.get('href'))):
            spisok_block_samolet.append('https://samolet.ru/' + str(i.get('href')))

print(spisok_block_samolet)
print(len(spisok_block_samolet))
