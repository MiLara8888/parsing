from bs4 import BeautifulSoup
from selenium import webdriver
import re
import time

driver = webdriver.Chrome()
driver.get("https://www.ingrad.ru/commercial/")
block = []
resultHtml = driver.page_source
soup = BeautifulSoup(resultHtml, 'lxml')
for i in soup.find_all(class_='overlink'):
    if re.match(r'\/projects\/\w+\/select\/commercial\/all', str(i.get('href'))):
        block.append('https://www.ingrad.ru' + str(i.get('href')))
driver.quit()
print(f'Блоки главного экрана-{block}')
list = []
for i in block:
    driver = webdriver.Chrome()
    driver.get(i)
    time.sleep(5)
    resultHtml = driver.page_source
    time.sleep(5)
    soup = BeautifulSoup(resultHtml, 'lxml')
    for i in soup.find_all('a'):
        if re.match(r'https:\/\/www\.ingrad\.ru\/\w+\/apartment\/\d+', 'https://www.ingrad.ru' + str(i.get('href'))):
            list.append('https://www.ingrad.ru' + str(i.get('href')))

    driver.close()
print(f'Объявления на сайте - {list}')
print(f'Колличество объявлений- {len(list)}')
