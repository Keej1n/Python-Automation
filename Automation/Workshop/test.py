# import section'
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time


url = 'https://www.amazon.com/'
xpath_search_by_id = 'nav-search-submit-button'
xpath_search_field_by_id = 'twotabsearchtextbox'
xpath_fivestar = '//*[@class = "a-icon a-icon-star-small a-star-small-5 aok-align-bottom"]'

if __name__ == '__main__':
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    driver.maximize_window()
    search_field = driver.find_element(By.ID, xpath_search_field_by_id)
    search_field.send_keys("lol")
    submit_button = driver.find_element(By.ID, xpath_search_by_id)
    submit_button.click()
    five_star = driver.find_elements(By.XPATH, xpath_fivestar)
    print(len(five_star))
    time.sleep(5)