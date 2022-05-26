# import section
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

import time
import logging

# variables section


# function section

def button_check(browser_driver):
    driver.get('http://uitestingplayground.com/')
    classattr_button = browser_driver.find_element(By.XPATH, '//a[contains(text(), "Class Attribute")]')
    classattr_button.click()
    list_of_buttons = browser_driver.find_elements(By.XPATH, '//button[@type="button"]')
    for button in list_of_buttons:
        print(button.get_attribute("class"))


def mouse_click_check(browser_driver):
    browser_driver.get('http://uitestingplayground.com/')
    mouse_over = browser_driver.find_element(By.XPATH, '//a[contains(text(), "Mouse Over")]')
    mouse_over.click()
    click_me_button = browser_driver.find_element(By.XPATH, '//a[@title="Click me"]')
    click_me_button.click()
    count = browser_driver.find_element(By.XPATH, '//span[@id="clickCount"]').text
    print(count)
    time.sleep(2)
# main section


if __name__ == '__main__':
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    button_check(driver)
    driver.get('http://uitestingplayground.com/')
    mouse_click_check(driver)
    driver.close()