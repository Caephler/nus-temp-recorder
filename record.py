from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from dotenv import load_dotenv
import os
from random import uniform

RECORD_LINK = """https://vafs.nus.edu.sg/adfs/oauth2/authorize?response_type=code&client_id=97F0D1CACA7D41DE87538F9362924CCB-184318&resource=sg_edu_nus_oauth&redirect_uri=https%3A%2F%2Fmyaces.nus.edu.sg%3A443%2Fhtd%2Fhtd"""
PATH_TO_CHROME_DRIVER = "./chromedriver.exe"

def main():
    load_dotenv()
    NUS_USERNAME = os.getenv("NUS_USERNAME")
    NUS_PASSWORD = os.getenv("NUS_PASSWORD")
    AM_TEMP = os.getenv("AM_TEMP")
    PM_TEMP = os.getenv("PM_TEMP")

    if AM_TEMP is None:
        AM_TEMP = generate_random_temp()
    if PM_TEMP is None:
        PM_TEMP = generate_random_temp()

    driver = webdriver.Chrome('./chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get(RECORD_LINK)

    login(driver, NUS_USERNAME, NUS_PASSWORD)
    submit_reading(driver, AM_TEMP, "AM")
    submit_reading(driver, PM_TEMP, "PM")

def generate_random_temp():
    return "{0:0.1f}".format(uniform(36.1, 36.9))


def login(driver, username, password):
    username_elem = driver.find_element_by_id("userNameInput")
    username_elem.clear()
    username_elem.send_keys(username)

    password_elem = driver.find_element_by_id("passwordInput")
    password_elem.clear()
    password_elem.send_keys(password)

    password_elem.send_keys(Keys.RETURN)



def submit_reading(driver, temp, part_of_day):
    # should be on the temperature recording page now

    select_elem = Select(driver.find_element_by_name("declFrequency"))
    select_elem.select_by_visible_text(part_of_day)

    temp_elem = driver.find_element_by_id("temperature")
    temp_elem.send_keys(temp)

    symptoms_elem = driver.find_element_by_css_selector("input[type='radio'][value='N']")
    symptoms_elem.click()

    submit_button = driver.find_element_by_css_selector("input[type='button']")
    submit_button.click()

    # should be on submit page
    back_button = driver.find_element_by_css_selector("input[type='button'][value='Back']")
    back_button.click()





main()
