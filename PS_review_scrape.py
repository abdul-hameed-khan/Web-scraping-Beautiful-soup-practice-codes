from selenium import webdriver
from bs4 import BeautifulSoup
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Chrome('C:/Users/Zulfiqar/selenium web driver/chromedriver.exe')
al = '&showAllReviews=true'
driver.get("https://play.google.com/store/apps/details?id=com.facebook.lite"+al)
time.sleep(5)

rev=[]
i=1
#Will keep scrolling down the webpage until it cannot scroll no more
last_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(3)
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == last_height:
        break
    last_height = new_height
    
soup = BeautifulSoup(driver.page_source,'lxml')
rw = soup.find_all('span',{'jsname':'bN97Pc'})

for r in rw:
    rev.append(r.text)

print(i)
df=pd.DataFrame({'Reviews':rev})
df.to_csv('reviews.csv')








# last_height = driver.execute_script('return document.body.scrollHeight')
# while True:
#     driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
#     time.sleep(3)
#     new_height = driver.execute_script('return document.body.scrollHeight')
#     try:
#         driver.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div/main/div/div[1]/div[2]/div/div['+str(i)+']/div/div[2]/div[2]/span[1]/div/button').click()
#         # time.sleep(5)
#         rev.append(driver.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div/main/div/div[1]/div[2]/div/div['+str(i)+']/div/div[2]/div[2]/span[2]').text)
#     except NoSuchElementException:
#         rev.append(driver.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div/main/div/div[1]/div[2]/div/div['+str(i)+']/div/div[2]/div[2]/span[1]').text)
#     if new_height == last_height:
#         try:
#             driver.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div/main/div/div[1]/div[2]/div[2]/div/span/span').click()
#         except NoSuchElementException:
#             break
#         # break
#     last_height = new_height
#     i=+1
    
    















