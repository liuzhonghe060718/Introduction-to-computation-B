from selenium import webdriver
from selenium.webdriver.common.by import By
import time
result_list=[]
driver = webdriver.Chrome()
driver.get("https://movie.douban.com/top250")
element_pics=driver.find_element(By.CLASS_NAME,'pic')
for element_pic in element_pics:
    element_a=element_pic.find_element(By.TAG_NAME,'a')
    herf=element_a.get_attribute('herf')
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(herf)
    title=driver.find_element(By.TAG_NAME,'h1').text
    short=driver.find_element(By.CLASS_NAME,'short').text
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
