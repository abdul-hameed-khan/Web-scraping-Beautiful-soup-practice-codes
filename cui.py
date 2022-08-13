

from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome('C:/Users/Zulfiqar/selenium web driver/chromedriver.exe')
driver.get("https://beta.openai.com/playground/p/default-grammar?model=text-babbage-001")
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/p/button[1]').click()
time.sleep(5)


email = driver.find_element_by_xpath('//*[@id="username"]')
email.send_keys('abdulhameed314khan@gmail.com')

p = driver.find_element_by_xpath('//*[@id="password"]')
p.send_keys('khan314hameed')
time.sleep(3)
driver.find_element_by_xpath('/html/body/main/section/div/div/div/form/div[2]/button').click()
time.sleep(8)
# driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div[1]/svg').click()
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div[1]/button/span/span/svg').click()
# time.sleep(2)


driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div/div/div').clear()
time.sleep(1)
# driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div/div/div').click()

rev = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div/div/div')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div[1]/button').click()
time.sleep(3)
rev.send_keys('Very bad app very high price all product and mambership active but price high bad poor app stuped.\n generate a developer reply for this play store app review.')
time.sleep(5)

driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/button[1]').click()

















