# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 18:46:06 2021

@author: Zulfiqar
"""

import requests
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers'

page = requests.get(url)
# print(page)

soup = BeautifulSoup(page.text, 'lxml')
# print(soup)

# TAGS
# print(soup.header.p.string) # will only get first occurence div

# print(soup.div) will only get first occurence div

# ATTRIBUTES

tag = soup.header.a
# print(tag.attrs)
# print(tag['data-toggle']) # accessing specific tag

tag['new_attr'] = 'this is new attribute'  # this will add the new attribute to our html code

# print(tag.attrs)

# FIND
# print(soup.find('header')) 

print(soup.find('div', {'class':'col-md-3'}))
# print(soup.find('h4', {'class':'pull-right price'}))









