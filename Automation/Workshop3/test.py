# import section
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import time

url = 'https://volo.global/'
company_xpath = '//li[@data-menu-article="company"]//a'


if __name__ == '__main__':
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    company = driver.find_element(By.XPATH, company_xpath)
    company.click()
    careers = driver.find_element(By.XPATH, '//a[contains(text(), "Careers")]')
    careers.click()
    careerslist = WebDriverWait(driver, 10).until(
        ec.visibility_of_all_elements_located((By.XPATH, '//a[@class="job"]/h4')))
    for careers in careerslist:
        print(careers.text)