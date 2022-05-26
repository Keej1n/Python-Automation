# import section
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

import time
import logging

# variables section
url = 'https://www.hyrtutorials.com/p/add-padding-to-containers.html'
browser_list = ['chrome', 'edge', 'firefox']
checkbox_of_countries = ["Germany", "Mexico", "Austria", "Canada", "Italy"]

# function section


def get_driver(choose_browser):
    try:
        if choose_browser == 'chrome':
            return webdriver.Chrome(ChromeDriverManager().install())
        elif choose_browser == 'edge':
            return webdriver.Edge(EdgeChromiumDriverManager().install())
        elif choose_browser == 'firefox':
            return webdriver.Firefox(executable_path=GeckoDriverManager().install())
    except:
        logging.error(f"{choose_browser} driver not initialized")
    else:
        logging.info(f"{choose_browser} driver successfully installed")


def input_field_test(browser_driver):
    # first name
    try:
        logging.info('try to send first name')
        first_name_input_field = browser_driver.find_element(
            By.XPATH, "//input[1]")
        first_name_input_field.send_keys('Ildar')
    except Exception as x:
        logging.error(str(x))
    else:
        logging.info("first name sent successfully")
    # last name
    try:
        logging.info('try to send last name')
        last_name_input_field = browser_driver.find_element(
            By.XPATH, "//input[2]")
        last_name_input_field.send_keys('Sabirov')
    except Exception as x:
        logging.error(str(x))
    else:
        logging.info("last name sent successfully")
    # mail
    try:
        logging.info('try to send email')
        mail_input_field = browser_driver.find_element(
            By.XPATH, "//input[3]")
        mail_input_field.send_keys("eldarsabirovv@gmail.com")
    except Exception as x:
        logging.error(str(x))
    else:
        logging.info("email sent successfully")
    # password
    try:
        logging.info("try to send password")
        password_input_field = browser_driver.find_element(
            By.XPATH, '//*[@class="container"]/div/input')
        password_input_field.send_keys('1q2s3c4r5g6n7u8k9.0p')
    except Exception as x:
        logging.error(str(x))
    else:
        logging.info("password sent successfully")
    # password repeat
    try:
        logging.info("try to send password repeat")
        password_repeat_input_field = browser_driver.find_element(
            By.XPATH, '//input[4]')
        password_repeat_input_field.send_keys('1q2s3c4r5g6n7u8k9.0p')
    except Exception as x:
        logging.error(str(x))
    else:
        logging.info("password repeat sent successfully")
    # register button
    try:
        logging.info("try to click submit button")
        submit_button = browser_driver.find_element(
            By.XPATH, "//button[@type='submit']")
        submit_button.click()
    except Exception as x:
        logging.error(str(x))
    else:
        logging.info("submit button clicked successfully")
    logging.info("input field test completed successfully")


def checkbox_test(browser_driver):
    for country in checkbox_of_countries:
        try:
            logging.info(f"try to click {country} checkbox")
            current_country = browser_driver.find_element(
                By.XPATH,
                f'//td[contains(text(),"{country}")]/ancestor::tr/td/input')
            current_country.click()
        except Exception as x:
            logging.error(str(x))
        else:
            logging.info(f"{country} checkbox clicked successfully")
    logging.info("Checkbox test completed successfully")

# main section


if __name__ == '__main__':
    logging.basicConfig(filename="test_report.log",
                        format='%(asctime)s - %(filename)s %(levelname)s: %(message)s',
                        level=logging.INFO)
    for browser in browser_list:
        logging.info(f"Starting test for {browser} driver")
        driver = get_driver(browser)
        driver.get(url)
        time.sleep(2)
        input_field_test(driver)
        time.sleep(2)
        checkbox_test(driver)
        time.sleep(2)
        driver.close()
