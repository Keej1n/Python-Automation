# import section
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

import time
import logging

# variables section
browser_list = ['chrome', 'edge', 'firefox']
url = 'https://courses.letskodeit.com/practice'
item_list = ['radio button', 'select class', 'multiple element', 'checkbox',
             'switch window', 'switch tab', 'switch to alert', 'web table',
             'enabled/disabled', 'element displayed', 'mouse hover', 'iframe']
dict_of_elements = {}
# function section


def get_xpath(element):
    if element == 'radio button':
        return '//*[@id="radio-btn-example"]/fieldset/label'
    elif element == 'select class':
        return '//*[@id="select-class-example"]/fieldset/select/option'
    elif element == 'multiple element':
        return '//*[@id="multi-select-example-div"]/fieldset/select/option'
    elif element == 'checkbox':
        return '//*[@id="checkbox-example-div"]/fieldset/label'
    elif element == 'switch window':
        return '//*[@id="open-window-example-div"]/fieldset/button'
    elif element == 'switch tab':
        return '//*[@id="open-tab-example-div"]/fieldset/a'
    elif element == 'switch to alert':
        return '//*[@id="alert-example-div"]/fieldset/input'
    elif element == 'web table':
        return '//*[@id="product"]/tbody/tr[2]/td'
    elif element == 'enabled/disabled':
        return '//*[@id="enabled-example-div"]/fieldset/input'
    elif element == 'element displayed':
        return '//*[@id="hide-show-example-div"]/fieldset/input'
    elif element == 'mouse hover':
        return '//*[@id="mouse-hover-example-div"]/div/fieldset/div/div/a'
    elif element == 'iframe':
        return '//*[@id="iframe-example-div"]/fieldset/'   # Idk how to do xpath for this


def get_driver(browser):
    try:
        if browser == 'chrome':
            return webdriver.Chrome(ChromeDriverManager().install())
        elif browser == 'edge':
            return webdriver.Edge(EdgeChromiumDriverManager().install())
        elif browser == 'firefox':
            return webdriver.Firefox(executable_path=GeckoDriverManager().install())
        logging.info(f"{browser} driver successfully installed")
    except:
        logging.error(f"{browser} driver not initialized")


def find_elements_of_url(urls, items_list):
    # step two - navigation to url
    try:
        logging.info(f"try to navigate to {urls}")
        driver.get(urls)
    except Exception as x:
        logging.error(str(x))
    else:
        logging.info("url is opened successfully")
        time.sleep(5)

    # step three - finding elements by css selector
    try:
        for item in items_list:
            logging.info(f"try to find {item}")
            list_of_current_element = driver.find_elements(By.XPATH, get_xpath(item))
            dict_of_elements[item] = len(list_of_current_element)
    except Exception as x:
        logging.error(str(x))
    else:
        logging.info("search is done successfully")


if __name__ == '__main__':
    logging.basicConfig(filename="test_report.log",
                        format='%(asctime)s - %(filename)s %(levelname)s: %(message)s',
                        level=logging.INFO)

    # step one - initialization

    for browser in browser_list:
        logging.info(f"Starting test for {browser} driver")
        driver = get_driver(browser)

        find_elements_of_url(url, item_list)
        print(browser)
        print(f"{dict_of_elements}")
        driver.close()
