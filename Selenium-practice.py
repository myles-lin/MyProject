from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

url = 'https://www.dcard.tw/f'
driver = Chrome('./Resource/chromedriver')

driver.get(url)
driver.find_element(By.TAG_NAME, 'input').send_keys('攝影')
driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/div[1]/div/div/form/button[2]').click()

time.sleep(3)
driver.execute_script('var a = document.documentElement.scrollTop=5000')

time.sleep(3)
driver.execute_script('var a = document.documentElement.scrollTop=10000')

time.sleep(3)
driver.execute_script('var a = document.documentElement.scrollTop=15000')

time.sleep(3)
driver.execute_script('var a = document.documentElement.scrollTop=20000')

html = driver.execute_script("return document.getElementsByTagName('html')[0].outerHTML")

driver.close()

print(html)
