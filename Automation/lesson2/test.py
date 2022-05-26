from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time


if __name__ == '__main__':
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://courses.letskodeit.com/practice')
    time.sleep(2)
    radio_btn_list = driver.find_elements(By.XPATH, '//*[@id="radio-btn-example"]/fieldset/label')
    print(len(result_list))
