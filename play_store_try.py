from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Chrome('C:/Users/Zulfiqar/selenium web driver/chromedriver.exe')
al = '&showAllReviews=true'
driver.get("https://play.google.com/store/apps/details?id=com.google.android.youtube"+al)
time.sleep(5)
# element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div/main/div/div[1]/div[2]/div/div[1]/div/div[2]/div[2]/span[1]/div/button')))

# driver.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div/main/div/div[1]/div[2]/div/div[1]/div/div[2]/div[2]/span[1]/div/button').click()

# time.sleep(5)
# print('\n\n\n\n\n\n')
# r = driver.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div/main/div/div[1]/div[2]/div/div[1]/div/div[2]/div[2]/span[2]')
                                    
# print(r.text)
# print('\n\n\n\n\n\n\n')
# print(driver.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div/main/div/div[1]/div[2]/div/div[2]/div/div[2]/div[2]/span[1]').text)

# print(driver.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div/main/div/div[1]/div[2]/div/div[3]/div/div[2]/div[2]/span[1]').text)
# rev=[]
# for i in range(1,20):
#     try:
#         driver.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div/main/div/div[1]/div[2]/div/div['+str(i)+']/div/div[2]/div[2]/span[1]/div/button').click()
#         time.sleep(5)
#         rev.append(driver.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div/main/div/div[1]/div[2]/div/div['+str(i)+']/div/div[2]/div[2]/span[2]').text)
#     except:
#         rev.append(driver.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div/main/div/div[1]/div[2]/div/div['+str(i)+']/div/div[2]/div[2]/span[1]').text)
# print(rev)

rev=[]
i=1
#Will keep scrolling down the webpage until it cannot scroll no more
last_height = driver.execute_script('return document.body.scrollHeight')
print(last_height)
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(5)
    new_height = driver.execute_script('return document.body.scrollHeight')
    print(last_height)
    if new_height == last_height:
        try:
            driver.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div/main/div/div[1]/div[2]/div[2]/div/span/span').click()
            # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div/main/div/div[1]/div[2]/div[2]/div/span/span'))).click()
        except NoSuchElementException:
            break
        # break
    last_height = new_height
    
    
soup = BeautifulSoup(driver.page_source,'lxml')

# //*[@id="fcxH9b"]/div[4]/c-wiz[2]/div/div[2]/div/div/main/div/div[1]/div[3]/div/div[2]/div[2]/span[1]

# //*[@id="fcxH9b"]/div[4]/c-wiz[2]/div/div[2]/div/div/main/div/div[1]/div[4]/div/div[2]/div[2]/span[1]
# while True:
#     try:
#         driver.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div/main/div/div[1]/div[2]/div/div['+str(i)+']/div/div[2]/div[2]/span[1]/div/button').click()
#         # time.sleep(5)
#         rev.append(driver.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div/main/div/div[1]/div[2]/div/div['+str(i)+']/div/div[2]/div[2]/span[2]').text)
#     except NoSuchElementException:
#         try:
#             rev.append(driver.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div/main/div/div[1]/div[2]/div/div['+str(i)+']/div/div[2]/div[2]/span[1]').text)
#         except NoSuchElementException:
#             break
#     i+=1
# # print(rev)
# df=pd.DataFrame({'Reviews':rev})
# df.to_csv('reviews.csv')
















