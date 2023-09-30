from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import numpy as np
import time

driver_path = 'C:/Users/Daymo/GithubProjects/Selenium-Fantasy-Football/drivers/chromedriver-win64'  
driver = webdriver.Chrome()
# driver.implicitly_wait(1)
driver.get("https://fantasy.espn.com/football/leaders")

time.sleep(3)

label = driver.find_element(By.XPATH, f'//*[@id="filterSlotIds"]/label[{8}]')
label.click()
time.sleep(3)

i = 1
try:
    button = driver.find_element(By.XPATH, f'//*[@id="fitt-analytics"]/div/div[5]/div[2]/div[3]/div/div/div/div/nav/button[2]')
    

    while button.is_enabled():
        print(f'displayed: {button.is_displayed()}')
        print(f'enabled: {button.is_enabled()}')
     
        button.click()
        time.sleep(2)
        print(f'Button clicked: {i}')
        i+=1
        print(f'displayed: {button.is_displayed()}')
        print(f'enabled: {button.is_enabled()}')
    

except:
    pass
    print('Button not found')