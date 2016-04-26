__author__ = 'cmiller'


#from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.by import By
from Wodify_Functions import login, element_wait, browser

get_max = 0
max_value = 0

login()

### Open Athlete Dropdown ###
element_wait(By.ID, "W_Theme_UI_wt19_block_wtMainContent_wtAthleteDropDown_chosen").click()


### Select Athlete ###
browser.find_elements_by_class_name('active-result')[1].click()


### Print Athlete Name ###
athlete_name = browser.find_element_by_xpath('//*[@id="W_Theme_UI_wt19_block_wtMainContent_wtAthleteDropDown_chosen"]/a/span')
print athlete_name.text
#iterate over this list somehow
#list = browser.find_elements_by_class_name('active-result')
#print list


### Set Type to Weightlifting ###

type_dropdown = element_wait(By.ID, 'W_Theme_UI_wt19_block_wtMainContent_wtPCard_wtComponentTypeComboBox')
Select(type_dropdown).select_by_visible_text('Weightlifting')


### Verify Measure Text Box Present Before Setting Component ###

element_wait(By.NAME, 'W_Theme_UI_wt19$block$wtMainContent$wtPCard$wt44')


### Open Component Dropdown ###

#element_wait(By.ID, 'W_Theme_UI_wt19_block_wtMainContent_wtPCard_wtComponentDropDown_chosen').click()


### Select Component ###
#will need to iterate input over list of expected components

components = ['Back Squat', 'Front Squat', 'Deadlift']


def set_components():
    global get_max, max_value
    for i in components:
        #global get_max, max_value
        element_wait(By.ID, 'W_Theme_UI_wt19_block_wtMainContent_wtPCard_wtComponentDropDown_chosen').click()
        element = element_wait(By.CSS_SELECTOR, '#W_Theme_UI_wt19_block_wtMainContent_wtPCard_wtComponentDropDown_chosen > a > span')
        input = element_wait(By.CSS_SELECTOR, '#W_Theme_UI_wt19_block_wtMainContent_wtPCard_wtComponentDropDown_chosen > div > div > input[type="text"]')
        input.send_keys(i + '\n')
        print i
        ### Get 1 Rep Max ###
        time.sleep(.5)
        get_max = element_wait(By.XPATH, '//*[@id="W_Theme_UI_wt19_block_wtMainContent_wtPCard_W_Performance_UI_wt18_block_wtPRWrapper"]/table/tbody/tr[2]/td[1]')
        max_value = get_max.text
        print max_value

# with the debugger the correct measurements are grabbed, implying a page load issue. The get_max element is likely still present from the first value. Need to figure out how to get it to change
#wait while loading is present?
#verify text matches component, return component + '(1x1)'
#need to add error handling if no performance history...

set_components()

browser.quit()