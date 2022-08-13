# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 09:50:39 2021

@author: Zulfiqar
"""


import requests
from bs4 import BeautifulSoup

url = 'https://www.marketwatch.com/investing/stock/aapl'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')
tag = soup.find('bg-quote',class_ = 'value')
# print(tag.text)

# print(soup.find('td', class_ = 'table__cell u-semi').text)

tg = soup.find_all('div', class_ = 'range__header')[2]
tg2= tg.find_all('span', class_ = 'primary')
# for i in tg2:
#     print(i.text)
# print(tg2)

# tg3 = soup.find_all('ul', class_ = 'analyst__rating')
tg3 = soup.find_all('li', class_ = 'analyst__option')[3]
print(tg3.text)