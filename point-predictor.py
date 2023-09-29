from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import time
# Set the path to the WebDriver executable (change this to the actual path)
driver_path = 'C:/Users/Daymo/GithubProjects/Selenium-Fantasy-Football/drivers/chromedriver-win64'  

# Initialize the WebDriver with the path to the executable
driver = webdriver.Chrome()
driver.implicitly_wait(2)
# Navigate to a website
# driver.get("https://fantasy.espn.com/football/leaders?leagueId=2118196454")
driver.get("https://fantasy.espn.com/football/leaders")

'''All weeks in the dropdown meny'''
for i in range(3,7):
    dropdown = driver.find_element(By.XPATH, f'//*[@id="fitt-analytics"]/div/div[5]/div[2]/div[2]/div[1]/div/div[2]/div[5]/div/div[2]/select/option[{i}]')
    dropdown.click()
    time.sleep(1)

'''All positions in radion buttons'''
for i in range(2,9):
    if i == 6:
        continue
    label = driver.find_element(By.XPATH, f'//*[@id="filterSlotIds"]/label[{i}]')
    label.click()
    time.sleep(1)
    
'''Go to next page until at the end for a given position and week'''
while True:
    try:
        # Locate and click the "Next" button
        button = driver.find_element(By.XPATH, f'//*[@id="fitt-analytics"]/div/div[5]/div[2]/div[3]/div/div/div/div/nav/button[2]')
        button.click()
        time.sleep(2)
    except NoSuchElementException:
        # The "Next" button is no longer available, exit the loop
        break
