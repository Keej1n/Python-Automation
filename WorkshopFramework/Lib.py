from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BrowserManager:
    @staticmethod
    def browser():
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.maximize_window()
        return browser

    @staticmethod
    def close_browser(browser):
        if browser:
            browser.quit()

    @staticmethod
    def count_elements(browser, loc):
        checker = WebDriverWait(browser, 10).until(
            EC.text_to_be_present_in_element(loc, "Selenium"))
        if checker:
            my_list = browser.find_elements(*loc)
            print(len(my_list))
        else:
            print(0)

    @staticmethod
    def found_and_click(browser, loc):
        button = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(loc))
        button.click()

    @staticmethod
    def found_input_and_fill(browser, loc, text):
        input_field = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(loc))
        input_field.send_keys(text)

    @staticmethod
    def load(browser, link):
        browser.get(link)

    @staticmethod
    def check_url(browser, url):
        if browser.current_url != url:
            BrowserManager.load(browser, url)
