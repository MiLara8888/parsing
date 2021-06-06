from bs4 import BeautifulSoup
from selenium import webdriver
import re
import time
import random

driver = webdriver.Chrome()
driver.get("https://samolet.ru/commercial/")
block = []
resultHtml = driver.page_source
soup = BeautifulSoup(resultHtml, 'lxml')
for i in soup.find_all('a'):
    if re.match(r'\/commercial\/project\/\w+-?\w+\/$', str(i.get('href'))):
        block.append('https://samolet.ru' + str(i.get('href')))
driver.close()
print('Блоки сайта -', block)
print("Колличество блоков -", len(block))

list = []
for i in block:
    driver = webdriver.Chrome()
    driver.get(i)
    time.sleep(random.randrange(5, 10, 1))
    resultHtml = driver.page_source
    time.sleep(random.randrange(5, 10, 1))
    soup = BeautifulSoup(resultHtml, 'lxml')
    for i in soup.find_all('a'):
        if re.match('\/commercial\/project\/\w+-?\w+\/objects\/\d+\/', str(i.get('href'))):
            list.append('https://samolet.ru/' + str(i.get('href')))
    driver.close()
print("Объявления из блоков -", list)
print('Колличество объявлений из блоков', len(list))
