# import section
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

import time
import logging


if __name__ == '__main__':
    logging.basicConfig(filename="test_report.log",
                        format='%(asctime)s - %(filename)s %(levelname)s: %(message)s',
                        level=logging.INFO)

    # step one Chrome
    try:
        logging.info(f"installing Chrome webdriver")
        driver = webdriver.Chrome(ChromeDriverManager().install())
    except Exception as x:
        logging.error(str(x))
    else:
        logging.info("Installed successfully")

    # step two
    try:
        logging.info("try to navigate to url")
        driver.get('http://automationpractice.com/')
        driver.maximize_window()
    except Exception as x:
        logging.error(str(x))
    else:
        logging.info("url is opened successfully")
        time.sleep(5)

    # step three
    try:
        logging.info("try to find search field")
        search_field = driver.find_element(By.ID, 'search_query_top')
    except Exception as x:
        logging.error(str(x))
    else:
        logging.info("search field found")
    try:
        logging.info("try to find submit search button")
        button_search = driver.find_element(By.NAME, 'submit_search')
    except Exception as x:
        logging.error(str(x))
    else:
        logging.info("submit search button found successfully")
    try:
        logging.info("try to send keys in the search field")
        search_field.send_keys('Product')
    except Exception as x:
        logging.error(str(x))
    else:
        logging.info("keys sent in the search field successfully")
        time.sleep(2)

    # step four
    try:
        logging.info("try to submit search")
        button_search.click()
    except Exception as x:
        logging.error(str(x))
    else:
        logging.info("text in the search field submitted successfully")

    # step five
    try:
        logging.info("try to check the result of search")
        result_list = driver.find_elements(By.XPATH, "//p[@class='alert alert-warning']")
    except Exception as x:
        logging.error(str(x))
    else:
        logging.info("checked successfully")
    if len(result_list) > 0:
        logging.info("element was not found in Chrome")
    else:
        logging.info("element was found in Chrome")

    # step six
    driver.close()

    # step one Firefox
    try:
        logging.info(f"installing Firefox webdriver")
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    except Exception as x:
        logging.error(str(x))
    else:
        logging.info("Installed successfully")

    # step two
    try:
        logging.info("try to navigate to url")
        driver.get('http://automationpractice.com/')
        driver.maximize_window()
    except Exception as x:
        logging.error(str(x))
    else:
        logging.info("url is opened successfully")
        time.sleep(5)

    # step three
    try:
        logging.info("try to find search field")
        search_field = driver.find_element(By.ID, 'search_query_top')
    except Exception as x:
        logging.error(str(x))
    else:
        logging.info("search field found")
    try:
        logging.info("try to find submit search button")
        button_search = driver.find_element(By.NAME, 'submit_search')
    except Exception as x:
        logging.error(str(x))
    else:
        logging.info("submit search button found successfully")
    try:
        logging.info("try to send keys in the search field")
        search_field.send_keys('Product')
    except Exception as x:
        logging.error(str(x))
    else:
        logging.info("keys sent in the search field successfully")
        time.sleep(2)

    # step four
    try:
        logging.info("try to submit search")
        button_search.click()
    except Exception as x:
        logging.error(str(x))
    else:
        logging.info("text in the search field submitted successfully")

    # step five
    try:
        logging.info("try to check the result of search")
        result_list = driver.find_elements(By.XPATH, "//p[@class='alert alert-warning']")
    except Exception as x:
        logging.error(str(x))
    else:
        logging.info("checked successfully")
    if len(result_list) > 0:
        logging.info("element was not found in Firefox")
    else:
        logging.info("element was found in Firefox")

    # step six
    driver.close()

    # step one Edge
    try:
        logging.info(f"installing Edge webdriver")
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    except Exception as x:
        logging.error(str(x))
    else:
        logging.info("Installed successfully")

    # step two
    try:
        logging.info("try to navigate to url")
        driver.get('http://automationpractice.com/')
        driver.maximize_window()
    except Exception as x:
        logging.error(str(x))
    else:
        logging.info("url is opened successfully")
        time.sleep(5)

    # step three
    try:
        logging.info("try to find search field")
        search_field = driver.find_element(By.ID, 'search_query_top')
    except Exception as x:
        logging.error(str(x))
    else:
        logging.info("search field found")
    try:
        logging.info("try to find submit search button")
        button_search = driver.find_element(By.NAME, 'submit_search')
    except Exception as x:
        logging.error(str(x))
    else:
        logging.info("submit search button found successfully")
    try:
        logging.info("try to send keys in the search field")
        search_field.send_keys('Product')
    except Exception as x:
        logging.error(str(x))
    else:
        logging.info("keys sent in the search field successfully")
        time.sleep(2)

    # step four
    try:
        logging.info("try to submit search")
        button_search.click()
    except Exception as x:
        logging.error(str(x))
    else:
        logging.info("text in the search field submitted successfully")

    # step five
    try:
        logging.info("try to check the result of search")
        result_list = driver.find_elements(By.XPATH, "//p[@class='alert alert-warning']")
    except Exception as x:
        logging.error(str(x))
    else:
        logging.info("checked successfully")
    if len(result_list) > 0:
        logging.info("element was not found in Edge")
    else:
        logging.info("element was found in Edge")

    # step six
    driver.close()




