from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import numpy as np
import time

driver_path = 'C:/Users/Daymo/GithubProjects/Selenium-Fantasy-Football/drivers/chromedriver-win64'  
driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get("https://fantasy.espn.com/football/leaders")

# Initialize an empty list to store the data
all_data = []

# Loop through weeks in the dropdown menu
for week in range(3, 7):
    dropdown = driver.find_element(By.XPATH, f'//*[@id="fitt-analytics"]/div/div[5]/div[2]/div[2]/div[1]/div/div[2]/div[5]/div/div[2]/select/option[{week}]')
    dropdown.click()
    time.sleep(1)

    # Loop through positions
    for position in range(2, 9):
        if position == 6:
            continue
        label = driver.find_element(By.XPATH, f'//*[@id="filterSlotIds"]/label[{position}]')
        label.click()
        time.sleep(1)

        while True:
            try:
                # rows = driver.find_elements(By.XPATH, '//your-xpath-for-rows')
                
                # for row in rows:
                    # data = row.text.split('\n')  # Split the row text into data points
                    # all_data.append(data)  # Add the data to the list
                
                # Click the "Next" button to go to the next page
                button = driver.find_element(By.XPATH, f'//*[@id="fitt-analytics"]/div/div[5]/div[2]/div[3]/div/div/div/div/nav/button[2]')
                button.click()
                time.sleep(2)
            except:
                break

# Convert the collected data into a Pandas DataFrame
df = pd.DataFrame(all_data)
df.sa