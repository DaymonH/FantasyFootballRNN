from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import  Select
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd
# import numpy as np
import time

position = {'QB': 2, 'RB': 3, 'WR': 4, 'TE': 5, 'D/ST': 7, 'K': 8}
week = {"NFL Week 1": 3, "NFL Week 2": 4, "NFL Week 3": 5, "NFL Week 4": 6}

driver = webdriver.Chrome()
driver.get("https://fantasy.espn.com/football/leaders")

# Initialize an empty list to store the data
all_data = []
time.sleep(4)
for week, week_index in week.items():
    dropdown = driver.find_element(By.XPATH, f'//*[@id="fitt-analytics"]/div/div[5]/div[2]/div[2]/div[1]/div/div[2]/div[5]/div/div[2]/select/option[{week_index}]')
    print(f'Week: {week}')
    dropdown.click()
    time.sleep(3)

    # Loop through positions
    for position, position_index in position.items():
        print(f'Position: {position}')
        label = driver.find_element(By.XPATH, f'//*[@id="filterSlotIds"]/label[{position_index}]')
        label.click()
        time.sleep(5)

        while True: 
            i = 0
            try: 

                # Find all the rows in the table
                rows = driver.find_elements(By.XPATH, '//*[@id="espn-analytics"]/div/div[5]/div[2]/div[3]/div/div/div/table/tbody/tr')
                for row in rows:
                    data = []
                    # Extract data from each column in the row
                    columns = row.find_elements(By.TAG_NAME, 'td')
                    for column in columns:
                        data.append(column.text)
                    # Add the "Week" information
                    data.append(week_name)
                    # Append the data to the all_data list
                    all_data.append(data)


                button = driver.find_element(By.XPATH, f'//*[@id="fitt-analytics"]/div/div[5]/div[2]/div[3]/div/div/div/div/nav/button[2]')
                while button.is_enabled():
                    button.click()
                    print(f' Next Page Button clicked: {i}')
                    i+=1
                    time.sleep(5)
                break
            except Exception as e:
                print('Button not found')
                break
                


        
