# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 19:05:04 2021

@author: Zulfiqar
"""


# import requests
# from bs4 import BeautifulSoup

# url = 'https://play.google.com/store/apps/details?id=com.google.android.youtube'

# page = requests.get(url)
# # print(page)

# soup = BeautifulSoup(page.text, 'lxml')

# tag = soup.body.span

# # print(soup.find('div', {'class':'UD7Dzf'}))
# print(soup.find('span', {'jsname':'fbQN7e'}))

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome('C:/Users/Zulfiqar/selenium web driver/chromedriver.exe')
driver.get("https://play.google.com/store/apps/details?id=com.google.android.youtube")
time.sleep(5)
# element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div/main/div/div[1]/div[2]/div/div[2]/div[2]/span[2]')))
# r = driver.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div/main/div/div[1]/div[2]/div/div[2]/div[2]/span[2]/text()')
driver.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div/main/div/div[1]/div[2]/div/div[2]/div[2]/span[1]/div/button').click()
time.sleep(5)
print('\n\n\n\n\n\\n')
r = driver.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div/main/div/div[1]/div[2]/div/div[2]/div[2]/span[2]')
print(r.text)






