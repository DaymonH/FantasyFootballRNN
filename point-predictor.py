from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd
import numpy as np
import time

position = {'QB': 2, 'RB': 3, 'WR': 4, 'TE': 5, 'D/ST': 7, 'K': 8}
week = {"NFL Week 1": 3, "NFL Week 2": 4, "NFL Week 3": 5, "NFL Week 4": 6}

driver_path = 'C:/Users/Daymo/GithubProjects/Selenium-Fantasy-Football/drivers/chromedriver-win64'  
driver = webdriver.Chrome()
driver.get("https://fantasy.espn.com/football/leaders")

# Initialize an empty list to store the data
all_data = []
time.sleep(4)
for key, value in week.items():
    dropdown = driver.find_element(By.XPATH, f'//*[@id="fitt-analytics"]/div/div[5]/div[2]/div[2]/div[1]/div/div[2]/div[5]/div/div[2]/select/option[{value}]')
    print(f'Week: {key}')
    dropdown.click()
    time.sleep(3)

    # Loop through positions
    for key, value in position.items():
        print(f'Week: {key}')
        label = driver.find_element(By.XPATH, f'//*[@id="filterSlotIds"]/label[{value}]')
        label.click()
        time.sleep(5)

        try: 
            button = driver.find_element(By.XPATH, f'//*[@id="fitt-analytics"]/div/div[5]/div[2]/div[3]/div/div/div/div/nav/button[2]')
            while button.is_enabled():
                button.click()
                print(f' Next Page Button clicked: {i}')
                i+=1
                time.sleep(5)
        except:
            pass
            print('Button not found')


        
