
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
time.sleep(10)


while driver.find_element_by_tag_name('div'):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    Divs=driver.find_element_by_tag_name('div').text
    if 'End of Results' in Divs:
        print ('end')
        break
    else:
        continue